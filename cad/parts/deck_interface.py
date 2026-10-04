"""Cue-lever servo on a beam off the end panel, its horn and yoke, inner end stop, deck camera, LED bar."""
from math import cos, radians, sin

from .. import params as P
from .common import box, cyl_z, union_all


def cue_servo_assembly():
    """MG996R hanging over the cue lever from a beam off the end panel, and the arm's inner end stop.

    The lever's top travels along Y, so the servo's shaft stands vertical beside it and a horn with a
    yoke straddles the top and carries it both ways.
    """
    x_panel = P.FRAME_X1 - P.PLY
    sx, sy, sz = P.CUE_SERVO_X, P.CUE_SERVO_Y, P.CUE_SERVO_Z
    beam_z = sz + 37 + 5                                                          # on top of the 37 mm servo body
    bracket = box(25, 30, beam_z + 5 - 20, x_panel - 12.5, sy, (beam_z + 5 + 20) / 2)   # post on the panel's bottom strip, up to the beam
    servo = box(40, 20, 37, sx + 10, sy, sz + 18.5)                               # body, shaft 10 mm from its lever end
    beam = box(x_panel - (sx - 10), 20, 10, (x_panel + sx - 10) / 2, sy, beam_z)
    horn = box(sx - P.CUE_LEVER_X + 12, 12, 4, (sx + P.CUE_LEVER_X) / 2, sy, sz - 4)
    travel = P.CUE_LEVER_Y_DOWN - P.CUE_LEVER_Y_UP
    yoke = box(12, travel + 12, 8, P.CUE_LEVER_X, sy, sz - 10)                    # everything the yoke sweeps, over the lever's top
    # end-stop bar in front of the lever, under the arm, with the pin at END_STOP
    px, py, _ = P.ARM_PIVOT
    ex = px + P.END_STOP_R * cos(radians(P.END_STOP_ANGLE))
    ey = py + P.END_STOP_R * sin(radians(P.END_STOP_ANGLE))
    bar_y = P.CUE_LEVER_Y_DOWN + 23.0                                             # clear of the lever's travel
    foot = box(25, 20, P.DECK_H + 13 - 20, x_panel - 12.5, bar_y, (P.DECK_H + 13 + 20) / 2)        # narrow: the deck camera post stands next to it
    bar_x0 = P.DECK_SPINDLE_X + P.PLATTER_R + 4.0                                 # the bar and the stub stay outside the platter's rim
    bar = box(x_panel - bar_x0, 8, 10, (x_panel + bar_x0) / 2, bar_y, P.DECK_H + 8)
    stub = box(10, bar_y - ey, 8, bar_x0 + 5, (bar_y + ey) / 2 + 4, P.DECK_H + 8)
    web = box(bar_x0 + 5 - ex, 8, 8, (bar_x0 + 5 + ex) / 2, ey + 4, P.DECK_H + 8)  # from the stub to the pin, between the rim and the arm base
    pin = cyl_z(5, 50, ex, ey, P.DECK_H + 10).union(cyl_z(9, 22, ex, ey, P.DECK_H + 38))
    return union_all([bracket, servo, beam, horn, yoke, foot, bar, stub, web, pin])


def end_stop_point():
    px, py, _ = P.ARM_PIVOT
    return (px + P.END_STOP_R * cos(radians(P.END_STOP_ANGLE)), py + P.END_STOP_R * sin(radians(P.END_STOP_ANGLE)))


def deck_camera_and_led():
    x, y, z = P.DECK_CAM
    post = box(24, 24, 120, x, y, 60)
    cam = box(40, 30, 30, x - 20, y, z)
    led = box(16, 70, 16, x - 10, y + 45, z - 38)
    return union_all([post, cam, led])
