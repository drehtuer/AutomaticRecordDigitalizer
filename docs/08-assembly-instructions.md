# Assembly instructions

How the machine goes together, in the order it has to, with every part named: bought, printed, cut from plywood, picked up at the Baumarkt, or already on hand. Dimensions come from `../cad/params.py`, which is the authority; where this document gives a number, that is where it came from. Nothing here has been built yet, so treat the sequence as a plan to be corrected on the first pass and written back.

Read `07-status-and-next-steps.md` first. It front-loads the things that can still change the design — measuring the deck, printing the three parts that decide the geometry — and none of the work below should start before those are done. Four decisions in `06-open-questions.md` also bear on this document and are called out where they land: where the `GRIP` check lives, the ring rest's real diameter, the size of the electronics box, and where the Raspberry Pi sits.

## Already on hand

Nothing in this table is bought. Everything in it has a place in the build.

| Item | Goes | Notes |
|---|---|---|
| Omnitronic DD 3120 turntable | On the bench under the deck end of the frame | Swap the felt slipmat for rubber or cork before the first record. The Stanton T.92 USB stays a spare and is not used |
| Ortofon DJ S cartridge | On the deck's headshell | Spherical, tracks at about 3 g; the right stylus for commissioning |
| Focusrite Scarlett | Beside the deck | USB to the powered hub, not to the Pi. The deck's line output feeds it; the Scarlett has no phono input |
| Conrad 393905 USB relay card | In the electronics box, or with the Pi if the Pi moves to the deck end | Channel 1 to the deck's remote jack, channels 2 and 3 across the 33 and 45 buttons |
| 2 × Raspberry Pi 4B rev 1.1, 2 GB, with 15 W supplies and 32 GB cards | One runs the machine; the other is the cold spare, kept boxed | rev 1.1 refuses e-marked USB-C cables: use the official supply. The card holds the OS only, never a recording |
| External USB 3.0 SSD | With the Pi | Every WAV goes here. About 860 MB per side, about 40 GB per full magazine |
| Self-powered USB 3.0 hub | With the Pi | The Scarlett, the SSD, the wrist camera and the relay card all hang off it; the Pi's own ports budget about 1.2 A across all four |
| Logitech C270 webcam | On the wrist | The wrist camera. Fixed focus, set once by hand at the working distance over a label, then focus, exposure, gain and white balance locked |
| 1080p USB webcam | Kept | The first fallback if 720p label photographs turn out not to be enough for tagging |
| 3D printer | Prints every part in the printed-parts table | PETG for structure, TPU wherever a record is touched |

## Plywood

Everything is 18 mm birch plywood. None of the cuts needs to be better than a few millimetres — every position that matters is carried by a printed or bought part that registers to the wood — but the carousel disc wants to be flat, so take it from the middle of a sheet, not an edge that has been standing in a corner.

| Piece | Size (mm) | Qty | Cut-outs |
|---|---|---|---|
| Side panel | 1210 × 830 | 2 | Two windows, each about 420 × 570, leaving a 120 mm strip along the bottom, a 140 mm strip along the top, 120 mm posts at both ends and one at 380 mm from the carousel end |
| End panel | 842 × 830 | 1 | One window about 620 × 570, same strips, 120 mm posts at both sides. 842 is the width between the side panels' inner faces; it sits between them, at the deck end |
| Carousel disc | Ø 860 | 1 | Ø 26 hole at the centre for the stub shaft bore of the printed hub. Cut with a jigsaw against a trammel; rough is fine, the printed rim and combs carry the geometry |
| Carousel base plate | Ø 880 | 1 | The stub shaft and ten roller brackets bolt to it; a Ø 25 hole at the centre if the shaft is through-bolted |
| Bench top | 1900 × 1000 | 1 | Only if there is no bench. An existing bench of about that size does the job |

**Sheets.** This does not come out of one sheet, whatever the earlier bill of materials said. On a 1500 × 3000 sheet the two side panels stack (1210 × 1660) with the end panel below them (842 × 830) — that is sheet one, with a 290 mm strip left over. The two discs need 880 × 1740 between them and fill most of sheet two; a bench top is a third sheet, or spruce, or the bench that is already there. Have the shop cut the sheets into the rectangles at least; the windows and the discs are jigsaw work at home.

