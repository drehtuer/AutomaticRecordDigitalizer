"""Cue-lever servo bracket on the end panel, pusher rod, inner end stop, deck camera, LED bar."""
from math import radians, cos, sin
from .common import box, cyl_z, cyl_x, cyl_y, union_all
from .. import params as P


def cue_servo_assembly():
    x_panel = P.FRAME_X1 - P.PLY
    y, z = P.CUE_SERVO_Y, P.CUE_SERVO_Z
    bracket = box(25, 30, 100, x_panel - 12.5, y, 70)
    servo = cyl_x(20, 35, x_panel - 60, y, z)
    rod_len = x_panel - 25 - (P.CUE_LEVER[0] + 30)
    rod = cyl_x(6, rod_len, P.CUE_LEVER[0] + 30, y, z)
    guide = box(20, 14, 14, x_panel - 100, y, z)
    pad = box(8, 16, 16, P.CUE_LEVER[0] + 34, y, z)
    # end-stop bar in front of the arm base, under the arm, with the pin at END_STOP
    px, py, _ = P.ARM_PIVOT
    ex = px + P.END_STOP_R * cos(radians(P.END_STOP_ANGLE))
    ey = py + P.END_STOP_R * sin(radians(P.END_STOP_ANGLE))
    bar_y = -20.0
    bar = box(x_panel - ex, 8, 10, (x_panel + ex) / 2, bar_y, 98)
    stub = box(10, abs(ey - bar_y) + 8, 8, ex, (ey + bar_y) / 2, 98)
    pin = cyl_z(5, 50, ex, ey, 100).union(cyl_z(9, 22, ex, ey, 128))
    return union_all([bracket, servo, rod, guide, pad, bar, stub, pin])


def end_stop_point():
    px, py, _ = P.ARM_PIVOT
    return (px + P.END_STOP_R * cos(radians(P.END_STOP_ANGLE)), py + P.END_STOP_R * sin(radians(P.END_STOP_ANGLE)))


def deck_camera_and_led():
    x, y, z = P.DECK_CAM
    post = box(24, 24, 120, x, y, 60)
    cam = box(40, 30, 30, x - 20, y, z)
    led = box(16, 70, 16, x - 10, y + 45, z - 38)
    return union_all([post, cam, led])
