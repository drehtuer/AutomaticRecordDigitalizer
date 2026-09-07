"""Export the machine for the WebGL viewer in the documentation.

    python -m cad.export_web

Writes two files into export/web/:

    parts.glb    every rigid body of the machine, each a named node in its own
                 rest frame, with the colours assembly.py assigns
    scene.json   the constants the viewer needs to assemble and animate them

The viewer applies the same transforms assembly.Machine does, so the pictures
in the documentation move exactly as check_collisions.py sweeps them. Nothing
here restates a dimension: everything comes from params.py through Machine.

The cycle itself is not written here. It is cycle.json, from kinematics.
"""
import json
from pathlib import Path

import cadquery as cq

from . import params as P
from .assembly import COLORS, Machine
from .parts import deck

EXPORT = Path(__file__).parent / "export" / "web"

# Coarser than the STEP and STL exports on purpose: this file crosses a network.
TOLERANCE = 0.5
ANGULAR_TOLERANCE = 0.5

DEFAULT_COLOR = (0.5, 0.5, 0.5)
RECORD_COLOR = (0.06, 0.06, 0.07)


def rest_parts():
    """Every rigid body at rest, keyed by the node name the viewer looks for.

    Machine already caches the moving parts in their own frames; the pose
    transforms live in the viewer instead of being baked in here.
    """
    m = Machine()
    parts = {
        # Bolted down.
        "bench": m.bench,
        "frame": m.frame,
        "station": m.station,
        "plinth": m.plinth,
        "deck_interface": m.deck_if,
        "deck_camera": m.deck_cam,
        "carousel_base": m.car_base,
        # Turns with the carousel.
        "carousel_disc": m.car_disc0,
        # Pivots about the tonearm bearing; built at azimuth 0 with the cue down.
        "tonearm": deck.tonearm(0.0, 0.0),
        # Ride the gantry, each already in its own frame.
        "x_carriage": m.xcar0,
        "y_carriage": m.ycar0,
        "z_carriage": m.zcar0,
        "wrist": m.wrist0,
        "record_held": m.held0,
        # Shown or hidden by the state of the cycle.
        "record_platter": m.platter_rec,
        "record_ring": m.ring_rec,
    }
    for k, rec in enumerate(m.slot_recs0):
        parts[f"record_slot{k}"] = rec
    return parts


def scene():
    """Constants the viewer needs. Every number is read from params."""
    return {
        "units": "mm",
        "carousel": {"centre": [P.CAR_CX, P.CAR_CY], "slots": P.CAR_SLOTS},
        "wrist": {"offsetX": P.WRIST_X},
        "tonearm": {"pivot": list(P.ARM_PIVOT), "lift": P.ARM_LIFT},
        # Which node names hang off which moving group. The viewer nests them
        # x -> y -> z -> wrist, exactly as Machine.moving composes the transforms.
        "groups": {
            "static": ["bench", "frame", "station", "plinth", "deck_interface",
                       "deck_camera", "carousel_base"],
            "carousel": ["carousel_disc"] + [f"record_slot{k}" for k in range(P.CAR_SLOTS)],
            "tonearm": ["tonearm"],
            "x": ["x_carriage"],
            "y": ["y_carriage"],
            "z": ["z_carriage"],
            "wrist": ["wrist", "record_held"],
        },
        # Node shown when the named visibility flag is set. "slot" governs the
        # record in slot 0, the one the cycle is handling.
        "visibility": {
            "held": "record_held",
            "platter": "record_platter",
            "ring": "record_ring",
            "slot": "record_slot0",
        },
    }


def main():
    EXPORT.mkdir(parents=True, exist_ok=True)

    asm = cq.Assembly(name="AutomaticRecordDigitalizer")
    for name, solid in rest_parts().items():
        col = COLORS.get(name, RECORD_COLOR if name.startswith("record") else DEFAULT_COLOR)
        asm.add(solid, name=name, color=cq.Color(*col))

    glb = EXPORT / "parts.glb"
    asm.export(str(glb), tolerance=TOLERANCE, angularTolerance=ANGULAR_TOLERANCE)

    meta = EXPORT / "scene.json"
    meta.write_text(json.dumps(scene(), indent=1) + "\n")

    print(f"wrote {glb.name}: {glb.stat().st_size / 1024:.0f} kB, "
          f"{len(rest_parts())} parts")
    print(f"wrote {meta.name}")


if __name__ == "__main__":
    main()