**Windows.** Drill a starter hole in each corner, jigsaw between them, and do not bother with a clean edge: the windows exist so the interior stays open, and nothing registers to them. Sand the edges where hands will go.

## Baumarkt

What the bill of materials leaves to a local shop, on top of the plywood.

- Wood glue, D3, one 250 g bottle. The frame is a glued box; the screws are clamps.
- Wood screws: 4 × 40 mm, about 40, for the panel joints and the beam blocks; 3.5 × 25 mm, about 60, for printed parts onto plywood; 3.5 × 16 mm, about 40, for the roller brackets and small brackets. Countersunk, Torx.
- Sanding: 80 and 120 grit, one sheet each; a block.
- Four rubber feet or adjustable levelling feet for the carousel base plate, so it stands flat on a bench that is not.
- Self-adhesive felt, about 1 m of 20 mm strip, to line the tops of the combs where a record's edge sits — or print those in TPU and skip the felt.
- Cable ties, 100 × 2.5 mm, one bag; and a few cable tie mounts with adhesive backs.
- Fabric or Kapton tape for holding cable bundles in the chains while they are dressed.
- Double-sided tape or hook-and-loop for the Pi and relay card if they are not screwed down.
- A rubber or cork turntable mat if the deck's felt slipmat is the only one there.
- Optional: a small can of clear wax or oil for the plywood, and a 40 mm hole saw for the cable exits through the panels.

Tools, if they are not there already: a jigsaw with a wood blade, a cordless drill with a 4 mm and an 8 mm wood bit and a countersink, a long straightedge and a square, four clamps of at least 90 cm reach or strap clamps, hex keys 2 to 5 mm, a set of small spanners, a soldering iron, a crimp tool for Dupont and JST-SM contacts, a heat gun for the shrink tube, digital calipers, and a spirit level.

## Printed parts

PETG unless marked TPU. The CAD marks which parts have their functional features and which are still envelopes to be detailed as the build reaches them; do not print an envelope. Print the geometry-deciding parts first, as `07-status-and-next-steps.md` says: the fork, the cup bracket and three combs with a hub, before any frame exists.

| Assembly | Part | Qty | Material | In the CAD |
|---|---|---|---|---|
| Carousel | Centre hub, 24 comb sockets and the 25 mm shaft bore | 1 | PETG | Print-ready |
| Carousel | Slot comb, with the 5 mm locating slot on top | 24 | PETG, or TPU top | Print-ready |
| Carousel | Rim ring segment, 45° each | 8 | PETG | Envelope |
| Carousel | GT2 tooth-ring segment, dovetailed, 45° each | 8 | PETG | Envelope |
| Carousel | Roller bracket for one 608 bearing | 10 | PETG | Print-ready |
| Carousel | Index stepper mount with the 20T pulley position | 1 | PETG | Envelope |
| Carousel | Home-mark flag and the slot-sensor mount | 1 + 1 | PETG | Envelope |
| Gantry | X carriage V-wheel plate, 4 wheels each | 2 | PETG, or the donor's aluminium plates | Envelope |
| Gantry | Cross-beam end bracket, joins the cross beam to each X plate | 2 | PETG | Envelope |
| Gantry | X motor mount and the two belt idler mounts | 1 + 2 | PETG | Envelope |
| Gantry | Y wheel plate under the guide block, 4 wheels | 1 | PETG | Envelope |
| Gantry | Z guide block, rides the Y plate, carries the Z motor and the column's guide | 1 | PETG | Envelope |
| Gantry | Z carriage block with the 90 mm outrigger | 1 | PETG | Envelope |
| Gantry | Lead-screw nut holder | 1 | PETG | Envelope |
| Gantry | Column end caps | 2 | PETG | Envelope |
| Gantry | Cable-chain end brackets, X, Y and Z | 6 | PETG | Envelope |
| Wrist | Hub with the bearing seats and the stepper coupling | 1 | PETG | Envelope |
| Wrist | Arm, 220 mm, with the cup bracket at its end | 1 | PETG | Envelope |
| Wrist | Cup bracket, kept above the cup so the spindle tip meets nothing | 1 | PETG | Envelope |
| Wrist | Hose clips along the arm | 3 | PETG | Envelope |
| Wrist | Wrist camera mount, outer side of the arm, 110 mm up | 1 | PETG | Envelope |
| Wrist | Finger-lift fork, 55 mm, with prongs 28 mm apart | 1 | PETG | Print-ready |
| Wrist | Fork lining | 1 | TPU | To be added to the fork |
| Wrist | Hall sensor mount at the hub | 1 | PETG | Envelope |
| Station | Ring rest, with the pad groove on top | 1 | PETG | Print-ready, at the CAD's diameter — see the decision below |
| Station | Ring rest pads | 3 | TPU | — |
| Station | Post bracket onto the electronics box | 1 | PETG | Envelope |
| Station | Electronics box, or a bought enclosure | 1 | PETG or bought | Envelope, and too small — see the decision below |
| Deck interface | Cue-servo bracket for the MG996R on the end panel | 1 | PETG | Envelope, drawn for a linear servo |
| Deck interface | Pusher rod guide | 1 | PETG | Envelope |
| Deck interface | Lever pad on the rod's end | 1 | PETG or TPU | Envelope |
| Deck interface | End-stop bar and pin base | 1 | PETG | Envelope |
| Deck interface | End-stop pin sleeve | 1 | TPU | — |
| Cameras and light | Deck camera bracket on the end panel | 1 | PETG | Envelope |
| Cameras and light | LED bar housing | 1 | PETG | Envelope |

