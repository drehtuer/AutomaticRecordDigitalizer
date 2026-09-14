"""Render the machine to PNG images for the documentation, with no renderer but numpy.

    python -m cad.render                     # every still view into docs/images/
    python -m cad.render rear deck-end       # named views only
    python -m cad.render --animate           # the cycle for every record size, as animated PNG
    python -m cad.render --animate 7 --frames 72 --width 640

Each still is an orthographic projection of the machine at the home pose, with the carousel's
demonstration load in the slots, the electronics on the frame, and the chains and cables as the
model draws them. An animation samples the planner's keyframes at even intervals of the same
timeline the web viewer plays, places every rigid body exactly as the viewer does, and writes the
frames as one animated PNG. The parts are tessellated once, shaded with one light, and rasterised
through a depth buffer; the result is a picture of the model, not a photograph of anything.
"""
import argparse
import struct
import zlib
from math import cos, radians, sin
from pathlib import Path

import numpy as np

from . import kinematics as K
from .assembly import Machine, color_of
from .export_web import rest_parts, scene
from .parts.carousel import DEMO_LOAD, RADII

OUT = Path(__file__).parent.parent / "docs" / "images"
WIDTH, HEIGHT = 1600, 1000
TOLERANCE, ANGULAR = 1.0, 0.4
BACKGROUND = (0.97, 0.97, 0.96)

# name: (azimuth about Z from +X, elevation above the horizon, degrees). The camera looks at the
# machine from that direction; +Y is the front of the bench.
VIEWS = {
    "overview": (35.0, 28.0),      # from the front, deck end nearer
    "rear": (-88.0, 12.0),         # from behind: the controller group, the pump, the X chain
    "deck-end": (2.0, 10.0),       # from beyond the deck-end panel: the Pi group
    "top": (0.0, 89.0),            # straight down
    "carousel": (155.0, 30.0),     # from the open end, over the carousel
}
ANIMATION_VIEW = (35.0, 24.0)


# ---------------------------------------------------------------- geometry
def camera(az, el):
    """Right, up and towards-the-viewer unit vectors for a camera at azimuth az and elevation el."""
    a, e = radians(az), radians(el)
    view = np.array([cos(e) * cos(a), cos(e) * sin(a), sin(e)])     # from the scene towards the camera
    up0 = np.array([0.0, 0.0, 1.0])
    right = np.cross(up0, view)
    right /= np.linalg.norm(right)
    up = np.cross(view, right)
    return right, up, view


def mesh(solid, name, tolerance=TOLERANCE, angular=ANGULAR):
    verts, faces = solid.val().tessellate(tolerance, angular)
    v = np.array([(p.x, p.y, p.z) for p in verts], dtype=np.float64)
    f = np.array(faces, dtype=np.int64)
    return v, f, np.array(color_of(name), dtype=np.float64)


def still_parts(size="12"):
    """Every part at the home pose, the record of `size` in slot 0 and the demonstration load around it."""
    m = Machine(RADII[size], load=DEMO_LOAD)
    s, vis = dict(K.HOME), {"held": False, "slot": True, "platter": False, "ring": False}
    return {**m.environment(s, vis), **m.moving(s, vis), **m.display(s)}


# ---------------------------------------------------------------- placing rest-frame parts, as the viewer does
def _rot_z(v, deg):
    c, s = cos(radians(deg)), sin(radians(deg))
    return v @ np.array([[c, s, 0], [-s, c, 0], [0, 0, 1]])


def _rot_x(v, deg):
    c, s = cos(radians(deg)), sin(radians(deg))
    return v @ np.array([[1, 0, 0], [0, c, s], [0, -s, c]])


def place(group, v, s, scn):
    """Transform rest-frame vertices of a part in `group` for state s, exactly as cad-model.html does."""
    if group == "static":
        return v
    if group == "carousel":
        cx, cy = scn["carousel"]["centre"]
        c = np.array([cx, cy, 0.0])
        return _rot_z(v - c, s["c"]) + c
    if group == "tonearm":
        pv = np.array(scn["tonearm"]["pivot"])
        return _rot_z(v - pv, s["a"]) + pv + np.array([0, 0, s["l"] * scn["tonearm"]["lift"]])
    if group == "x":
        return v + np.array([s["x"], 0, 0])
    if group == "y":
        return v + np.array([s["x"], s["y"], 0])
    if group == "z":
        return v + np.array([s["x"], s["y"], s["z"]])
    if group == "wrist":
        return _rot_x(v, s["phi"]) + np.array([s["x"] + scn["wrist"]["offsetX"], s["y"], s["z"]])
    raise KeyError(group)


