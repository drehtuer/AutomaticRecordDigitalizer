"""Electronics on the frame, the three cable chains, and the cable and hose runs.

Positions follow `docs/08-assembly-instructions.md`: the controller group outside the rear panel
under the X beam, the pump and valve outside the rear panel near the open end, the Pi group
outside the deck-end panel, the Scarlett and the power strip on the bench. Everything here is an
envelope: the boards and boxes have their catalogue sizes, the cables their routed paths.

The chains and the cables that feed them change shape as the gantry moves, so they are drawn at
the home pose and the collision checker does not look at them; the cables that ride rigidly on
the column and the wrist are real moving parts and are checked.
"""
import cadquery as cq

from .. import params as P
from .common import box, cyl_z, union_all

REAR = -P.FRAME_Y - P.PLY / 2            # outer face of the rear panel
END = P.FRAME_X1                          # outer face of the deck-end panel
HOME = {"x": 200.0, "y": 30.0, "z": P.TRAVEL_Z}   # the carriage at rest, as in kinematics.HOME

# chain: 10 x 20 links, R28, drawn as a band
CHAIN_W, CHAIN_T, CHAIN_R = 24.0, 14.0, 28.0
X_CHAIN_Y, X_CHAIN_Z = REAR - 23.0, 800.0             # trough on the rear panel's outer face under the X beam, lower run
X_CHAIN_FIXED = 200.0                                  # mid-travel
Y_CHAIN_DX, Y_CHAIN_Z = -60.0, 860.0                   # beside the cross beam on its -X side
Y_CHAIN_FIXED = -380.0                                 # at the rear X plate
Z_CHAIN_DX, Z_CHAIN_Z0 = -60.0, 950.0                  # standing above the guide block, -X of the column
COLUMN_POST_H = 60.0                                   # post on the column top that carries the chain's moving end


# ---------------------------------------------------------------- helpers
def tube(points, r):
    """A cable or hose of radius r along a polyline: a cylinder per segment, a sphere at every corner."""
    parts = []
    for a, b in zip(points[:-1], points[1:], strict=True):
        pa, pb = cq.Vector(*a), cq.Vector(*b)
        d = pb - pa
        plane = cq.Plane(origin=pa, normal=d.normalized())
        parts.append(cq.Workplane(plane).circle(r).extrude(d.Length))
    for pt in points[1:-1]:
        parts.append(cq.Workplane("XY").sphere(r).translate(pt))
    return union_all(parts)


def _band_xz(x_fixed, x_moving, z_low, y, sign=1):
    """A chain lying in an XZ plane: lower run from x_fixed to the bend, upper run back to x_moving.
    sign=+1 puts the bend on the +X side."""
    L = 512.0                                               # link length without the bend, from the 600 mm chain
    xb = (x_fixed + x_moving + sign * L) / 2
    z_high = z_low + 2 * CHAIN_R
    lower = box(abs(xb - x_fixed), CHAIN_W, CHAIN_T, (xb + x_fixed) / 2, y, z_low)
    upper = box(abs(xb - x_moving), CHAIN_W, CHAIN_T, (xb + x_moving) / 2, y, z_high)
    ring = (cq.Workplane("XZ").circle(CHAIN_R + CHAIN_T / 2).circle(CHAIN_R - CHAIN_T / 2)
            .extrude(CHAIN_W / 2, both=True).translate((xb, y, z_low + CHAIN_R)))
    half = box(2 * CHAIN_R + CHAIN_T, CHAIN_W + 2, 2 * CHAIN_R + CHAIN_T, xb + sign * (CHAIN_R + CHAIN_T / 2), y, z_low + CHAIN_R)
    return union_all([lower, upper, ring.intersect(half)])


def _band_yz(y_fixed, y_moving, z_low, x, sign=1):
    b = _band_xz(y_fixed, y_moving, z_low, 0, sign)         # build along X, then turn it to run along Y
    return b.rotate((0, 0, 0), (0, 0, 1), 90).translate((x, 0, 0))