About 30 distinct parts and 50 to 70 hours of printing. The 24 combs and 10 roller brackets are the bulk of it and are also the ones to print first, because the carousel is the one sub-assembly that can be built and tested before anything else exists.

## Assembly order

Each sub-assembly is built and checked on its own before it meets the next. The order is the order of dependence: the carousel needs nothing else; the frame needs nothing else; the gantry needs the frame; the wrist needs the gantry; everything electrical needs everything mechanical to be where it will stay.

### 1. Carousel

Bolt the stub shaft to the centre of the base plate, upright, and press the 6005 bearing onto it. Screw the ten roller brackets to the base plate on a 720 mm circle, 36° apart, each with its 608 bearing on an M4 axle, all pointing radially; a paper template printed at 1:1 puts them close enough, because the disc only rests on them. Stand the base plate on its feet and level it.

Drill the Ø 26 hole in the centre of the disc. Screw the hub to the top of the disc, centred on the hole, and lower the disc onto the shaft so the hub's bore takes the bearing. Spin it: it should turn on the rollers with no rock. If it rocks, one roller bracket is high; a washer under its neighbours fixes it.

Push the 24 combs into the hub's sockets, then fit the eight rim segments so that each comb's outer end seats in its rim tab; the hub and the rim between them set the 15° pitch, and the comb slots set the record plane. Fit the eight tooth-ring segments to the underside of the disc, dovetails engaged, on the 215 mm radius. Screw the index stepper mount to the base plate at the tooth ring's edge, with the geared NEMA17 and its 20T pulley meshing the ring, and fit the home-mark flag on the disc and the slot sensor on the base plate so the flag passes through it once per turn.

Stand three records in three adjacent slots and check the gap at the label radius with a ruler: about 65 mm between faces. If it is less, `06-open-questions.md` has the fallback.

### 2. Frame

Glue and screw the two side panels to the end panel, end panel between the sides, square on the bench top. Clamp, check the diagonals, let the glue cure. Screw a block of plywood offcut into each of the three lower corners as a foot if the bench is not flat.

Bolt a 1290 mm 2040 V-slot beam along the top edge of each side panel with its 40 mm face vertical and the slot facing the other beam, overhanging the open carousel end by 80 mm, using M5 bolts through the panel into T-nuts. Shim until the two beams are parallel and in one plane — this is the one alignment that matters on the whole frame, because the X carriages ride in these slots; a long straightedge across both beams, checked at three points, is the test. Bolt the 2020 tie across the open end, 880 mm long over the beams, so they stay parallel under load.

### 3. X axis

Build the two X carriage plates: four Delrin V-wheels each, two on fixed spacers and two on eccentrics, so the plate can be pinched onto the beam. Set each plate on its beam and adjust the eccentrics until it rolls the full 1290 mm with no rock and no binding. Join the plates with the 940 mm 2040 cross beam through the end brackets. The cross beam is 940 because the frame is 860 wide over the panels and the plates sit on the beams outside them; an 800 mm beam, which is what the concept had, does not reach.

