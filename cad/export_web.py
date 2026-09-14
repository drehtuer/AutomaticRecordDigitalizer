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
from .assembly import Machine, color_of
from .parts import carousel, deck, frame, gantry
from .parts.carousel import DEMO_LOAD, RADII

EXPORT = Path(__file__).parent / "export" / "web"

# Coarser than the STEP and STL exports on purpose: this file crosses a network.
TOLERANCE = 0.5
ANGULAR_TOLERANCE = 0.5



def rest_parts(m):
    """Every rigid body at rest, keyed by the node name the viewer looks for.

    Machine already caches the moving parts in their own frames; the pose
    transforms live in the viewer instead of being baked in here.
    """
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
        "column_post": m.column_post0,
        "outrigger_cables": m.outrigger_cables0,
        "wrist_cables": m.wrist_cables0,
    }
    # The record the cycle handles, in every size; the viewer shows the chosen size's nodes.
    for sz, r in RADII.items():
        parts[f"record_held_{sz}"] = gantry.held_record(r)
        parts[f"record_platter_{sz}"] = deck.record_on_platter(r)
        parts[f"record_ring_{sz}"] = frame.record_on_ring(r)
        parts[f"record_slot0_{sz}"] = carousel.record_in_slot(0, r)
    for k, rec in enumerate(m.slot_recs0):
        if k > 0 and rec is not None:
            parts[f"record_slot{k}"] = rec
    # Electronics, chains and cables. The chains and their feed cables are drawn at the home pose.
    parts.update(m.electronics)
    parts.update(m.display_static)
    parts.update(m.display_x)
    parts.update(m.display_y)
    return parts


def scene(m):
    """Constants the viewer needs. Every number is read from params."""
    sizes = list(RADII)
    return {
        "units": "mm",
        "sizes": sizes,
        "carousel": {"centre": [P.CAR_CX, P.CAR_CY], "slots": P.CAR_SLOTS,
                     "load": {str(k): sz for k, sz in DEMO_LOAD.items()}},
        "wrist": {"offsetX": P.WRIST_X},
        "tonearm": {"pivot": list(P.ARM_PIVOT), "lift": P.ARM_LIFT},
        # Which node names hang off which moving group. The viewer nests them
        # x -> y -> z -> wrist, exactly as Machine.moving composes the transforms.
        "groups": {
            "static": ["bench", "frame", "station", "plinth", "deck_interface",
                       "deck_camera", "carousel_base", *m.electronics, *m.display_static,
                       *[f"record_platter_{sz}" for sz in sizes], *[f"record_ring_{sz}" for sz in sizes]],
            "carousel": ["carousel_disc", *[f"record_slot0_{sz}" for sz in sizes],
                         *[f"record_slot{k}" for k in range(1, P.CAR_SLOTS) if m.slot_recs0[k] is not None]],
            "tonearm": ["tonearm"],
            "x": ["x_carriage", *m.display_x],
            "y": ["y_carriage", *m.display_y],
            "z": ["z_carriage", "column_post", "outrigger_cables"],
            "wrist": ["wrist", "wrist_cables", *[f"record_held_{sz}" for sz in sizes]],
        },
        # Node shown, for each record size, when the named visibility flag is set.
        # "slot" governs the record in slot 0, the one the cycle is handling; every
        # size's node exists and the viewer shows the chosen size's.
        "visibility": {
            "held": {sz: f"record_held_{sz}" for sz in sizes},
            "platter": {sz: f"record_platter_{sz}" for sz in sizes},
            "ring": {sz: f"record_ring_{sz}" for sz in sizes},
            "slot": {sz: f"record_slot0_{sz}" for sz in sizes},
        },
    }


def main():
    EXPORT.mkdir(parents=True, exist_ok=True)

    asm = cq.Assembly(name="AutomaticRecordDigitalizer")
    m = Machine(load=DEMO_LOAD)
    for name, solid in rest_parts(m).items():
        asm.add(solid, name=name, color=cq.Color(*color_of(name)))

    glb = EXPORT / "parts.glb"
    asm.export(str(glb), tolerance=TOLERANCE, angularTolerance=ANGULAR_TOLERANCE)

    meta = EXPORT / "scene.json"
    meta.write_text(json.dumps(scene(m), indent=1) + "\n")

    print(f"wrote {glb.name}: {glb.stat().st_size / 1024:.0f} kB, "
          f"{len(rest_parts(m))} parts")
    print(f"wrote {meta.name}")


if __name__ == "__main__":
    main()