def _band_zx(z_fixed, z_moving, x_near, y, sign=1):
    """A chain standing in an XZ plane: near leg from z_fixed to the bend, far leg back to z_moving."""
    b = _band_xz(z_fixed, z_moving, 0, 0, sign)             # along X with runs at z 0 and 56
    b = b.rotate((0, 0, 0), (0, 1, 0), -90)                  # +X -> +Z, +Z -> -X
    return b.translate((x_near, y, 0))


# ---------------------------------------------------------------- boards and boxes
def controller_group():
    """Octopus on its plate, the 24 V supply and the two bucks, on the rear panel's top strip."""
    y = REAR
    return {
        "pcb_octopus": box(160, 28, 110, 200, y - 14, 760),
        "psu_24v": box(159, 32, 97, 385, y - 16, 760),
        "buck_12v": box(45, 16, 22, 95, y - 8, 785),
        "buck_5v": box(45, 16, 22, 95, y - 8, 745),
        "power_strip": box(300, 40, 42, 300, y - 31, 21),
    }


def pump_group():
    """Pump on rubber mounts and the release valve, on the rear panel's end post."""
    y = REAR
    mounts = union_all([cyl_z(6, 12, -160 + sx * 35, y - 26 + sy * 18, 171) for sx in (-1, 1) for sy in (-1, 1)])
    pump = box(90, 50, 45, -160, y - 27, 200)
    return {"pump": pump.union(mounts), "valve": box(50, 32, 30, -160, y - 17, 260)}


def pi_group():
    """Pi, hub, SSD, relay card, MPRLS and the Pi's supply on a plate outside the deck-end panel."""
    x = END
    return {
        "pi_plate": box(4, 340, 110, x + 2, 0, 60),
        "pcb_pi": box(20, 85, 56, x + 14, 0, 85),
        "usb_hub": box(18, 100, 40, x + 13, 110, 95),
        "ssd": box(12, 100, 70, x + 10, 110, 40),
        "pcb_relay": box(22, 85, 55, x + 15, -110, 60),
        "pcb_mprls": box(8, 18, 13, x + 8, 150, 25),
        "psu_pi": box(30, 55, 28, x + 19, -45, 20),
    }


def bench_items():
    return {"scarlett": box(175, 120, 45, 600, 290, 22.5)}


def electronics():
    """Every static electronics part, keyed by node name."""
    return {**controller_group(), **pump_group(), **pi_group(), **bench_items()}


# ---------------------------------------------------------------- chains, drawn at the home pose
def x_chain():
    return _band_xz(X_CHAIN_FIXED, HOME["x"], X_CHAIN_Z, X_CHAIN_Y, +1)


def y_chain():
    """Rides on the X carriage; drawn for the home Y position. In the x_carriage frame (origin at carX)."""
    return _band_yz(Y_CHAIN_FIXED, HOME["y"], Y_CHAIN_Z, Y_CHAIN_DX, +1)


def z_chain():
    """Rides on the Y carriage; drawn for the home Z position. In the y_carriage frame (origin at carX, carY).
    Stands above the guide block: the near leg is fixed to the block, the far leg reaches the post on the column top."""
    z_moving = HOME["z"] + P.COLUMN_L + COLUMN_POST_H
    band = _band_zx(Z_CHAIN_Z0, z_moving, Z_CHAIN_DX, 0, +1)
    fixed_bracket = box(28, CHAIN_W, CHAIN_T, Z_CHAIN_DX + 14, 0, Z_CHAIN_Z0)
    moving_bracket = box(128, 14, 14, Z_CHAIN_DX - 2 * CHAIN_R + 64, 55, z_moving)
    tab = box(14, 14, 14, Z_CHAIN_DX - 2 * CHAIN_R, 40, z_moving)
    return union_all([band, fixed_bracket, moving_bracket, tab])


def column_post():
    """Post on the column top that carries the Z chain's moving end above the guide block. In the z_carriage frame."""
    return box(P.COLUMN_W, P.COLUMN_W, COLUMN_POST_H, 0, 0, P.COLUMN_L + COLUMN_POST_H / 2)


# ---------------------------------------------------------------- cables
CABLE_R = {"bundle": 4.0, "hose": 3.0, "tube": 2.0, "usb": 2.5, "mains": 3.0, "ribbon": 4.0, "wire": 2.0}