Fit the X motor on one end bracket, an idler on the other, and run the GT2 belt along the outside of one X beam: fixed at both beam ends, wrapped round the motor pulley and its idler on the carriage. Tension by hand until it hums when plucked. Fit the X end-stop at the deck end of the beam.

### 4. Y axis

Build the Y wheel plate — four wheels, two eccentric — and set it on the cross beam. Screw the Z guide block to it. Fit the Y motor on one end bracket of the cross beam, an idler at the other, and run the belt fixed at both ends of the cross beam, round the pulley and idler on the Y plate. Fit the Y end-stop on the cross beam at the rear.

The planner uses 625 mm of Y travel, not the 45 cm the concept assumed: the re-grip poses reach from −340 mm to +285 mm. With 80 mm plates at both ends and an 80 mm guide block, the 940 mm cross beam gives about 700 mm, so it fits, but it means the Y cables need a chain of their own along the cross beam, not a loop.

### 5. Z column

Bolt the 800 mm MGN12 rail to the 760 mm column and its carriage into the guide block, so the column slides through the block. Fit the KFL08 bearing at the top of the column, the lead-screw nut holder on the guide block, and the T8 screw through them, coupled to the Z motor on the guide block. The column carries the screw; the nut is fixed; turning the screw lifts the column. Fit the end caps, and the Z end-stop on the guide block so the column trips it at its top. The cycle uses 430 mm of Z; the screw and rail have room for 600.

### 6. Wrist

Bolt the Z carriage block to the bottom of the column and the wrist hub to the end of its 90 mm outrigger, on the +X side, with the geared NEMA17 driving the hub through the coupling. Fit the arm to the hub pointing down, the cup bracket at its end, the bellows cup on its neck facing −Y, and the fork on the hub opposite the arm, pointing up. Fit the camera mount 110 mm up the arm on the +X side and the C270 in it, looking along the cup's axis. Fit the Hall sensor at the hub and its magnet on the arm at the hanging position.

Before the wrist goes on the machine, test the cup end by hand: 12", 10", 7" and a picture disc, held by their labels with a hand pump. Test the fork on a handle against the real headshell's finger lift. Both are in `07-status-and-next-steps.md` as the first things to print, and both have to pass before the frame is worth building.

### 7. Flip station

The ring rest stands on a post that stands on the electronics box, at X = 200 mm, Y = −120 mm, Z = 300 mm, with its 60° opening towards the front. Screw the post bracket to the box, the post to the bracket, the horizontal arm to the post so it runs under the ring and never touches a record on it, and the ring to the riser. Stick the three TPU pads into the groove on top of the ring.

**Decision needed: the ring's diameter.** The specification describes an annulus of 70 mm inner and 86 mm outer *diameter*, so that it touches nothing but the label; the CAD, and the STL in `../cad/export/`, have a major *radius* of 78 mm, so the ring contacts a record between 70 and 86 mm from its centre — outside the 50 mm label, on the lead-out band of a 12" and on the outermost grooves of a 7". One of the two is wrong and it decides what gets printed. The spec size leaves the 24 mm arm only 5.5 mm of clearance each side through the 60° opening; a ring at 43 mm major radius with a 6 mm tube would contact at 37 to 49 mm, inside the label, with 6.5 mm a side. Whichever is chosen goes into `../cad/params.py`, through the collision sweep, and back into `01-design-specification.md`.

**Decision needed: the box.** At 260 × 180 × 90 mm the box under the station cannot hold what `01-design-specification.md` puts in it. The Octopus is 160 × 110 and the 150 W supply 159 × 97; side by side they need 319 mm, stacked 207, and the box offers 260 by 180 — and that is before the Pi, the relay card, the pump, the valve and the hub, whose footprints add up to 116 % of the floor on their own. Either the box grows to about 360 × 260 × 110, which there is room for towards the rear panel, or the supply and the pump leave it: the supply under the bench, where it also gets air, and the pump on a rubber mount outside the box, where its vibration is not next to the Pi. The second is the better machine. The box's size is a parameter in `../cad/params.py` and the post stands on it, so this too goes through the sweep.

### 8. Deck interface

Set the deck on the bench inside the frame with its spindle at X = 550, Y = 0, and screw a plywood stop against two of its feet so it goes back to the same place after every lift-out. Measure everything `07-status-and-next-steps.md` says to measure before this point; the bracket positions below depend on those numbers.

