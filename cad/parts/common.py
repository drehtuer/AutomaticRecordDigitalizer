"""Small helpers so the part files read like the specification."""

import cadquery as cq


def box(sx, sy, sz, cx=0.0, cy=0.0, cz=0.0):
    """Axis-aligned box of size (sx, sy, sz) centred at (cx, cy, cz)."""
    return cq.Workplane("XY").box(sx, sy, sz).translate((cx, cy, cz))


def cyl_z(r, h, cx=0.0, cy=0.0, z0=0.0):
    """Cylinder along Z from z0 to z0+h."""
    return cq.Workplane("XY").circle(r).extrude(h).translate((cx, cy, z0))


def cyl_x(r, h, x0=0.0, cy=0.0, cz=0.0):
    """Cylinder along X from x0 to x0+h."""
    return cq.Workplane("YZ").circle(r).extrude(h).translate((x0, cy, cz))


def cyl_y(r, h, cx=0.0, y0=0.0, cz=0.0):
    """Cylinder along Y from y0 to y0+h."""
    return cq.Workplane("XZ").circle(r).extrude(-h).translate((cx, y0, cz))


def ring_z(r_out, r_in, h, cx=0.0, cy=0.0, z0=0.0):
    return (cq.Workplane("XY").circle(r_out).circle(r_in).extrude(h).translate((cx, cy, z0)))


def torus_z(r_major, r_minor, cx=0.0, cy=0.0, cz=0.0, arc_deg=360.0):
    """Torus (or arc of one) with its axis along Z, centred at (cx, cy, cz)."""
    t = cq.Workplane("XZ").moveTo(r_major, 0).circle(r_minor).revolve(arc_deg, (0, 0, 0), (0, 1, 0))
    return t.translate((cx, cy, cz))


def rot_z(shape, deg, about=(0.0, 0.0, 0.0)):
    return shape.rotate((about[0], about[1], 0), (about[0], about[1], 1), deg)


def rot_x(shape, deg, about=(0.0, 0.0, 0.0)):
    return shape.rotate((0, about[1], about[2]), (1, about[1], about[2]), deg)


def union_all(shapes):
    out = None
    for s in shapes:
        out = s if out is None else out.union(s)
    return out
