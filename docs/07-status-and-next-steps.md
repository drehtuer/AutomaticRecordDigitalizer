# Status and next steps

Written 6 September 2026, at the end of the concept phase.

## Where the project stands

The concept is complete and has been reviewed step by step against an interactive model (`concept-model.html`) that plans every motion of the cycle as waypoints. Every subsystem has a defined mechanism, every step of the cycle has a defined sequence, and every decision and rejected alternative is written down in `05-design-decisions.md`. Nothing has been bought, cut or printed. There is no CAD and no code yet.

The machine, in its final concept form: a 24-slot carousel magazine with records standing as spokes; a plywood box frame carrying an XYZ gantry on V-slot with a rotary wrist; a single vacuum cup on the label as the gripper, with a camera and a finger-lift fork on the same wrist; a passive ring rest for the side-B flip and the label photos; the Omnitronic DD 3120 as the deck, worked through its remote start/stop jack, its 33/45 buttons and its cue lever; a second camera and a 50 Hz LED strobe facing the headshell; Klipper on a printer mainboard for motion, a Raspberry Pi 5 for orchestration, vision, the web interface and recording through the Focusrite Scarlett. No brush; records are cleaned by hand before loading. No automatic recovery from a skip; the arm lifts, the platter stops, and the machine waits.

## Decisions taken during the review, in order

The stacking changer was rejected for distortion; a gantry was chosen over an arm; the rim gripper gave way to a vacuum cup on the label so that 10", 7" and shaped records work; the linear infeed and outfeed racks gave way to a round magazine with the record returning to its own slot; the wrist axis turned to X so the cup approaches a spoke along Y; the flip became a passive ring rest off the centreline; the Z tower became a moving column; the fork moved onto the wrist opposite the cup; the label camera moved onto the wrist and the deck camera down to platter height facing the headshell; the deck's own cue lever, worked by a servo, took over all lifting, with the platter stopped for every placement and removal; the servo bracket gained an end-stop pin so the stylus can never reach the label; speed is set by the deck's buttons, not by resampling, because of RIAA; a crystal-timed LED strobe measures platter speed on any deck; the aluminium frame became plywood with V-slot beams; the lazy susan became a roller ring of 608 bearings; the brush module was dropped; an automatic turntable was rejected because of locked grooves, inside-out sides and non-standard start and end positions; V-slot replaced linear rails on X and Y; a used printer became the intended parts source; the deck's start/stop jack and speed buttons are switched by the Conrad USB relay card already on hand; the MIMXRT1010-EVK was ruled out as a Klipper MCU.

## Already on hand

The Omnitronic DD 3120 (and a Stanton T.92 USB as spare), the Focusrite Scarlett, the Conrad Components 393905 USB relay card, an Ortofon DJ S cartridge. Not yet: a 3D printer, a Raspberry Pi, cameras, motors, extrusion, a controller board.

## What to buy and do first

The order below front-loads the things that could still change the design, so that nothing expensive is bought on an assumption.

First, measure the DD 3120 with a ruler and record the numbers in `01-design-specification.md`: spindle to arm pivot, pivot to arm rest, the cue lever's position, travel and force, the lever's height above the plinth, the finger lift's shape. Check the remote jack's behaviour (held or toggle) with a paper clip, measure the voltage across the 33 and 45 switches, find out what the pitch output carries, and swap the felt slipmat for a rubber or cork mat.

Second, buy the 3D printer, since it is needed for everything after this point, and then a used donor printer (CR-10 class preferred) for motors, PSU, wheels, belts and a possible controller board.

Third, print and test the three parts that decide the geometry before any frame exists: the finger-lift fork on a hand-held handle against the real headshell; the vacuum cup bracket with a hand pump against 12", 10", 7" and picture-disc labels; and three carousel combs with the hub and rim segments to confirm the 6.5 cm gap takes the wrist assembly. A Raspberry Pi with one camera can be set up in parallel to prove hole and groove-band detection on a record lying on a table.

Fourth, the parametric CAD (OpenSCAD or CadQuery), starting from the measured deck and the tested gripper, then the frame panels, the gantry, the carousel.

Fifth, the software, which can begin before the machine is complete: the Klipper configuration and macros, the orchestrator's state machine and motion planner (the same one the concept model uses), the vision routines, and the web interface with the batch manifest. The step-through mode of the web interface is the commissioning tool.

## Repository

The `concept-design` branch holds the concept phase; `main` has only the initialising commit. The branch is meant to be pushed and merged through a pull request once the concept is accepted.