Screw the cue-servo bracket to the inside of the end panel at the cue lever's height, with the MG996R in it and the pusher rod through its guide so the rod's pad meets the lever's tip along X. The servo's horn drives the rod through a short link; the rod's travel is the lever's travel plus a few millimetres, and its end stop is the bracket, so the servo can never push the lever past its own stop. Screw the end-stop bar to the same bracket so it runs in front of the arm base and under the arm, with the TPU-sleeved pin standing 45 mm from the arm pivot; with the arm swung by hand, the tube must meet the sleeve before the stylus reaches a radius of about 53 mm.

Screw the deck camera bracket low on the end panel at platter height, 30 mm inside the panel, 20 mm to the front, 155 mm up, facing the headshell across the platter, with the LED bar housing beside it aimed low across the platter surface. Run the Camera Module 3 ribbon and the LED wires out through a hole in the panel.

Plug the 6.3 mm mono cable into the deck's remote start/stop jack. Open the deck, find the 33 and 45 button switches on the front-left board, measure the voltage across each with the deck on, and solder two thin wires across each switch's legs, led out through the case under the board. Close the deck. Nothing else in it is touched.

### 9. Electronics

Mount in the box, or wherever the box decision puts them: the 24 V supply with mains in through a fused, earthed inlet; the Octopus, on standoffs, fed 24 V; the 24 V to 12 V buck for the pump, the valve and the LED bar, since the bill of materials has a 24 V supply and a 5 V buck and nothing in between while all three of those loads are 12 V; the 24 V to 5 V buck for the servo alone — never the Pi, because an MG996R stalls at about 2.5 A; the pump and the direct-acting valve on the vacuum line, with the tee for the MPRLS. The MPRLS is an I²C device and stays within 30 cm of the Pi on the line at the valve, not out on the wrist.

The Pi with its own 15 W supply, the powered hub, the SSD, the relay card and the Scarlett form a second group that talks to the first only through the Pi's USB cable to the Octopus. Where that group lives is the last open decision, and the deck camera decides it — see the cable lengths below.

Wire the five TMC2209 sticks into the Octopus with UART jumpers set, X, Y, Z, wrist and carousel in that order; the servo to the servo header; the pump, valve and LED to three fan or heater MOSFET outputs, the LED on a hardware PWM pin; every end-stop, the Hall sensor and the slot sensor to end-stop inputs. Set the TMC run currents in `printer.cfg` and nowhere else.

### 10. Cabling

Three cable chains, 10 × 20 mm, R28, not two: the concept drew one along the X beam and one along the column and forgot that the Y carriage moves 625 mm along the cross beam. The chain lengths below are half the travel plus the bend allowance plus 150 mm for the mounts, rounded up; the 3 m bought covers all three with a metre spare.

| Chain | Runs along | Travel it covers | Length |
|---|---|---|---|
| X | The rear X beam, fixed end at mid-travel | 857 mm | 700 mm |
| Y | The cross beam, fixed end at the X plate | 625 mm | 600 mm |
| Z | The column, fixed end at the guide block | up to 600 mm | 600 mm |

Everything to the gantry leaves the box, climbs the rear panel to the beam, enters the X chain, crosses to the Y chain on the cross beam, and, for anything on the column or the wrist, enters the Z chain. Dress each chain with its cables laid flat and not crossing, the vacuum hose on the outside of the bend, and a cable tie at each chain end only — nothing tied inside the chain.

**Cable lengths.** Each length is the routed path from the box exit, at the top rear corner of the box, to the device, with 15 % added and rounded up to the next 10 cm. The rule is that a cable which turns out too long is fixed with a cable tie and a cable which turns out too short is a new cable, so every number here errs long, and the loop that results is dressed into the chain. Where the bill of materials already names a length, the verdict says whether it reaches.

