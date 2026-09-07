"""Export the machine as glTF for the viewer in the documentation.

    python -m cad.export_web

Writes export/web/machine.glb: the whole machine at one pose, in a single
binary glTF with the colours assembly.py assigns. The tolerances are coarser
than the STEP and STL exports on purpose; this file is loaded over the network
by a browser, not printed or opened in FreeCAD.
"""
from pathlib import Path

from .assembly import build_assembly, state_at

EXPORT = Path(__file__).parent / "export" / "web"

# The pose to show: the record is on the platter and the gantry is clear of it,
# which reads as the machine doing its job rather than parked.
POSE = "place"

# Millimetres and degrees of deviation allowed when the solids are tessellated.
# 0.5 mm is invisible at the size the viewer draws the machine and keeps the
# file small enough to load on a phone.
TOLERANCE = 0.5
ANGULAR_TOLERANCE = 0.5


def main():
    EXPORT.mkdir(parents=True, exist_ok=True)
    state, vis = state_at(POSE)
    asm = build_assembly(state, vis)
    out = EXPORT / "machine.glb"
    asm.export(str(out), tolerance=TOLERANCE, angularTolerance=ANGULAR_TOLERANCE)
    print(f"wrote {out.name} at pose {POSE}: {out.stat().st_size / 1024:.0f} kB")


if __name__ == "__main__":
    main()
