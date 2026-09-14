"""Carousel magazine: fixed base with roller ring and centre bearing, rotating plywood disc
with printed hub, combs and GT2 tooth ring, and the records standing as spokes.

Every comb has a V-shaped slot floor with its apex at CAR_REC_R, so a record of any diameter
rolls to the same centre radius; only its centre height depends on its size."""
from math import cos, degrees, pi, sin, tan

import cadquery as cq

from .. import params as P
from .common import box, cyl_y, cyl_z, ring_z, rot_z, union_all

RADII = {"12": P.RECORD_12_R, "10": P.RECORD_10_R, "7": P.RECORD_7_R}


def record_z(r=P.RECORD_12_R):
    """Centre height of a record of radius r standing in the V of a comb slot."""
    return P.CAR_SLOT_Z + r / cos(P.CAR_V_SLOPE)


def base():
    """Everything that does not rotate: base plate, stub shaft, roller brackets, index stepper."""
    cx, cy = P.CAR_CX, P.CAR_CY
    plate = cyl_z(P.CAR_BASE_R, P.CAR_BASE_T, cx, cy, 0)
    shaft = cyl_z(P.CAR_SHAFT_R, 50, cx, cy, P.CAR_BASE_T)
    parts = [plate, shaft]
    for i in range(P.CAR_ROLLER_N):
        a = 2 * pi * i / P.CAR_ROLLER_N
        rx, ry = cx + P.CAR_ROLLER_R * cos(a), cy + P.CAR_ROLLER_R * sin(a)
        bracket = box(32, 36, 36, 0, 0, P.CAR_BASE_T + 18)
        bearing = cyl_y(11, 7, 0, -3.5, P.CAR_BASE_T + 38)   # 608 bearing, axis radial after rotation
        parts.append(rot_z(bracket.union(bearing), degrees(a)).translate((rx, ry, 0)))
    stepper = box(42, 42, 40, cx - 245, cy + 90, P.CAR_BASE_T + 20)
    parts.append(stepper)
    return union_all(parts)


def _v_floor(z_apex):
    """The V floor as (x, z) points in the comb's own frame: x radial from the comb's centre, z from its underside."""
    s = tan(P.CAR_V_SLOPE)
    x0, x1 = -P.CAR_COMB_L / 2, P.CAR_COMB_L / 2
    xa = P.CAR_REC_R - P.CAR_COMB_R
    return [(x0, z_apex + (xa - x0) * s), (xa, z_apex), (x1, z_apex + (x1 - xa) * s)]


def _extrude_xz(points, width):
    """A prism from a closed (x, z) polygon, `width` wide along Y and centred on y = 0."""
    return cq.Workplane("XZ").polyline(points).close().extrude(width / 2, both=True)


def comb_end_height():
    """Height of the comb at its inner end, where it plugs into the hub."""
    return _v_floor(P.CAR_COMB_H)[0][1]


def comb():
    """One slot comb, printed: a bar whose top follows a shallow V, with a 5 mm slot in it that locates
    the record's edge; the record rolls to the apex, so every size is centred at CAR_REC_R. The inner
    end plugs into the hub. Origin at the comb's centre, on its underside."""
    x0, x1 = -P.CAR_COMB_L / 2, P.CAR_COMB_L / 2
    top = _v_floor(P.CAR_COMB_H)
    body = _extrude_xz([(x0, 0), (x1, 0)] + top[::-1], P.CAR_COMB_T)
    floor = _v_floor(P.CAR_COMB_H - P.CAR_SLOT_D)
    slot = _extrude_xz(floor + [(x1, 200), (x0, 200)], P.CAR_SLOT_W)
    return body.cut(slot)


def disc():
    """Rotating floor with tooth ring, hub and combs (all printed parts bolted to the plywood)."""
    cx, cy = P.CAR_CX, P.CAR_CY
    floor = cyl_z(P.CAR_DISC_R, P.CAR_DISC_T, cx, cy, P.CAR_DISC_Z)
    tooth = ring_z(P.CAR_TOOTH_R, P.CAR_TOOTH_R - 12, P.CAR_TOOTH_T, cx, cy, P.CAR_DISC_Z - P.CAR_TOOTH_T)
    top = P.CAR_DISC_Z + P.CAR_DISC_T
    hub = cyl_z(P.CAR_HUB_R, P.CAR_HUB_H, cx, cy, top)
    parts = [floor, tooth, hub]
    one = comb().translate((P.CAR_COMB_R, 0, top))
    for k in range(P.CAR_SLOTS):
        a = (k + 0.5) * P.CAR_PITCH
        parts.append(rot_z(one, degrees(a)).translate((cx, cy, 0)))
    return union_all(parts)


def hub():
    """Printed centre hub with 24 sockets for the comb inner ends and a bore for the stub shaft."""
    body = cyl_z(P.CAR_HUB_R, P.CAR_HUB_H, 0, 0, 0)
    body = body.cut(cyl_z(P.CAR_SHAFT_R + 0.2, 60, 0, 0, -1))
    h = comb_end_height() + 0.4
    for k in range(P.CAR_SLOTS):
        a = degrees((k + 0.5) * P.CAR_PITCH)
        socket = box(40, P.CAR_COMB_T + 0.4, h, P.CAR_HUB_R - 15, 0, h / 2)
        body = body.cut(rot_z(socket, a))
    return body


def roller_bracket():
    """Printed bracket holding one 608 bearing as a roller under the disc."""
    b = box(32, 36, 36, 0, 0, 18)
    axle_hole = cyl_y(4.1, 40, 0, -20, 38)
    bearing_pocket = box(24, 9, 40, 0, 0, 40)
    return b.cut(axle_hole).cut(bearing_pocket)


def record_in_slot(k, r=P.RECORD_12_R):
    """A record of radius r standing in slot k (slot 0 points along +X). Its plane contains the radial direction."""
    cx, cy = P.CAR_CX, P.CAR_CY
    a = k * P.CAR_PITCH
    rec = cyl_y(r, P.RECORD_T, 0, -P.RECORD_T / 2, 0).cut(cyl_y(P.HOLE_R, P.RECORD_T + 2, 0, -P.RECORD_T / 2 - 1, 0))   # plane normal along Y before rotation
    rec = rec.translate((P.CAR_REC_R, 0, record_z(r)))
    return rot_z(rec, degrees(a)).translate((cx, cy, 0))


def pick_record_centre(r=P.RECORD_12_R):
    """Centre of the record in slot 0: the same radius for every size, a height that follows the size."""
    return (P.CAR_CX + P.CAR_REC_R, P.CAR_CY, record_z(r))