| Cable | Route | Buy | In the BOM | Verdict |
|---|---|---|---|---|
| Vacuum hose, pump to cup, 6 × 4 PU | Box, X chain, Y chain, Z chain, arm to the cup neck, plus about 0.4 m of plumbing in the box | 4.8 m | 5 m | Reaches with 20 cm to spare; buy 6 m, it costs a euro |
| Wrist camera USB, C270 | Same path to the camera mount, 110 mm up the arm | 4.2 m | The C270's fixed 1.5 m | Does not reach. Add a 3 m USB 2.0 A-to-A extension; 4.5 m total is under the 5 m passive limit |
| Wrist stepper, 4-core | Same path to the outrigger | 4.0 m | Motor lead, about 1 m | Does not reach. 3 m extension |
| Wrist Hall sensor, 3-core | Same | 4.0 m | Bare module | 4 m of 3-core |
| Z stepper, 4-core | To the guide block on the Y carriage | 3.1 m | Motor lead, about 1 m | 2 m extension |
| Z end-stop, 3-core | Same | 3.1 m | 0.5 m lead | 2.6 m extension |
| Y stepper, 4-core | To the cross-beam end on the X carriage | 2.2 m | Motor lead, about 1 m | 1.2 m extension |
| Y end-stop, 3-core | Same | 2.2 m | 0.5 m lead | 1.7 m extension |
| X stepper, 4-core | To the X carriage | 2.2 m | Motor lead, about 1 m | 1.2 m extension |
| X end-stop, 3-core | Fixed at the deck end of the X beam | 1.9 m | 0.5 m lead | 1.4 m extension |
| Deck camera CSI ribbon | Box to the end panel, 1.07 m routed | 1.3 m | 0.5 m | **Does not reach, by half.** See below |
| LED bar, 2-core 12 V | Same | 1.3 m | Strip only | 1.3 m of 2-core |
| Cue servo, 3-core 5 V | Box to the end panel at lever height | 1.1 m | MG996R lead, 0.3 m | 0.8 m extension |
| Carousel stepper, 4-core | Box to the base plate at the carousel's far side | 1.8 m | Motor lead, about 1 m | 0.8 m extension |
| Carousel home sensor, 3-core | Same | 1.8 m | Bare module | 1.8 m of 3-core |
| Deck remote start/stop, 6.3 mm | Relay card to the deck's rear jack | 0.6 m | 1.8 m | Reaches with 1.2 m to tie up |
| 33 and 45 button taps, 2 × 2-core thin | Relay card into the deck's front-left board | 1.0 m each | Thin wire | 2 m of thin 2-core |

The extensions add up to about 12 m of 4-core for the steppers, 12 m of 3-core for the sensors and the servo, 1.3 m of 2-core for the LED, 2 m of thin 2-core for the buttons, one 3 m USB extension and one longer camera ribbon. Silicone 20 AWG is the right wire for the steppers and the servo; the sensors can take 24 AWG.

**The deck camera decides where the Pi lives.** The box under the station is 1.07 m from the camera on the end panel by the shortest sensible route, and CSI ribbons over a metre are at the edge of what a Camera Module 3 tolerates. There are two clean answers. A 1.3 m ribbon, which exists, works in most builds and is the cheaper try. Or the Pi and its whole USB group — the hub, the SSD, the Scarlett, the relay card — move to a small enclosure on the deck-end panel, which is where three of those four want to be anyway: the Scarlett is next to the deck, the relay card's cables go into the deck, and the ribbon becomes the 0.5 m already bought. Only the Pi-to-Octopus USB cable and the MPRLS I²C lead then cross from the deck end to the station box, and neither minds a metre. The second answer is the better machine; it costs one more enclosure and a longer I²C lead. Decide before drilling the panel.

### 11. Power-up and commissioning

Power the Octopus alone first, no motors connected, and flash Klipper. Connect one stepper at a time and jog it a few millimetres in each direction at low current before connecting the next; a stepper wired backwards is found here and nowhere worse. Home each axis by hand against its end-stop and set the soft limits in `printer.cfg` from what the ruler says, not from the CAD, then confirm that the Z hard limit stops the column above its lowest working height.

Power the Pi from its own supply, with the hub, and bring up Moonraker, the orchestrator and the web interface. Calibrate the datums through the interface with the cameras live, in this order: the pick slot's centre, the spindle, the ring rest, the arm pivot, and the arm's rest, lead-in and run-out angles for the deck as measured. Run the cycle in step-through mode with no record, then with a sacrificial record, then with a good one, and only then a batch.

The collision sweep in `../cad/check_collisions.py` runs against the CAD, not the machine. Every number that a ruler changed on the real deck goes into `../cad/params.py` first, the sweep runs, and only a clean sweep is allowed to become a soft limit.