def static_cables():
    """Runs that do not move, keyed by node name. Every point is on the outside of a panel or on the bench."""
    y = REAR - 8                                             # on the rear panel's outer face
    xe = END + 6                                             # on the deck-end panel's outer face
    out = {}
    # controller group up into the X chain
    out["cable_climb"] = tube([(200, REAR - 12, 816), (200, X_CHAIN_Y, X_CHAIN_Z - 8)], CABLE_R["bundle"])
    # X end-stop, fixed at the deck end of the rear beam
    out["cable_x_endstop"] = tube([(280, REAR - 12, 770), (280, y, 822), (982, y, 822), (982, REAR - 12, 845)], CABLE_R["wire"])
    # pump and valve drive
    out["cable_pump"] = tube([(120, REAR - 12, 720), (120, y, 700), (-130, y, 700), (-130, y, 300), (-140, REAR - 12, 277)], CABLE_R["wire"])
    out["cable_valve"] = tube([(-130, y, 300), (-130, y, 236), (-140, REAR - 12, 224)], CABLE_R["wire"])
    # vacuum hose, pump to the X chain's fixed end; the tube stub from the valve to the MPRLS at the Pi
    out["hose"] = tube([(-205, REAR - 27, 210), (-215, y, 300), (60, y, 300), (60, y, 840), (195, X_CHAIN_Y, X_CHAIN_Z - 9)], CABLE_R["hose"])
    out["tube_mprls"] = tube([(-135, REAR - 12, 262), (-120, y, 290), (982, y, 290), (xe, y + 10, 290), (xe, 150, 290), (xe, 150, 40), (END + 5, 150, 30)], CABLE_R["tube"])
    # Pi to Octopus, USB-C, along the outside of both panels
    out["cable_usbc"] = tube([(END + 12, -10, 100), (xe, -10, 330), (xe, y + 10, 330), (982, y, 330), (290, y, 330), (290, y, 700), (280, REAR - 12, 740)], CABLE_R["usb"])
    # cue servo and LED bar, along the rear panel to the deck-end panel and through it
    out["cable_servo"] = tube([(170, REAR - 12, 705), (170, y, 360), (982, y, 360), (xe, y + 10, 360), (xe, P.CUE_SERVO_Y, 360), (xe, P.CUE_SERVO_Y, 130), (975, P.CUE_SERVO_Y, 130), (958, P.CUE_SERVO_Y, P.CUE_SERVO_Z)], CABLE_R["wire"])
    out["cable_led"] = tube([(xe, P.CUE_SERVO_Y, 200), (xe, 65, 200), (xe, 65, 130), (975, 65, 130), (958, 65, 117)], CABLE_R["wire"])
    # carousel stepper and home sensor, along the rear panel, round its open end and over the base plate
    out["cable_carousel"] = tube([(140, REAR - 12, 705), (140, y, 400), (-225, y, 400), (-225, y, 25), (-232, -420, 24), (-156, -336, 24),
                                  (-224, -243, 24), (-620, 50, 24), (-645, 68, 55)], CABLE_R["bundle"])   # between two roller brackets, under the tooth ring
    # relay card into the deck, deck line out to the Scarlett, Scarlett to the hub
    out["cable_relay"] = tube([(END + 15, -110, 88), (xe, -110, 140), (xe, -190, 140), (830, -190, 80), (816, -180, 80)], CABLE_R["wire"])
    out["cable_audio"] = tube([(700, -180, 80), (700, -200, 12), (830, -200, 12), (830, 300, 12), (690, 300, 25)], CABLE_R["wire"])
    out["cable_scarlett_usb"] = tube([(690, 290, 45), (975, 300, 130), (xe, 300, 130), (xe, 130, 130), (END + 13, 130, 116)], CABLE_R["usb"])
    # deck camera ribbon through the panel
    out["cable_ribbon"] = tube([(END + 14, 20, 113), (xe, 20, 150), (END - 10, 20, 155), (960, 20, 155)], CABLE_R["ribbon"])
    # mains: supply, Pi supply and deck to the strip
    out["mains_psu"] = tube([(330, y, 45), (330, y, 690), (360, REAR - 12, 711)], CABLE_R["mains"])
    out["mains_pi"] = tube([(END + 19, -45, 34), (xe, -100, 20), (xe, -452, 20), (982, -452, 20), (450, y, 40)], CABLE_R["mains"])
    out["mains_deck"] = tube([(830, -185, 60), (900, -300, 130), (xe, -300, 130), (xe, -452, 24), (982, -452, 24), (460, y, 44)], CABLE_R["mains"])   # out through the end panel's window
    return out


