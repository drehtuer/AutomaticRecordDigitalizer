"""Carousel magazine: fixed base with roller ring and centre bearing, rotating plywood disc
with printed hub, combs, rim segments and GT2 tooth ring, and the records standing as spokes."""
from math import cos, degrees, sin

from .. import params as P
from .common import box, cyl_y, cyl_z, ring_z, rot_z, torus_z, union_all


def base():
    """Everything that does not rotate: base plate, stub shaft, roller brackets, index stepper."""
    cx, cy = P.CAR_CX, P.CAR_CY
    plate = cyl_z(P.CAR_BASE_R, P.CAR_BASE_T, cx, cy, 0)
    shaft = cyl_z(P.CAR_SHAFT_R, 50, cx, cy, P.CAR_BASE_T)
    parts = [plate, shaft]
    for i in range(P.CAR_ROLLER_N):
        a = 2 * 3.141592653589793 * i / P.CAR_ROLLER_N
        rx, ry = cx + P.CAR_ROLLER_R * cos(a), cy + P.CAR_ROLLER_R * sin(a)
        bracket = box(32, 36, 36, 0, 0, P.CAR_BASE_T + 18)
        bearing = cyl_y(11, 7, 0, -3.5, P.CAR_BASE_T + 38)   # 608 bearing, axis radial after rotation
        parts.append(rot_z(bracket.union(bearing), degrees(a)).translate((rx, ry, 0)))
    stepper = box(42, 42, 40, cx - 245, cy + 90, P.CAR_BASE_T + 20)
    parts.append(stepper)
    return union_all(parts)


def disc():
    """Rotating floor with tooth ring, hub, rim and combs (all printed parts bolted to the plywood)."""
    cx, cy = P.CAR_CX, P.CAR_CY
    floor = cyl_z(P.CAR_DISC_R, P.CAR_DISC_T, cx, cy, P.CAR_DISC_Z)
    tooth = ring_z(P.CAR_TOOTH_R, P.CAR_TOOTH_R - 12, P.CAR_TOOTH_T, cx, cy, P.CAR_DISC_Z - P.CAR_TOOTH_T)
    top = P.CAR_DISC_Z + P.CAR_DISC_T
    hub = cyl_z(P.CAR_HUB_R, P.CAR_HUB_H, cx, cy, top)
    rim = torus_z(P.CAR_RIM_R, P.CAR_RIM_TUBE, cx, cy, P.CAR_RIM_Z)
    parts = [floor, tooth, hub, rim]
    for k in range(P.CAR_SLOTS):
        a = (k + 0.5) * P.CAR_PITCH
        comb = box(P.CAR_COMB_L, P.CAR_COMB_T, P.CAR_COMB_H, P.CAR_COMB_R, 0, top + P.CAR_COMB_H / 2)
        parts.append(rot_z(comb, degrees(a)).translate((cx, cy, 0)))
    return union_all(parts)


def comb():
    """One slot comb, printed: a bar with a 5 mm slot on top that locates the record's edge, plus hub and rim tabs."""
    bar = box(P.CAR_COMB_L, P.CAR_COMB_T, P.CAR_COMB_H, 0, 0, P.CAR_COMB_H / 2)
    slot = box(P.CAR_COMB_L, 5.0, 12.0, 0, 0, P.CAR_COMB_H - 6.0)
    return bar.cut(slot)


def hub():
    """Printed centre hub with 24 sockets for the comb inner ends and a bore for the stub shaft."""
    body = cyl_z(P.CAR_HUB_R, P.CAR_HUB_H, 0, 0, 0)
    body = body.cut(cyl_z(P.CAR_SHAFT_R + 0.2, 60, 0, 0, -1))
    for k in range(P.CAR_SLOTS):
        a = degrees((k + 0.5) * P.CAR_PITCH)
        socket = box(40, P.CAR_COMB_T + 0.4, P.CAR_COMB_H + 0.4, P.CAR_HUB_R - 15, 0, P.CAR_COMB_H / 2)
        body = body.cut(rot_z(socket, a))
    return body


def roller_bracket():
    """Printed bracket holding one 608 bearing as a roller under the disc."""
    b = box(32, 36, 36, 0, 0, 18)
    axle_hole = cyl_y(4.1, 40, 0, -20, 38)
    bearing_pocket = box(24, 9, 40, 0, 0, 40)
    return b.cut(axle_hole).cut(bearing_pocket)


def record_in_slot(k, r=P.RECORD_12_R):
    """A record standing in slot k (slot 0 points along +X). Its plane contains the radial direction."""
    cx, cy = P.CAR_CX, P.CAR_CY
    a = k * P.CAR_PITCH
    rec = cyl_y(r, P.RECORD_T, 0, -P.RECORD_T / 2, 0).cut(cyl_y(P.HOLE_R, P.RECORD_T + 2, 0, -P.RECORD_T / 2 - 1, 0))   # plane normal along Y before rotation
    rec = rec.translate((P.CAR_REC_R, 0, P.CAR_REC_Z))
    return rot_z(rec, degrees(a)).translate((cx, cy, 0))


def pick_record_centre():
    return (P.CAR_CX + P.CAR_REC_R, P.CAR_CY, P.CAR_REC_Z)
