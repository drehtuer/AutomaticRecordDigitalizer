# CAD

Parametric CadQuery model of the machine, the motion planner of the cycle, and a collision
checker that sweeps every step of the cycle against the whole machine.

```sh
pip install cadquery            # 2.4 or newer; pulls in the OpenCascade kernel
python -m cad.check_collisions  # sweep the full cycle with a 12", then the pick with a 10" and a 7"; exit 1 on any intersection
python -m cad.check_collisions --size 7   # the whole cycle with a 7"
python -m cad.assembly place regrip   # STEP of the whole machine at named poses
python -m cad.export_parts      # STL of the printed parts, STEP of the sub-assemblies
python -m cad.kinematics > cad/cycle.json  # the keyframes of the cycle for every record size, keyed "12", "10", "7" (--size 7 for one, as a bare list)
python -m cad.export_web        # glTF of every rigid body plus scene.json, for cad-model.html
python -m cad.render            # PNG views of the machine at rest into docs/images/, for the documents
python -m cad.render --animate  # the cycle for every record size as animated PNG, into docs/images/
```

Run the commands from the repository root.

## Layout

`params.py` holds every dimension in millimetres, including the deck measurements marked
MEASURE that still have to be confirmed with a ruler. Change a number there and everything
downstream follows.

`parts/` builds the solids: `deck.py` (plinth, platter, tonearm as a rigid body pivoting about
the measured pivot, cue lever), `carousel.py` (base with roller ring, rotating disc with hub,
V-floor combs and tooth ring, records of any size as spokes), `frame.py` (plywood box, V-slot beams, flip
station on its foot), `gantry.py` (X, Y and Z carriages and the wrist with cup, camera and
fork, each in its own kinematic frame), `deck_interface.py` (cue-lever servo bracket with
pusher and end stop, deck camera and LED bar), `electronics.py` (every board and box on the frame
at its catalogue size, the three cable chains, and the cable and hose runs as tubes along their
routes). The chains and the cables that feed them are drawn at the home pose, because their shape
changes with every move; the sweep checks the electronics and the cable runs that ride rigidly on
the column and the wrist, and does not check the chains.

`kinematics.py` is the forward kinematics (where the cup and the fork are for a carriage
position and wrist angle), the fourteen poses of the cycle, and the planner that turns two
poses into a list of keyframes: retreat, raise, ordered horizontal moves, lower, approach, with
the special plans for the station and the tonearm steps. It is the same planner the concept
model animates and the one the orchestrator will run.

`assembly.py` places the parts for a state and exports a coloured STEP. `check_collisions.py`
samples every keyframe segment (20 mm and 5° by default), rebuilds the moving parts and the
pose-dependent environment (tonearm angle and lift, carousel angle, which records are where)
and reports every intersection between the Z carriage, the wrist and the held record and
anything else, with the pose, the segment and the position. `export_parts.py` writes the STL
files for printing and the sub-assembly STEP files for FreeCAD. `export_web.py` writes every rigid body in
its rest frame as one glTF plus `scene.json`, the constants the viewer in `cad-model.html` needs to assemble
and animate them; the viewer restates no dimension of its own. `render.py` tessellates the machine and rasterises
orthographic views through a depth buffer with nothing but numpy, since the container has no renderer and
no browser; the pictures in the documents come from it, and with `--animate` it samples the planner's
keyframes on the web viewer's own timeline and places every rest-frame part exactly as the viewer does
(checked: the same bounding boxes as `Machine` to the last millimetre), writing one animated PNG per size.

`export/` holds generated files. They are committed at reviewed states so the STEP files can
be opened without running anything; regenerate them after changing `params.py`.

## Coordinate system

X along the bench from the carousel towards the deck, Y across the bench with +Y towards the
front, Z up. Origin on the bench top, 200 mm left of the flip station post, on the machine's
centreline. A carriage state is the centre of the Z carriage block; the wrist pivot sits
`WRIST_X` further along +X. Wrist angle `phi` is a right-hand rotation about +X: 0 is the arm
hanging with the cup facing −Y, +90 is the cup facing down, −90 the cup facing up, 180 the arm
pointing up with the fork pointing down.

## Record sizes

Every record stands with its centre at `CAR_REC_R`, whatever its diameter, because the slot floor
of each comb is a V with its apex there; `carousel.record_z(r)` gives the centre height for a
radius. `Machine(record_r)` builds the machine with a record of that radius in slot 0, on the cup,
on the platter and on the ring, with 12" records in the other slots, and `kinematics.full_cycle(r)`
plans the cycle for it: only the pick and the return move. `Machine(load=carousel.DEMO_LOAD)` fills the
other slots with the mixed load the pictures and the viewer show (three 10", four 7", one empty slot for
the loading rule, 12" in the rest); the checker never uses it. The neighbour that matters is slot 1,
the spoke on the front side of the pick, the one the wrist descends beside; `Machine(record_r,
neighbour_r)` sets it (None leaves it empty). The checker sweeps the whole cycle with a 12" and then
the pick, the carry away from the slot and the return with a 10" beside a 12" and a 7" beside a 10",
the largest neighbours the loading rule allows; `--size 7 --neighbour 12 --poses pick` shows why the
rule exists.

## Fidelity

This is a layout model: every part has its true envelope, position and travel, the records are
real discs with holes, and the tonearm pivots about the measured point. It is not yet a print
model. The printed parts that exist as separate functions (`comb`, `hub`, `roller_bracket`,
`ring_rest`, `fork`) have their functional features; the rest of the printed parts are still
envelopes inside their sub-assembly and get detailed as the build reaches them.

## What the checker found so far

Running the checker on the first version of this model found five real problems that the
concept model had not shown, and they are fixed here: the wrist camera on the hub side of the
arm sat where the gap between spokes narrows (moved to the outer side and higher up the arm);
the cup bracket reached below the cup and met the spindle tip (raised); the end-stop pin stood
inside a 12" record's outline (moved from 60 to 45 mm from the pivot); the fork pointed through
the rear panel at the re-grip pose (shortened from 100 to 55 mm, frame widened to 86 cm); and the
swing to B-up over the deck pushed the record into the front panel (the station plan now swings
the record to vertical before moving Y). Adding the record sizes found a sixth: picking a 7" beside
a 12" puts the wrist hub 18 mm and the column's foot 7 mm into the neighbour, which no change to
the slot can fix and became the loading rule in the design decisions. At 20 mm / 5° sampling the
cycle runs with zero intersections for every size.