def visible(name, vis, size, scn):
    for flag, entry in scn["visibility"].items():
        for sz, node in entry.items():
            if node == name:
                return bool(vis[flag]) and sz == size
    return True


# ---------------------------------------------------------------- the viewer's timeline
def timeline(cycle):
    """Segments (pose index, keyframe a, keyframe b, duration) with the web viewer's timing."""
    segs = []
    for pi, pose in enumerate(cycle):
        ks = pose["keyframes"]
        for a, b in zip(ks[:-1], ks[1:], strict=True):
            d = (np.hypot(b["x"] - a["x"], np.hypot(b["y"] - a["y"], b["z"] - a["z"]))
                 + abs(b["phi"] - a["phi"]) * 3 + abs(b["c"] - a["c"]) * 3 + abs(b["a"] - a["a"]) * 3)
            segs.append((pi, a, b, max(0.25, d / 420)))
        if len(ks) == 1:
            segs.append((pi, ks[0], ks[0], 0.5))
    return segs


def state_at(segs, time):
    acc = 0.0
    for pi, a, b, dur in segs:
        if time < acc + dur:
            return pi, K.interpolate(a, b, (time - acc) / dur)
        acc += dur
    pi, a, b, dur = segs[-1]
    return pi, K.interpolate(a, b, 1.0)


# ---------------------------------------------------------------- rasterising
class Projection:
    """Orthographic camera fitted once to a set of vertices, so every frame of an animation shares it."""

    def __init__(self, az, el, allv, width, height, margin=0.04):
        self.right, self.up, self.view = camera(az, el)
        self.width, self.height = width, height
        u, w = allv @ self.right, allv @ self.up
        su = (width * (1 - 2 * margin)) / (u.max() - u.min())
        sw = (height * (1 - 2 * margin)) / (w.max() - w.min())
        self.scale = min(su, sw)
        self.cu, self.cw = (u.max() + u.min()) / 2, (w.max() + w.min()) / 2
        light = np.array([0.35, -0.5, 0.8])
        self.light = light / np.linalg.norm(light)

    def render(self, meshes):
        width, height = self.width, self.height
        img = np.empty((height, width, 3), dtype=np.float64)
        img[:] = BACKGROUND
        zbuf = np.full((height, width), -np.inf)
        for v, f, color in meshes:
            px = (v @ self.right - self.cu) * self.scale + width / 2
            py = height / 2 - (v @ self.up - self.cw) * self.scale
            pz = v @ self.view
            a, b, c = v[f[:, 0]], v[f[:, 1]], v[f[:, 2]]
            n = np.cross(b - a, c - a)
            ln = np.linalg.norm(n, axis=1)
            keep = ln > 1e-9
            n = n[keep] / ln[keep][:, None]
            tri = f[keep]
            shade = 0.42 + 0.58 * np.abs(n @ self.light)
            for (i0, i1, i2), sh in zip(tri, shade, strict=True):
                x0, x1, x2 = px[i0], px[i1], px[i2]
                y0, y1, y2 = py[i0], py[i1], py[i2]
                xmin, xmax = int(max(0, np.floor(min(x0, x1, x2)))), int(min(width - 1, np.ceil(max(x0, x1, x2))))
                ymin, ymax = int(max(0, np.floor(min(y0, y1, y2)))), int(min(height - 1, np.ceil(max(y0, y1, y2))))
                if xmin > xmax or ymin > ymax:
                    continue
                det = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
                if abs(det) < 1e-9:
                    continue
                gx, gy = np.meshgrid(np.arange(xmin, xmax + 1) + 0.5, np.arange(ymin, ymax + 1) + 0.5)
                w1 = ((gx - x0) * (y2 - y0) - (x2 - x0) * (gy - y0)) / det
                w2 = ((x1 - x0) * (gy - y0) - (gx - x0) * (y1 - y0)) / det
                w0 = 1 - w1 - w2
                inside = (w0 >= -1e-6) & (w1 >= -1e-6) & (w2 >= -1e-6)
                if not inside.any():
                    continue
                depth = w0 * pz[i0] + w1 * pz[i1] + w2 * pz[i2]
                zs = zbuf[ymin:ymax + 1, xmin:xmax + 1]
                win = inside & (depth > zs)
                zs[win] = depth[win]
                img[ymin:ymax + 1, xmin:xmax + 1][win] = color * sh
        return img


