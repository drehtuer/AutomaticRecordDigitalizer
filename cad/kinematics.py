"""Poses, forward kinematics and the motion planner of the cycle.

A pose is a dict with keys x, y, z (Z-carriage centre in machine mm), phi (wrist angle, degrees,
right-hand rotation about +X; 0 = arm hanging, cup facing -Y; +90 = cup down; -90 = cup up; 180 = arm up),
a (tonearm azimuth, degrees), l (cue lift 0/1), c (carousel angle, degrees).

The planner produces keyframe lists exactly like the concept model's: retreat, raise, ordered
horizontal moves, lower, approach, with special plans for the station and the tonearm steps.
"""
from math import radians, cos, sin
from . import params as P
from .parts.deck import finger_lift_point, platter_top_z
from .parts.carousel import pick_record_centre

TRAVEL = P.TRAVEL_Z


def cup_offset(phi_deg):
    """Cup centre relative to the wrist pivot for wrist angle phi."""
    p = radians(phi_deg)
    c, L = P.CUP_OFF, P.ARM_L
    return (0.0, -c * cos(p) + L * sin(p), -c * sin(p) - L * cos(p))


def fork_offset(phi_deg):
    p = radians(phi_deg)
    return (0.0, -P.FORK_L * sin(p), P.FORK_L * cos(p))


def carriage_for_cup(tx, ty, tz, phi):
    ox, oy, oz = cup_offset(phi)
    return {"x": tx - ox - P.WRIST_X, "y": ty - oy, "z": tz - oz, "phi": phi}


def carriage_for_fork(fx, fy, fz):
    ox, oy, oz = fork_offset(180.0)
    return {"x": fx - ox - P.WRIST_X, "y": fy - oy, "z": fz - oz, "phi": 180.0}


def fork_on(arm_state):
    """Carriage pose with the fork's crossbar 7 mm above the finger lift, arm lifted."""
    fx, fy, fz = finger_lift_point(P.ARM_ANGLE[arm_state], lift=1.0)
    return carriage_for_fork(fx, fy, fz + 7.0)


# ---------------------------------------------------------------- targets
PICK = pick_record_centre()
PICK_CUP = (PICK[0], PICK[1] + P.RECORD_T / 2 + P.CUP_H / 2, PICK[2])
PLATTER_REC_Z = platter_top_z() + 3.0 + P.RECORD_T / 2            # released 3 mm above the mat
PLACE_CUP = (P.DECK_SPINDLE_X, P.DECK_SPINDLE_Y, PLATTER_REC_Z + P.RECORD_T / 2 + P.CUP_H / 2)
RING_TOP = P.ST_Z + P.ST_RING_TUBE
STATION_CUP = (P.ST_X, P.ST_Y, P.ST_Z)                             # cup up; the record on it touches the ring top exactly when set down
RING_REC_Z = RING_TOP + P.RECORD_T / 2
REGRIP_CUP = (P.ST_X, P.ST_Y, RING_REC_Z + P.RECORD_T / 2 + P.CUP_H / 2)
PARK = {"x": 200.0, "y": -220.0, "z": TRAVEL, "phi": 180.0}


def V(held, slot, platter, ring):
    return {"held": held, "slot": slot, "platter": platter, "ring": ring}


POSES = [
    dict(id="pick", name="Pick from carousel", car=lambda: carriage_for_cup(*PICK_CUP, 0.0),
         approach=(0, 8, 0), before=V(False, True, False, False), after=V(True, False, False, False), spin=False),
    dict(id="place", name="Place side A", car=lambda: carriage_for_cup(*PLACE_CUP, 90.0),
         before=V(True, False, False, False), spin=False),
    dict(id="liftarm", name="Lift arm, engage fork", car=lambda: fork_on("rest"), approach=(0, 0, 40),
         before=V(False, False, True, False), arm=("rest", 1), spin=False, plan="liftarm"),
    dict(id="toleadin", name="Carry arm to lead-in", car=lambda: fork_on("leadin"),
         before=V(False, False, True, False), arm=("leadin", 1), spin=False, plan="direct"),
    dict(id="drop", name="Lower needle, start", car=lambda: {**fork_on("leadin"), "z": fork_on("leadin")["z"] + 80},
         before=V(False, False, True, False), arm=("leadin", 0), spin=True, plan="drop"),
    dict(id="runout", name="Run-out: stop, lift, find arm", car=lambda: fork_on("runout"), approach=(0, 0, 40),
         before=V(False, False, True, False), arm=("runout", 1), spin=False, plan="runout"),
    dict(id="torest", name="Carry arm to rest, lower", car=lambda: {**fork_on("rest"), "z": fork_on("rest")["z"] + 80},
         before=V(False, False, True, False), arm=("rest", 0), spin=False, plan="torest"),
    dict(id="lift", name="Lift record off the platter", car=lambda: carriage_for_cup(*PLACE_CUP, 90.0),
         before=V(False, False, True, False), after=V(True, False, False, False), spin=False),
    dict(id="station", name="Carry to station, B up", car=lambda: carriage_for_cup(*STATION_CUP, -90.0),
         before=V(True, False, False, False), spin=False, plan="station"),
    dict(id="release", name="Release & withdraw", car=lambda: carriage_for_cup(P.ST_X, P.ST_Y, P.ST_Z - 60.0, -90.0),
         before=V(False, False, False, True), spin=False, plan="direct"),
    dict(id="regrip", name="Re-grip from above", car=lambda: carriage_for_cup(*REGRIP_CUP, 90.0), approach=(0, 0, 30),
         before=V(False, False, False, True), after=V(True, False, False, False), spin=False, plan="regrip"),
    dict(id="placeB", name="Place side B", car=lambda: carriage_for_cup(*PLACE_CUP, 90.0),
         before=V(True, False, False, False), spin=False),
    dict(id="return", name="Return to its slot", car=lambda: carriage_for_cup(*PICK_CUP, 0.0),
         before=V(True, False, False, False), after=V(False, True, False, False), retreat=(0, 8, 0), spin=False),
    dict(id="index", name="Index carousel", car=lambda: {"x": 200.0, "y": 30.0, "z": TRAVEL, "phi": 0.0},
         carousel=360.0 / P.CAR_SLOTS, before=V(False, True, False, False), spin=False),
]

