"""Omnitronic DD 3120 envelope: plinth, platter, spindle, tonearm, cue lever."""
from math import radians, cos, sin
import cadquery as cq
from .common import box, cyl_z, cyl_x, union_all, rot_z
from .. import params as P


def plinth():
    body = box(P.DECK_W, P.DECK_D, P.DECK_H, P.DECK_CX, P.DECK_CY, P.DECK_H / 2)
    platter = cyl_z(P.PLATTER_R, P.PLATTER_T, P.DECK_SPINDLE_X, P.DECK_SPINDLE_Y, P.DECK_H)
    mat = cyl_z(P.PLATTER_R - 13, P.MAT_T, P.DECK_SPINDLE_X, P.DECK_SPINDLE_Y, P.DECK_H + P.PLATTER_T)
    spindle = cyl_z(P.SPINDLE_R, P.SPINDLE_H, P.DECK_SPINDLE_X, P.DECK_SPINDLE_Y, P.DECK_H + P.PLATTER_T)
    base = cyl_z(32, 40, P.ARM_PIVOT[0], P.ARM_PIVOT[1], P.DECK_H)             # arm base
    rest = box(24, 12, 6, P.ARM_REST_XY[0], P.ARM_REST_XY[1], 124).union(
        cyl_z(9, 35, P.ARM_REST_XY[0], P.ARM_REST_XY[1], P.DECK_H))              # arm rest post + clip
    fader = box(16, 100, 4, P.DECK_SPINDLE_X + 230, P.DECK_SPINDLE_Y + 64, P.DECK_H + 2)
    startstop = box(45, 30, 8, P.DECK_SPINDLE_X - 145, P.DECK_SPINDLE_Y + 153, P.DECK_H + 4)
    lever = box(34, 8, 5, P.CUE_LEVER[0] + 12, P.CUE_LEVER[1], P.CUE_LEVER[2])     # cue lever, resting position
    return union_all([body, platter, mat, spindle, base, rest, fader, startstop, lever])


def platter_top_z():
    return P.DECK_H + P.PLATTER_T + P.MAT_T


def tonearm(angle_deg, lift=0.0):
    """Tonearm as a rigid body: pivot at ARM_PIVOT, stylus at ARM_EFF_L along the azimuth angle_deg.

    Built along +X then rotated about Z. lift raises the whole arm (cue lever up).
    """
    px, py, pz = P.ARM_PIVOT
    tube = cyl_x(5.5, P.ARM_EFF_L - 20, 0, 0, 0)                                 # straight stand-in for the S tube
    headshell = box(36, 17, 16, P.ARM_EFF_L - 16, 0, -7)
    fl = P.FINGER_LIFT_LOCAL
    finger = box(3.5, 28, 3.5, fl[0], fl[1] - 12, fl[2])                          # finger lift, sticking outwards (+Y local)
    stylus = box(3, 3, 12, P.ARM_EFF_L - 6, 4, -14)
    counterweight = cyl_x(18, 32, -61, 0, 0)
    bearing = cyl_z(16, 14, 0, 0, -7)
    arm = union_all([tube, headshell, finger, stylus, counterweight, bearing])
    arm = rot_z(arm, angle_deg).translate((px, py, pz + lift * P.ARM_LIFT))
    return arm


def finger_lift_point(angle_deg, lift=0.0):
    """World position of the finger lift's centre for a given arm angle."""
    px, py, pz = P.ARM_PIVOT
    a = radians(angle_deg)
    lx, ly, lz = P.FINGER_LIFT_LOCAL
    return (px + lx * cos(a) - ly * sin(a), py + lx * sin(a) + ly * cos(a), pz + lz + lift * P.ARM_LIFT)


def stylus_point(angle_deg):
    px, py, _ = P.ARM_PIVOT
    a = radians(angle_deg)
    return (px + P.ARM_EFF_L * cos(a), py + P.ARM_EFF_L * sin(a))


def record_on_platter(r=P.RECORD_12_R):
    z = platter_top_z()
    return cyl_z(r, P.RECORD_T, P.DECK_SPINDLE_X, P.DECK_SPINDLE_Y, z).cut(cyl_z(P.HOLE_R, P.RECORD_T + 2, P.DECK_SPINDLE_X, P.DECK_SPINDLE_Y, z - 1))