def to_bytes(img):
    return (np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8)


def _chunk(kind, body):
    c = kind + body
    return struct.pack(">I", len(body)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)


def _scanlines(data):
    return zlib.compress(b"".join(b"\x00" + row.tobytes() for row in data), 9)


def write_png(path, img):
    data = to_bytes(img)
    h, w, _ = data.shape
    png = b"\x89PNG\r\n\x1a\n" + _chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
    png += _chunk(b"IDAT", _scanlines(data)) + _chunk(b"IEND", b"")
    Path(path).write_bytes(png)


def write_apng(path, frames, delay):
    """Animated PNG: every frame full size, `delay` seconds each, looping forever."""
    h, w, _ = frames[0].shape
    num, den = int(round(delay * 1000)), 1000
    png = b"\x89PNG\r\n\x1a\n" + _chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
    png += _chunk(b"acTL", struct.pack(">II", len(frames), 0))
    seq = 0
    for i, frame in enumerate(frames):
        png += _chunk(b"fcTL", struct.pack(">IIIIIHHBB", seq, w, h, 0, 0, num, den, 0, 0))
        seq += 1
        data = _scanlines(frame)
        if i == 0:
            png += _chunk(b"IDAT", data)
        else:
            png += _chunk(b"fdAT", struct.pack(">I", seq) + data)
            seq += 1
    png += _chunk(b"IEND", b"")
    Path(path).write_bytes(png)


# ---------------------------------------------------------------- drivers
def stills(names, width, height):
    parts = still_parts()
    meshes = [mesh(solid, name) for name, solid in parts.items()]
    allv = np.vstack([v for v, _, _ in meshes])
    for name in names:
        az, el = VIEWS[name]
        img = Projection(az, el, allv, width, height).render(meshes)
        out = OUT / f"render-{name}.png"
        write_png(out, img)
        print("wrote", out, f"{out.stat().st_size // 1024} kB")


def animation(size, n_frames, width, height):
    m = Machine(RADII[size], load=DEMO_LOAD)
    scn = scene(m)
    group_of = {name: g for g, names in scn["groups"].items() for name in names}
    rest = {name: mesh(solid, name, 1.5, 0.6) for name, solid in rest_parts(m).items() if name in group_of}
    cycle = [{"keyframes": ks, "before": p["before"]} for p, ks in K.full_cycle(RADII[size])]
    segs = timeline(cycle)
    total = sum(d for _, _, _, d in segs)
    times = [total * i / n_frames for i in range(n_frames)]

    def frame_meshes(time):
        pi, s = state_at(segs, time)
        vis = cycle[pi]["before"]
        return [(place(group_of[name], v, s, scn), f, col)
                for name, (v, f, col) in rest.items() if visible(name, vis, size, scn)]

    allv = np.vstack([v for tm in times[:: max(1, n_frames // 12)] for v, _, _ in frame_meshes(tm)])
    proj = Projection(*ANIMATION_VIEW, allv, width, height)
    frames = []
    for i, tm in enumerate(times):
        frames.append(to_bytes(proj.render(frame_meshes(tm))))
        print(f'{size}" frame {i + 1}/{n_frames}', flush=True)
    out = OUT / f"cycle-{size}.png"
    write_apng(out, frames, total / n_frames)
    print("wrote", out, f"{out.stat().st_size // 1024} kB, {n_frames} frames, {total:.0f} s of cycle")


def main():
    ap = argparse.ArgumentParser(description="render views of the machine from the CAD")
    ap.add_argument("views", nargs="*", help="still views to render (default: all); with --animate, record sizes")
    ap.add_argument("--animate", action="store_true", help="render the cycle as an animated PNG per record size")
    ap.add_argument("--frames", type=int, default=72)
    ap.add_argument("--width", type=int, default=None)
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.animate:
        width = args.width or 640
        for size in args.views or list(RADII):
            animation(size, args.frames, width, width * 5 // 8)
    else:
        width = args.width or WIDTH
        stills(args.views or list(VIEWS), width, width * HEIGHT // WIDTH)


if __name__ == "__main__":
    main()