HOME = {"x": 200.0, "y": 30.0, "z": TRAVEL, "phi": 0.0, "a": P.ARM_ANGLE["rest"], "l": 0.0, "c": 0.0}


def _push(keys, state, **changes):
    state = {**state, **changes}
    keys.append(state)
    return state


def default_plan(f, g, retreat=None, approach=None):
    keys, s = [], dict(f)
    keys.append(s)
    a = approach or (0, 0, 0)
    if retreat:
        s = _push(keys, s, x=f["x"] + retreat[0], y=f["y"] + retreat[1], z=f["z"] + retreat[2])
    s = _push(keys, s, z=max(TRAVEL, s["z"], g["z"] + a[2]))
    if g["x"] > f["x"] + 10:          # leaving the carousel: X, then Y, then wrist
        s = _push(keys, s, x=g["x"] + a[0])
        s = _push(keys, s, y=g["y"] + a[1])
        s = _push(keys, s, phi=g["phi"], c=g["c"], a=g["a"], l=g["l"])
    else:                             # towards it: wrist, then Y, then X
        s = _push(keys, s, phi=g["phi"], c=g["c"], a=g["a"], l=g["l"])
        s = _push(keys, s, y=g["y"] + a[1])
        s = _push(keys, s, x=g["x"] + a[0])
    s = _push(keys, s, z=g["z"] + a[2])
    s = _push(keys, s, x=g["x"], y=g["y"], z=g["z"], a=g["a"], l=g["l"])
    return keys


def plan(pose, f, prev=None):
    """Keyframes from state f to the target of `pose`."""
    g = {**f, **pose["car"]()}
    g["c"] = f["c"] + pose.get("carousel", 0.0)
    if "arm" in pose:
        g["a"], g["l"] = P.ARM_ANGLE[pose["arm"][0]], float(pose["arm"][1])
    kind = pose.get("plan")
    if kind == "direct":
        return [f, g]
    if kind == "liftarm":
        f2 = {**f, "l": 1.0}
        return [f, f2] + default_plan(f2, g, None, pose.get("approach"))[1:]
    if kind == "drop":
        return [f, {**f, "z": g["z"]}, {**g, "l": 0.0}]
    if kind == "runout":
        f1 = {**f, "a": g["a"], "l": 0.0}
        f2 = {**f1, "l": 1.0}
        return [f, f1, f2] + default_plan(f2, g, None, pose.get("approach"))[1:]
    if kind == "torest":
        on = fork_on("rest")
        k1 = {**f, "x": on["x"], "y": on["y"], "a": P.ARM_ANGLE["rest"], "l": 1.0}
        k2 = {**k1, "z": g["z"]}
        return [f, k1, k2, {**g, "l": 0.0}]
    if kind == "station":
        # raise; swing the record to vertical (it hangs inside the frame); move Y; swing to B-up; X; lower
        keys, s = [f], dict(f)
        s = _push(keys, s, z=TRAVEL)
        s = _push(keys, s, phi=0.0)
        s = _push(keys, s, y=g["y"])
        s = _push(keys, s, phi=g["phi"])
        s = _push(keys, s, x=g["x"])
        s = _push(keys, s, z=g["z"])
        return keys
    if kind == "regrip":
        keys, s = [f], dict(f)
        s = _push(keys, s, y=f["y"] + 185)
        s = _push(keys, s, z=P.TRAVEL_Z_STATION)
        s = _push(keys, s, phi=0.0)
        s = _push(keys, s, y=g["y"])
        s = _push(keys, s, phi=g["phi"])
        s = _push(keys, s, z=g["z"] + 30)
        s = _push(keys, s, z=g["z"])
        return keys
    retreat = prev.get("retreat") if prev else None
    return default_plan(f, g, retreat, pose.get("approach"))


def full_cycle():
    """List of (pose, keyframes, visibility_before, visibility_after) for one record."""
    state, prev, out = dict(HOME), None, []
    for pose in POSES:
        keys = plan(pose, state, prev)
        out.append((pose, keys))
        state, prev = keys[-1], pose
    return out


def interpolate(k0, k1, t):
    return {k: k0[k] + (k1[k] - k0[k]) * t for k in ("x", "y", "z", "phi", "a", "l", "c")}


if __name__ == "__main__":
    import json, sys
    cyc = [{"id": p["id"], "name": p["name"], "keyframes": ks, "before": p["before"], "after": p.get("after")}
           for p, ks in full_cycle()]
    json.dump(cyc, sys.stdout, indent=1)
