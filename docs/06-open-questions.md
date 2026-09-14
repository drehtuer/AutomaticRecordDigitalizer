# Open questions

Things the concept could not settle and that the first hardware has to answer. Each one names what to measure and what depends on it.

**The turntable's exact geometry.** The layout in the specification was measured on a top-down photo of the DD 3120 (`images/dd-3120-top.jpg`) and is good to about half a centimetre; perspective in the photo makes the outer positions the least certain. Confirm with a ruler before the CAD: spindle to pivot, pivot to arm rest, the cue lever's position and travel, and the height of the lever above the plinth. The cue-servo bracket, the end-stop pin and the fork's approach all hang on these numbers.

**Slipmat.** Replace the felt DJ slipmat with a rubber or cork mat before the first batch and check that the vacuum-cup release a few millimetres above it still centres the record on the spindle.

**The remote start/stop jack's behaviour.** Fader start suggests the platter runs while the contact is held and stops when it opens; confirm that it is not a toggle, and whether the front-panel button still works while the remote contact is closed.

**The pitch output.** What signal the DD 3120's pitch output carries: a control voltage, a tacho pulse train, or something else. A pulse train proportional to platter speed would be a second, strobe-independent speed reference for the sidecar file.

**Stylus for the archive pass.** The Ortofon DJ S is spherical and robust, which is right for commissioning and for worn records. Decide after the first batches whether an elliptical stylus is worth a second pass on the records that matter.

**Cue lever force and throw.** How much force and travel does the lever need, and does it lift the arm enough for the fork to walk it without the stylus touching a warped record? This decides whether a micro linear servo is enough or a larger one is needed, and sets the lift height the deck camera must confirm.

**Finger-lift shape.** Whether the fork's U straddles the actual finger lift cleanly across the whole arc from rest to run-out, or needs a different opening width or a slight yaw. A printed test fork on a hand-held handle answers this in an afternoon before any gantry exists.

**Cup size against 7" labels.** A 40 mm bellows cup on an 88 mm label leaves margin; confirm the seal on printed and glossy labels, on labels with embossed text, and on a shaped picture disc's centre.

**Where the `GRIP` post-condition lives.** *A decision, not a measurement — and it has to be made before anything is wired.* The bill of materials no longer buys a vacuum switch: an industrial one starts at about 95 €, against about 31 € for an Adafruit MPRLS pressure breakout. That is a cheaper part in a different place, and the difference is not the price. A switch is a digital contact on a controller end-stop input, so `GRIP` waits on it inside Klipper and a failed grip aborts within the motion queue, before the next move runs. The MPRLS is an I²C device on the Pi, so the check moves up into the orchestrator and a failed grip is caught a round trip later, with the move already queued. The choices:

- *MPRLS alone, and accept the latency.* Cheapest, one sensor, one line to tee. It also gives an actual pressure number rather than a threshold crossing, which distinguishes a weak seal from no seal and would let the machine retry a marginal grip instead of faulting. The cost is that `GRIP` stops being a Klipper macro with a hard post-condition and becomes an orchestrator step, and the abort is as fast as the Moonraker round trip, not as fast as the motion queue.
- *MPRLS for the reading, plus a cheap digital vacuum switch purely as the Klipper interlock.* Keeps the fast abort exactly as `03-electronics-and-software.md` describes it and still gets the pressure reading. Costs a second sensor, a tee in the cup line, and one more controller input.
- *A digital switch alone, as originally drawn.* No change to the design at all, at about 95 € and with no pressure reading.

What it decides: whether the cup line carries one sensor or two, whether `GRIP` is a Klipper macro or an orchestrator step, and how quickly a dropped record stops the machine. Deciding the middle option costs the least design churn; deciding the first costs the most and buys a genuinely better signal.

