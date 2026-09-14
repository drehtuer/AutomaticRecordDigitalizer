"""Sweep the whole cycle and report every intersection between the moving parts and the rest.

    python -m cad.check_collisions            # full cycle with a 12", then pick, place and return with a 10" and a 7"
    python -m cad.check_collisions --step 10  # finer
    python -m cad.check_collisions --size 7   # the whole cycle with a 7"
    python -m cad.check_collisions --size 7 --neighbour 12 --poses pick   # the case the loading rule forbids

Only the pick and the return depend on the record's size (every size stands at the same radius in
its slot and is picked at its own centre height), so the smaller sizes are swept through those
poses and the carry away from the slot. The neighbour that matters is the spoke on the front (+Y)
side of the pick, the one the wrist descends beside: a 12" and a 10" are swept with a 12" there,
a 7" with a 10", the largest the loading rule allows next to a 7" (with a 12" there the column's
foot and the wrist hub reach below the neighbour's edge, which is why the rule exists).
Exit code 1 if any collision above the tolerance is found.
"""
import argparse
import math
import sys
import time

from . import kinematics as K
from .assembly import Machine
from .parts.carousel import RADII

SIZE_DEPENDENT = ("pick", "place", "return")     # the poses whose path differs with the record's size
NEIGHBOUR = {"12": "12", "10": "12", "7": "10"}   # the largest record the loading rule allows on the front side of each size


def bbox_overlap(a, b, margin=0.0):
    return not (a.xmax + margin < b.xmin or b.xmax + margin < a.xmin or
                a.ymax + margin < b.ymin or b.ymax + margin < a.ymin or
                a.zmax + margin < b.zmin or b.zmax + margin < a.zmin)


def samples(k0, k1, step_mm, step_deg):
    d = max(abs(k1["x"] - k0["x"]), abs(k1["y"] - k0["y"]), abs(k1["z"] - k0["z"]))
    da = max(abs(k1["phi"] - k0["phi"]), abs(k1["a"] - k0["a"]), abs(k1["c"] - k0["c"]))
    n = max(1, int(math.ceil(max(d / step_mm, da / step_deg))))
    return [(i / n, K.interpolate(k0, k1, i / n)) for i in range(n + 1)]


CHECK_MOVING = ("z_carriage", "wrist", "record_held")     # x/y carriages ride on the beams by design
SKIP_PAIRS = {("wrist", "tonearm")}                        # the fork straddles the finger lift: checked separately with a margin


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", type=float, default=20.0, help="sampling step in mm")
    ap.add_argument("--deg", type=float, default=5.0, help="sampling step in degrees")
    ap.add_argument("--tol", type=float, default=1.0, help="intersection volume tolerance in mm^3")
    ap.add_argument("--poses", nargs="*", help="pose ids to check (default: all)")
    ap.add_argument("--size", choices=sorted(RADII), help="one record size only, through every pose (default: all sizes)")
    ap.add_argument("--neighbour", choices=sorted(RADII) + ["none"],
                    help="what stands in the slot on the front side of the pick (default: the largest the loading rule allows)")
    args = ap.parse_args()

    if args.size:
        runs = [(args.size, args.poses)]
    else:
        runs = [("12", args.poses)] + [(sz, [p for p in SIZE_DEPENDENT if not args.poses or p in args.poses])
                                       for sz in ("10", "7")]
    t0 = time.time()
    findings, n_samples = [], 0
    for size, pose_ids in runs:
        if not pose_ids and pose_ids is not None:
            continue
        nb = args.neighbour or NEIGHBOUR[size]
        m = Machine(RADII[size], None if nb == "none" else RADII[nb])
        print(f'--- {size}" record, {"nothing" if nb == "none" else nb + chr(34)} in the slot on its front side ---')
        n_samples += sweep(m, K.full_cycle(RADII[size]), pose_ids, args, findings, t0, size)
    print(f"\n{n_samples} samples, {len(findings)} collisions above {args.tol} mm^3")
    sys.exit(1 if findings else 0)


def sweep(m, cycle, pose_ids, args, findings, t0, size):
    n_samples = 0
    for pose, keys in cycle:
        if pose_ids and pose["id"] not in pose_ids:
            continue
        # visibility switches at the start (before) and end (after) of a pose
        vis_before, vis_after = pose["before"], pose.get("after") or pose["before"]
        for si in range(len(keys) - 1):
            for t, s in samples(keys[si], keys[si + 1], args.step, args.deg):
                vis = vis_after if (si == len(keys) - 2 and t >= 1.0) else vis_before
                env = m.environment(s, vis)
                env_bb = {n: e.val().BoundingBox() for n, e in env.items()}
                mov = m.moving(s, vis)
                n_samples += 1
                for mn in CHECK_MOVING:
                    if mn not in mov:
                        continue
                    mb = mov[mn].val().BoundingBox()
                    for en, e in env.items():
                        if (mn, en) in SKIP_PAIRS or not bbox_overlap(mb, env_bb[en]):
                            continue
                        try:
                            vol = mov[mn].intersect(e).val().Volume()
                        except Exception:
                            vol = 0.0
                        if vol > args.tol:
                            findings.append((size, pose["id"], si, round(t, 2), mn, en, round(vol)))
                            print(f"COLLISION {size:>2s}\" {pose['id']:8s} seg {si} t={t:.2f}  {mn} x {en}: {vol:.0f} mm^3   "
                                  f"at x={s['x']:.0f} y={s['y']:.0f} z={s['z']:.0f} phi={s['phi']:.0f}")
        print(f"checked {pose['id']:8s} ({len(keys) - 1} segments)   elapsed {time.time() - t0:.0f}s")
    return n_samples


if __name__ == "__main__":
    main()
