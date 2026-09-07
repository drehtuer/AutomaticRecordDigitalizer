"""Export STL files of the printed parts and STEP files of the sub-assemblies.

    python -m cad.export_parts
"""
from pathlib import Path

import cadquery as cq

from .parts import carousel, deck, deck_interface, frame, gantry

EXPORT = Path(__file__).parent / "export"

PRINTED = {
    "carousel_comb": carousel.comb,
    "carousel_hub": carousel.hub,
    "carousel_roller_bracket": carousel.roller_bracket,
    "station_ring_rest": frame.ring_rest,
    "wrist_fork": gantry.fork,
}

SUBASSEMBLIES = {
    "gantry_wrist": gantry.wrist,
    "gantry_z_carriage": gantry.z_carriage,
    "carousel_disc": carousel.disc,
    "carousel_base": carousel.base,
    "deck_interface": deck_interface.cue_servo_assembly,
    "frame": frame.frame,
    "station": frame.station,
    "deck_plinth": deck.plinth,
}


def main():
    EXPORT.mkdir(exist_ok=True)
    for name, fn in PRINTED.items():
        cq.exporters.export(fn(), str(EXPORT / f"{name}.stl"), tolerance=0.05, angularTolerance=0.1)
        print("wrote", name + ".stl")
    for name, fn in SUBASSEMBLIES.items():
        cq.exporters.export(fn(), str(EXPORT / f"{name}.step"))
        print("wrote", name + ".step")


if __name__ == "__main__":
    main()