def x_carriage_cables():
    """From the X chain's moving end to the Y chain's fixed end and to the X motor; in the x_carriage frame."""
    return {
        "cable_y_chain_feed": tube([(0, X_CHAIN_Y + 6, X_CHAIN_Z + 2 * CHAIN_R + 4), (Y_CHAIN_DX, -400, 900), (Y_CHAIN_DX, Y_CHAIN_FIXED - 10, Y_CHAIN_Z - 8)], CABLE_R["bundle"]),
        "cable_x_motor": tube([(6, X_CHAIN_Y + 6, X_CHAIN_Z + 2 * CHAIN_R + 4), (6, -455, 912)], CABLE_R["wire"]),
    }


def y_carriage_cables():
    """From the Y chain's moving end to the Z motor and to the Z chain's fixed end; in the y_carriage frame."""
    z_top = Y_CHAIN_Z + 2 * CHAIN_R
    return {
        "cable_z_motor": tube([(Y_CHAIN_DX, 0, z_top + 8), (-20, 60, 960), (0, 65, 990)], CABLE_R["wire"]),
        "cable_z_chain_feed": tube([(Y_CHAIN_DX, 8, z_top + 8), (Z_CHAIN_DX, 8, Z_CHAIN_Z0 - 8)], CABLE_R["bundle"]),
    }


def outrigger_cables():
    """From the column's slot, over the block and along the outrigger to the wrist hub; in the z_carriage frame."""
    return tube([(0, 22, 44), (0, 38, 44), (0, 38, 0), (30, 22, 0), (72, 22, 0), (78, 12, 8)], CABLE_R["bundle"])


def wrist_cables():
    """Hose to the cup and USB to the camera, on the arm's +Y face; in the wrist frame."""
    L = P.ARM_L
    hose = tube([(0, 27, -8), (0, 15, -40), (0, 15, -L + 30), (-20, 8, -L + 14), (-20, -16, -L + 2), (-13, -16, -L)], CABLE_R["hose"])
    usb = tube([(4, 27, 0), (14, 12, -20), (14, 0, -L + 110), (39, 0, -L + 110)], CABLE_R["usb"])
    return hose.union(usb)


COLORS = {
    "pcb_octopus": (0.10, 0.30, 0.20), "pcb_pi": (0.10, 0.35, 0.22), "pcb_relay": (0.10, 0.30, 0.20),
    "pcb_mprls": (0.15, 0.20, 0.45), "psu_24v": (0.75, 0.76, 0.78), "psu_pi": (0.15, 0.15, 0.16),
    "buck_12v": (0.15, 0.20, 0.45), "buck_5v": (0.15, 0.20, 0.45), "power_strip": (0.90, 0.90, 0.90),
    "pump": (0.20, 0.20, 0.22), "valve": (0.70, 0.60, 0.25), "pi_plate": (0.85, 0.39, 0.17),
    "usb_hub": (0.20, 0.20, 0.22), "ssd": (0.35, 0.36, 0.38), "scarlett": (0.80, 0.15, 0.12),
    "x_chain": (0.12, 0.12, 0.13), "y_chain": (0.12, 0.12, 0.13), "z_chain": (0.12, 0.12, 0.13),
    "column_post": (0.24, 0.27, 0.31),
    "hose": (0.55, 0.70, 0.90), "tube_mprls": (0.55, 0.70, 0.90),
    "cable_usbc": (0.20, 0.40, 0.80), "cable_scarlett_usb": (0.20, 0.40, 0.80),
    "cable_ribbon": (0.90, 0.55, 0.15),
    "mains_psu": (0.05, 0.05, 0.05), "mains_pi": (0.05, 0.05, 0.05), "mains_deck": (0.05, 0.05, 0.05),
}
CABLE_DEFAULT = (0.45, 0.45, 0.48)
RIGID_MOVING = ("outrigger_cables", "wrist_cables", "column_post")   # checked by the sweep; the rest is drawn at home
