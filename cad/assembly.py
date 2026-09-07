"""Build the machine at a pose, as CadQuery solids or as a cq.Assembly for STEP export.

    python -m cad.assembly                 # exports export/assembly_<pose>.step for a few poses
    python -m cad.assembly place regrip    # chosen pose ids
"""
import sys
from pathlib import Path

import cadquery as cq

from . import kinematics as K
from . import params as P
from .parts import carousel, deck, deck_interface, frame, gantry

EXPORT = Path(__file__).parent / "export"


def _rot_x(shape, deg):
    return shape.rotate((0, 0, 0), (1, 0, 0), deg)


def _rot_z_about(shape, deg, cx, cy):
    return shape.rotate((cx, cy, 0), (cx, cy, 1), deg)


class Machine:
    """Caches the static solids; place() returns the moving ones for a state."""

    def __init__(self):
        self.bench = frame.bench()
        self.frame = frame.frame()
        self.station = frame.station()
        self.plinth = deck.plinth()
        self.deck_if = deck_interface.cue_servo_assembly()
        self.deck_cam = deck_interface.deck_camera_and_led()
        self.car_base = carousel.base()
        self.car_disc0 = carousel.disc()
        self.slot_recs0 = [carousel.record_in_slot(k) for k in range(P.CAR_SLOTS)]
        self.xcar0 = gantry.x_carriage()
        self.ycar0 = gantry.y_carriage()
        self.zcar0 = gantry.z_carriage()
        self.wrist0 = gantry.wrist()
        self.held0 = gantry.held_record()
        self.platter_rec = deck.record_on_platter()
        self.ring_rec = frame.record_on_ring()

    def static(self):
        return {"bench": self.bench, "frame": self.frame, "station": self.station, "plinth": self.plinth,
                "deck_interface": self.deck_if, "deck_camera": self.deck_cam, "carousel_base": self.car_base}

    def environment(self, s, vis):
        """Static-for-this-pose solids the gantry must not touch."""
        env = dict(self.static())
        env["tonearm"] = deck.tonearm(s["a"], s["l"])
        env["carousel_disc"] = _rot_z_about(self.car_disc0, s["c"], P.CAR_CX, P.CAR_CY)
        for k, rec in enumerate(self.slot_recs0):
            if k == 0 and not vis["slot"]:
                continue
            env[f"record_slot{k}"] = _rot_z_about(rec, s["c"], P.CAR_CX, P.CAR_CY)
        if vis["platter"]:
            env["record_platter"] = self.platter_rec
        if vis["ring"]:
            env["record_ring"] = self.ring_rec
        return env

    def moving(self, s, vis):
        x, y, z = s["x"], s["y"], s["z"]
        parts = {
            "x_carriage": self.xcar0.translate((x, 0, 0)),
            "y_carriage": self.ycar0.translate((x, y, 0)),
            "z_carriage": self.zcar0.translate((x, y, z)),
            "wrist": _rot_x(self.wrist0, s["phi"]).translate((x + P.WRIST_X, y, z)),
        }
        if vis["held"]:
            parts["record_held"] = _rot_x(self.held0, s["phi"]).translate((x + P.WRIST_X, y, z))
        return parts


COLORS = {
    "bench": (0.85, 0.80, 0.69), "frame": (0.89, 0.79, 0.63), "station": (0.85, 0.39, 0.17),
    "plinth": (0.78, 0.80, 0.82), "deck_interface": (0.24, 0.27, 0.31), "deck_camera": (0.11, 0.11, 0.13),
    "carousel_base": (0.24, 0.27, 0.31), "carousel_disc": (0.89, 0.79, 0.63), "tonearm": (0.72, 0.75, 0.78),
    "x_carriage": (0.17, 0.18, 0.21), "y_carriage": (0.24, 0.27, 0.31), "z_carriage": (0.24, 0.27, 0.31),
    "wrist": (0.85, 0.39, 0.17),
}


def build_assembly(state, vis):
    m = Machine()
    asm = cq.Assembly(name="AutomaticRecordDigitalizer")
    for name, solid in {**m.environment(state, vis), **m.moving(state, vis)}.items():
        col = COLORS.get(name, (0.06, 0.06, 0.07) if name.startswith("record") else (0.5, 0.5, 0.5))
        asm.add(solid, name=name, color=cq.Color(*col))
    return asm


def state_at(pose_id):
    """State and visibility at the end of the named pose."""
    for pose, keys in K.full_cycle():
        if pose["id"] == pose_id:
            vis = pose.get("after") or pose["before"]
            return keys[-1], vis
    raise KeyError(pose_id)


if __name__ == "__main__":
    ids = sys.argv[1:] or ["place", "liftarm", "station", "regrip"]
    EXPORT.mkdir(exist_ok=True)
    for pid in ids:
        st, vis = state_at(pid)
        asm = build_assembly(st, vis)
        out = EXPORT / f"assembly_{pid}.step"
        asm.save(str(out))
        print("wrote", out)
