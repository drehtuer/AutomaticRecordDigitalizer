# Design decisions

The machine took its shape through a review of a series of concept models. This document records what was decided, why, and what was rejected, so the reasoning survives into the CAD and software phases.

## No stacking changer

A second-hand automatic changer costs a fraction of this machine and needs no building. It was rejected because it drops each record onto the previous one, and a record playing on a stack of records is tilted, poorly supported and audibly distorted. Every other decision follows from the requirement that a record is never supported by anything but the mat, and never touched except on its label.

## Gantry, not an arm

A Cartesian gantry with one rotary wrist was chosen over an articulated arm. Linear axes give repeatable positioning for free, a 3D-printed jointed arm is hard to make stiff, and a gantry turns the whole build into a printer-shaped problem with a printer's toolchain. The wrist is the only joint and it does two jobs: turning the record from vertical to horizontal and flipping it for side B.

## Vacuum cup on the label

Early concepts gripped the rim with three fingers. That failed on two requirements: 10" and 7" records have a different rim, and shaped records ("sawblades") have no usable rim at all. The label area is the one feature common to every record, so the gripper is a single vacuum cup on the label. A label-pinch gripper (a pin through the centre hole and a jaw on the label) was considered as an alternative that needs no pump and cannot drop a record when power fails; it was set aside because the vacuum cup is simpler and the vacuum switch gives a positive confirmation of grip. 7" singles with the large jukebox hole are excluded.

## Round magazine instead of racks

The first layouts had a leaning queue for infeed and a slotted rack for outfeed, later a stepper-driven follower and a slotted comb. Each had a flaw: the queue put records face to face under pressure, the slotted rack could not accept a record with the gripper beside it at 20 mm pitch, and both needed the gantry to travel over 1.5 m. A round magazine with records as spokes solves all of it: the gap between neighbours at the label is 6.5 cm, pick and return are at one fixed position, each record goes back into its own slot, records never touch, and the X travel halved. The price is a diameter of 86 cm.

## Records rest against the outer rim

Placing records in the slots with their outer edge against a rim ring, rather than standing on the slot floor at the hub, puts every size at the same outer radius. A 7" then sits at a larger radius than it otherwise would, where the gap between spokes is wider, so the gripper fits beside it.

## Wrist axis along X

With the pick slot pointing along X, the record's face is normal to Y and the cup must approach along Y, so the wrist rotates about X and the Y axis does real work: it carries the cup onto and off the spoke and it reaches 22 cm either side of the station ring for the two station poses. This set the Y travel at about 45 cm.

## Flip via a passive ring rest

A cup on one face can never place the record with that face down; somewhere the cup must change sides. Two ways were considered: a two-cup yoke that flips in the air, and a passive ring rest that the record is set down on by its label so the cup can re-grip from the other side. The ring won because it has no moving parts, it is also the best place to photograph label B, and it costs twenty seconds per side. It was moved 12 cm off the centreline once the motion planning showed that a vertical record travelling along X would otherwise pass through it.

## Moving Z column

The first gantry had a fixed Z tower hanging from the cross beam, and it swept through the brush, the platter and the station on every X move. Replacing it with a column that slides up through a guide means nothing hangs below the carriage when it is raised, and every X move happens at a travel height that clears everything by construction.

## Fork on the wrist, opposite the arm

Hanging the finger-lift fork from the carriage either dipped it into the carousel during a pick or parked the carriage a few centimetres above the tonearm while cueing. Mounting it on the wrist hub opposite the vacuum arm means it points down exactly when the arm points up, shares the cup's Y position, and keeps the carriage well above the arm.

## The deck's own cue lever does all lifting

The turntable has a manual cue lever. A servo on a frame bracket works it, so every lift and lower of the tonearm happens on the deck's damped mechanism, and the fork only ever moves the arm sideways while it is floating. The arm cannot be dropped by the machine. The platter is stopped before every stylus placement and removal, as it would be by a careful person; the lead-in silence absorbs the spin-up.

## Inner end stop

The cue-servo bracket initially collided with the arm's inner swing. That collision became a feature: a soft-sleeved pin on the bracket stands in the arm tube's path just past the run-out radius, so whatever the software does, the stylus cannot reach the label.

## Omnitronic DD 3120, not the Stanton T.92

Two decks were available. The Omnitronic has a cue lever, a remote start/stop jack and a pitch output; the Stanton has none of these and a built-in USB converter that is not wanted. The cue lever alone decides it: without one, the machine would need its own damped arm lift, which is the part most likely to damage a record. The remote jack is a bonus that removes all soldering on the start/stop switch.

## No automatic skip recovery

A skip is detected by audio and by camera at once. The response is to lift the arm via the cue lever within half a second, stop the platter, pause the batch and notify. Re-cueing automatically was rejected because a record that skipped once will usually skip again at the same place, and an unattended retry loop grinding a stylus into a scratch is the one thing the machine must never do.

## Two cameras, placed by what they need to see

An overhead camera cannot see a label or hole past the gripper, and cannot see the label at all while the record stands in the magazine. So the label-and-hole camera rides on the wrist looking along the cup's axis and sees whatever face is about to be gripped, and the deck camera sits low at platter height facing the headshell, where it sees the stylus in profile, the groove bands edge-on and the strobe dots on the rim. A rail-top camera above the deck was tried and moved for that reason.

## 33/45 by the deck's buttons, not by resampling

Recording everything at one speed and resampling later was rejected because the phono stage applies RIAA equalisation at fixed frequencies; a record played at the wrong speed is equalised wrongly and resampling does not undo it. The deck's 33 and 45 buttons are momentary switches, so two optocouplers and a manifest column solve it properly.

## LED strobe for speed, not camera frame rate

The camera cannot imitate a 50 Hz neon strobe, but an LED pulsed at 50.000 Hz from the controller's crystal makes the deck's dot rows, or a printed strobe ring on a deck without them, show the speed error as a drift the camera can measure. It works on any turntable, and the same LED run continuously is a raking light that shows the grooves for cueing and stylus checks. The measured speed and wow are logged with each recording rather than corrected live.

## Brush on the frame, with a dust edge

The brush was first drawn clamped to the turntable's plinth. It moved to a frame bracket so the deck can be swapped or shifted without re-alignment beyond a software offset. On its return path a radial comb edge, as long as the brush, strips the dust from the bristles into a slide-out tray, so cleaning side A does not put its dust onto side B.

## Plywood frame, extrusion rails

A full aluminium extrusion frame was replaced by a glued box of 18 mm birch plywood with 2040 extrusion only where the X rails need a straight, adjustable mounting surface. The panels give more racking stiffness than a lattice with diagonals, the interior stays open, brackets screw straight to the panels, and extrusion drops from ten metres to four. Cost is about the same; the choice is about the tools the builder prefers.

## Roller ring instead of a lazy susan

The 86 cm carousel rolls on ten printed brackets with 608 bearings around a central 6005 bearing, rather than on a bought lazy-susan ring. It is cheaper, has no play in height, spreads the load, and every part of it is printable except the bearings.

## Precision where it is printed, cheapness where it is wood

The carousel disc and base plate, the frame panels and the bench top are plywood cut to a few millimetres. Every position that matters, the slot angles, the rail line, the ring rest, is carried by a printed or bought part that registers to the wood without depending on how accurately it was cut.
