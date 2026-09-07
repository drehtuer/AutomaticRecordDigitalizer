"""Plywood box frame with V-slot beams, flip station and electronics box."""
from math import degrees

from .. import params as P
from .common import box, cyl_z, torus_z, union_all


def side_panel(y):
    L = P.FRAME_X1 - P.FRAME_X0
    cx = (P.FRAME_X0 + P.FRAME_X1) / 2
    strips = [
        box(L, P.PLY, P.PANEL_BOTTOM_STRIP, cx, y, P.PANEL_BOTTOM_STRIP / 2),
        box(L, P.PLY, P.PANEL_TOP_STRIP, cx, y, P.FRAME_H - P.PANEL_TOP_STRIP / 2),
    ]
    for x in (P.FRAME_X0 + P.PANEL_POST_W / 2, P.PANEL_MID_POST_X, P.FRAME_X1 - P.PANEL_POST_W / 2):
        strips.append(box(P.PANEL_POST_W, P.PLY, P.FRAME_H, x, y, P.FRAME_H / 2))
    return union_all(strips)


def end_panel():
    x = P.FRAME_X1 - P.PLY / 2
    W = 2 * P.FRAME_Y
    parts = [
        box(P.PLY, W, P.PANEL_BOTTOM_STRIP, x, 0, P.PANEL_BOTTOM_STRIP / 2),
        box(P.PLY, W, P.PANEL_TOP_STRIP, x, 0, P.FRAME_H - P.PANEL_TOP_STRIP / 2),
        box(P.PLY, P.PANEL_POST_W, P.FRAME_H, x, -P.FRAME_Y + 60, P.FRAME_H / 2),
        box(P.PLY, P.PANEL_POST_W, P.FRAME_H, x, P.FRAME_Y - 60, P.FRAME_H / 2),
    ]
    return union_all(parts)


def beams():
    L = P.BEAM_X1 - P.BEAM_X0
    cx = (P.BEAM_X0 + P.BEAM_X1) / 2
    parts = [box(L, 20, 40, cx, y, P.BEAM_Z) for y in (-P.FRAME_Y, P.FRAME_Y)]
    parts.append(box(20, 2 * P.FRAME_Y + 20, 20, P.TIE_X, 0, P.BEAM_Z))
    return union_all(parts)


def frame():
    return union_all([side_panel(-P.FRAME_Y), side_panel(P.FRAME_Y), end_panel(), beams()])


def station():
    """Ring rest on its post, with the opening towards +Y, standing on the electronics box."""
    ring = torus_z(P.ST_RING_R, P.ST_RING_TUBE, 0, 0, 0, arc_deg=360 - degrees(P.ST_GAP))
    # revolve starts at +X; rotate so the gap is centred on +Y
    ring = ring.rotate((0, 0, 0), (0, 0, 1), 90 + degrees(P.ST_GAP) / 2).translate((P.ST_X, P.ST_Y, P.ST_Z))
    post = cyl_z(12, P.ST_Z - P.ST_BOX[2], P.ST_X, P.ST_POST_Y, P.ST_BOX[2])
    arm = box(22, P.ST_Y - P.ST_POST_Y - P.ST_RING_R + 12, 22, P.ST_X, (P.ST_POST_Y + P.ST_Y - P.ST_RING_R + 8) / 2, P.ST_ARM_Z)
    riser = box(22, 16, P.ST_Z - P.ST_ARM_Z, P.ST_X, P.ST_Y - P.ST_RING_R, (P.ST_Z + P.ST_ARM_Z) / 2)
    ebox = box(*P.ST_BOX, P.ST_X, P.ST_BOX_Y, P.ST_BOX[2] / 2)
    return union_all([ring, post, arm, riser, ebox])


def ring_rest():
    """Printed ring rest alone, at the origin, opening towards +Y, with a TPU pad groove on top."""
    ring = torus_z(P.ST_RING_R, P.ST_RING_TUBE, 0, 0, 0, arc_deg=360 - degrees(P.ST_GAP))
    ring = ring.rotate((0, 0, 0), (0, 0, 1), 90 + degrees(P.ST_GAP) / 2)
    groove = torus_z(P.ST_RING_R, 2.0, 0, 0, P.ST_RING_TUBE - 1.0)
    return ring.cut(groove)


def record_on_ring(r=P.RECORD_12_R):
    z = P.ST_Z + P.ST_RING_TUBE
    return cyl_z(r, P.RECORD_T, P.ST_X, P.ST_Y, z).cut(cyl_z(P.HOLE_R, P.RECORD_T + 2, P.ST_X, P.ST_Y, z - 1))


def bench():
    return box(P.BENCH_L, P.BENCH_W, P.BENCH_T, P.BENCH_CX, 0, -P.BENCH_T / 2)