**Label photographs at 720p.** The wrist camera is now a USB webcam that tops out at 720p, where the plan assumed a 12 MP Camera Module 3 on both ends. That is ample for what the cycle needs — the centre hole, the label edge, the groove bands — but the label photographs also feed the follow-up project's Discogs matching, which reads catalogue numbers and small print, not just artwork. Try it on a real batch. If 720p is not enough, the cheap move first: a 1080p USB module is already on hand and can simply replace the C270 on the wrist, at the cost of autofocus that has to be locked down before every batch. If 1080p is still not enough, the answer is a static high-resolution label camera at the flip station, where the record is held still in front of it and the camera can be as heavy and as well lit as it likes, rather than a heavier camera on the moving wrist.

**The ring rest's diameter.** *A decision: the specification and the CAD disagree, and the STL follows the CAD.* The specification describes an annulus of 70 mm inner and 86 mm outer *diameter*, touching only the label; `cad/params.py` has a major *radius* of 78 mm with an 8 mm tube, so the printed ring contacts a record between 70 and 86 mm from its centre — outside the 50 mm label, on the lead-out band of a 12" and on the outermost grooves of a 7". The spec size is right about the record and tight for the arm: 5.5 mm of clearance each side through the 60° opening. A ring at 43 mm major radius with a 6 mm tube contacts at 37 to 49 mm, inside the label, with 6.5 mm a side. Whichever is chosen goes into `params.py`, through the collision sweep, and into the specification and the STL.

**Gap at the pick slot.** 65 mm between spoke faces at the arm's radius against 48 mm of cup, neck, bracket and arm, leaving 8 mm of approach and 9 mm of margin. Print the wrist's cup end first and check it in a mock-up of three slots; if it is too tight, the fix is 22 slots at 16.4° rather than a wider carousel. The camera is no longer in the gap.

**Carousel indexing accuracy.** Whether a printed GT2 ring in eight segments indexes to within a millimetre at the rim over many revolutions, or whether the per-slot optical mark is needed for every index rather than only for homing.

**Vertical record at travel height.** The planned travel height leaves about 3 cm between a hanging 12" record and the carousel rim while it moves along X. Confirm the real rim height and the record's swing when the gantry accelerates; raise the travel height if needed.

**Deck camera view.** Whether the low, oblique view from the end panel sees the headshell over the whole arc and resolves the stylus, or wants a slightly higher mounting; and whether the raking LED at that angle shows the groove bands reliably on dark and on coloured vinyl.

**Skip detection thresholds.** The audio discontinuity and the headshell-radius jump both need thresholds that catch a skip within a second but do not fire on a loud transient or a slightly eccentric pressing. Tune on a deliberately scratched sacrificial record.

**Strobe reading on the clone's platter.** Whether the deck's dot rows are usable under the 50 Hz LED, or whether a printed strobe ring on the rim is the better reference. On a quartz-locked deck the expected result is "no drift"; the test is nudging the pitch fader and watching the number move.

**Wrist camera cable.** CSI over a cable-chain-length extender versus a USB module on the wrist. Try the USB module first; it is the smaller problem.

**Phono stage.** Whether the clone's built-in phono stage on its line output is good enough, or an external phono preamp goes between the deck and the Scarlett. Record the same side both ways and compare before deciding.

**Column height.** The raised column top at about 135 cm is fine on a bench but not under a low shelf; if headroom is short, the Z travel can be reduced by lowering the travel height for horizontal carries, at the cost of a slightly longer cycle.

**V-wheel play on X.** With Delrin wheels on V-slot the carriages must be adjusted with their eccentric spacers until there is no rock and no binding over the whole 1.3 m; check that the cup's position at the pick slot repeats to within half a millimetre after a full X traverse, and fall back to a rail on X if it does not.

**Pick without a camera.** The pick relies on the record's centre being within about a millimetre of its nominal position when it rests against the rim ring. Check this on the printed combs and rim with a 12", a 10" and a 7": if a size sits further off, the wrist camera can take one look from above the slot before the arm descends, at the cost of a few seconds.

**Spindle in the cup.** The spindle tip enters the hollow bellows cup by about 10 mm when a record is released 3 mm above the mat. Confirm the cup's inner depth allows that with the chosen cup; otherwise release from a little higher.
