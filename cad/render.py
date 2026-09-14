"""Render the machine to PNG images for the documentation, with no renderer but numpy.

    python -m cad.render                 # every view into docs/images/
    python -m cad.render rear deck-end   # named views only

Each view is an orthographic projection of the machine at the home pose, with every record in
its slot, the electronics on the frame, and the chains and cables as the model draws them. The
parts are tessellated, shaded with one light, and rasterised through a depth buffer; the result
is a picture of the model, not a photograph of anything.
"""
import struct
import sys
import zlib
from math import cos, radians, sin
from pathlib import Path

import numpy as np

from . import kinematics as K
from .assembly import Machine, color_of

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


def camera(az, el):
    """Right, up and towards-the-viewer unit vectors for a camera at azimuth az and elevation el."""
    a, e = radians(az), radians(el)
    view = np.array([cos(e) * cos(a), cos(e) * sin(a), sin(e)])     # from the scene towards the camera
    up0 = np.array([0.0, 0.0, 1.0])
    right = np.cross(up0, view)
    right /= np.linalg.norm(right)
    up = np.cross(view, right)
    return right, up, view


def triangles(solid, name):
    verts, faces = solid.val().tessellate(TOLERANCE, ANGULAR)
    v = np.array([(p.x, p.y, p.z) for p in verts], dtype=np.float64)
    f = np.array(faces, dtype=np.int64)
    return v, f, np.array(color_of(name), dtype=np.float64)


def scene_parts():
    m = Machine()
    s, vis = dict(K.HOME), {"held": False, "slot": True, "platter": False, "ring": False}
    return {**m.environment(s, vis), **m.moving(s, vis), **m.display(s)}


def render(parts, az, el, width=WIDTH, height=HEIGHT):
    right, up, view = camera(az, el)
    light = np.array([0.35, -0.5, 0.8])
    light /= np.linalg.norm(light)
    meshes = [triangles(solid, name) for name, solid in parts.items()]
    allv = np.vstack([v for v, _, _ in meshes])
    u = allv @ right
    w = allv @ up
    margin = 0.04
    su = (width * (1 - 2 * margin)) / (u.max() - u.min())
    sw = (height * (1 - 2 * margin)) / (w.max() - w.min())
    scale = min(su, sw)
    cu, cw = (u.max() + u.min()) / 2, (w.max() + w.min()) / 2

    img = np.empty((height, width, 3), dtype=np.float64)
    img[:] = BACKGROUND
    zbuf = np.full((height, width), -np.inf)
    for v, f, color in meshes:
        px = (v @ right - cu) * scale + width / 2
        py = height / 2 - (v @ up - cw) * scale
        pz = v @ view
        tri = f
        a, b, c = v[tri[:, 0]], v[tri[:, 1]], v[tri[:, 2]]
        n = np.cross(b - a, c - a)
        ln = np.linalg.norm(n, axis=1)
        keep = ln > 1e-9
        n = n[keep] / ln[keep][:, None]
        tri = tri[keep]
        shade = 0.42 + 0.58 * np.abs(n @ light)
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
            xs = np.arange(xmin, xmax + 1) + 0.5
            ys = np.arange(ymin, ymax + 1) + 0.5
            gx, gy = np.meshgrid(xs, ys)
            # barycentric weights for vertices 1 and 2, then 0
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


def write_png(path, img):
    data = (np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8)
    h, w, _ = data.shape
    raw = b"".join(b"\x00" + data[y].tobytes() for y in range(h))

    def chunk(kind, body):
        c = kind + body
        return struct.pack(">I", len(body)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    Path(path).write_bytes(png)


def main():
    names = sys.argv[1:] or list(VIEWS)
    OUT.mkdir(parents=True, exist_ok=True)
    parts = scene_parts()
    for name in names:
        az, el = VIEWS[name]
        img = render(parts, az, el)
        out = OUT / f"render-{name}.png"
        write_png(out, img)
        print("wrote", out, f"{out.stat().st_size // 1024} kB")


if __name__ == "__main__":
    main()
