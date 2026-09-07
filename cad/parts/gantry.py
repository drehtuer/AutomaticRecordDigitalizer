"""Gantry parts, each built in the local frame of the kinematic group it belongs to.

x_carriage(): local origin at (carX, 0, 0)          - moves in X
y_carriage(): local origin at (carX, carY, 0)       - moves in X, Y
z_carriage(): local origin at (carX, carY, carZ)    - moves in X, Y, Z
wrist():      local origin at the wrist pivot,      - rotates about the X axis
              arm along -Z, cup facing -Y at wrist angle 0
"""
from .. import params as P
from .common import box, cyl_x, cyl_y, cyl_z, union_all


def x_carriage():
    px, py, pz = P.XCAR_PLATE
    plates = [box(px, py, pz, 0, y, P.BEAM_Z + 20 + pz / 2) for y in (-P.FRAME_Y, P.FRAME_Y)]
    cross = box(20, P.CROSS_BEAM_L, 40, 0, 0, P.CROSS_BEAM_Z)
    motor = box(42, 42, 42, 0, P.FRAME_Y + 20, P.CROSS_BEAM_Z + 45)   # X motor on one end
    return union_all(plates + [cross, motor])


def y_carriage():
    gx, gy, gz = P.GUIDE_BLOCK
    guide = box(gx, gy, gz, 0, 0, P.CROSS_BEAM_Z)
    zmotor = cyl_z(21, 45, 0, 65, P.CROSS_BEAM_Z + gz / 2)
    return guide.union(zmotor)


def z_carriage():
    bx, by, bz = P.ZCAR_BLOCK
    block = box(bx, by, bz, 0, 0, 0)
    column = box(P.COLUMN_W, P.COLUMN_W, P.COLUMN_L, 0, 0, P.COLUMN_L / 2)
    screw = cyl_z(5, P.COLUMN_L, 0, 32, 0)
    outrigger = box(P.WRIST_X - 10, 35, 35, (P.WRIST_X - 10) / 2, 0, 0)
    motor = cyl_x(22, 40, P.WRIST_X + 13, 0, 0)
    return union_all([block, column, screw, outrigger, motor])


def wrist():
    """Hub, arm, cup, camera and fork. Cup faces -Y; fork points +Z (opposite the arm)."""
    L = P.ARM_L
    hub = cyl_x(26, 26, -13, 0, 0)
    arm = box(P.ARM_W, P.ARM_W, L, 0, 0, -L / 2)
    end = box(30, 30, 30, 0, 0, -L + 3)             # cup bracket, kept above the arm end so it clears the spindle tip
    neck = cyl_y(14, 12, 0, -22, -L)               # Y -22 .. -10
    # bellows cup as a hollow: the spindle tip enters it when the record is released over the spindle
    cup = cyl_y(P.CUP_R, P.CUP_H, 0, -(P.CUP_OFF + P.CUP_H / 2), -L).cut(
        cyl_y(P.CUP_R - 5, P.CUP_H - 3, 0, -(P.CUP_OFF + P.CUP_H / 2), -L))   # Y -36 .. -20, open towards -Y
    cam_bracket = box(30, 12, 10, 26, 0, -L + 80)
    cam = box(22, 24, 22, P.CAM_OFF[0], 0, -L + P.CAM_OFF[2])
    rod = box(12, 12, P.FORK_L - 12, 0, 0, (P.FORK_L + 12) / 2)
    crossbar = box(12, P.FORK_PRONG_GAP + 6, 6, 0, 0, P.FORK_L)
    prongs = [box(12, 6, 16, 0, s * (P.FORK_PRONG_GAP / 2 + 3), P.FORK_L + 5) for s in (-1, 1)]
    return union_all([hub, arm, end, neck, cup, cam_bracket, cam] + [rod, crossbar] + prongs)


def fork():
    """Printed finger-lift fork alone: rod plus U, TPU lining in the U to be added."""
    rod = box(12, 12, P.FORK_L - 12, 0, 0, (P.FORK_L + 12) / 2)
    crossbar = box(12, P.FORK_PRONG_GAP + 6, 6, 0, 0, P.FORK_L)
    prongs = [box(12, 6, 16, 0, s * (P.FORK_PRONG_GAP / 2 + 3), P.FORK_L + 5) for s in (-1, 1)]
    return union_all([rod, crossbar] + prongs)


def held_record(r=P.RECORD_12_R):
    """A record on the cup, in the wrist's local frame."""
    y0 = -(P.HELD_OFF + P.RECORD_T / 2)
    return cyl_y(r, P.RECORD_T, 0, y0, -P.ARM_L).cut(cyl_y(P.HOLE_R, P.RECORD_T + 2, 0, y0 - 1, -P.ARM_L))


def fork_tip_local():
    return (0.0, 0.0, P.FORK_L)
