# Open questions

Things the concept could not settle and that the first hardware has to answer. Each one names what to measure and what depends on it.

**The turntable's exact geometry.** The layout in the specification was measured on a top-down photo of the DD 3120 (`images/dd-3120-top.jpg`) and is good to about half a centimetre; perspective in the photo makes the outer positions the least certain. Confirm with a ruler before the CAD: spindle to pivot, pivot to arm rest, the cue lever's position and travel, and the height of the lever above the plinth. The cue-servo bracket, the end-stop pin and the fork's approach all hang on these numbers.

**Slipmat.** Replace the felt DJ slipmat with a rubber or cork mat before the first batch and check that the vacuum-cup release a few millimetres above it still centres the record on the spindle.

**The remote start/stop jack's behaviour.** Whether a closure toggles start/stop or the platter runs only while the contact is held; the macros mirror whichever it is.

**The pitch output.** What signal the DD 3120's pitch output carries: a control voltage, a tacho pulse train, or something else. A pulse train proportional to platter speed would be a second, strobe-independent speed reference for the sidecar file.

**Stylus for the archive pass.** The Ortofon DJ S is spherical and robust, which is right for commissioning and for worn records. Decide after the first batches whether an elliptical stylus is worth a second pass on the records that matter.

**Cue lever force and throw.** How much force and travel does the lever need, and does it lift the arm enough for the fork to walk it without the stylus touching a warped record? This decides whether a micro linear servo is enough or a larger one is needed, and sets the lift height the deck camera must confirm.

**Finger-lift shape.** Whether the fork's U straddles the actual finger lift cleanly across the whole arc from rest to run-out, or needs a different opening width or a slight yaw. A printed test fork on a hand-held handle answers this in an afternoon before any gantry exists.

**Cup size against 7" labels.** A 40 mm bellows cup on an 88 mm label leaves margin; confirm the seal on printed and glossy labels, on labels with embossed text, and on a shaped picture disc's centre.

**Gap at the pick slot.** 6.5 cm between spokes at the label radius against a gripper assembly of just under 5 cm. Print the wrist's cup end and camera bracket first and check it in a mock-up of three slots; if it is too tight, the fix is 22 slots at 16.4° rather than a wider carousel.

**Carousel indexing accuracy.** Whether a printed GT2 ring in eight segments indexes to within a millimetre at the rim over many revolutions, or whether the per-slot optical mark is needed for every index rather than only for homing.

**Vertical record at travel height.** The planned travel height leaves about 3 cm between a hanging 12" record and the carousel rim while it moves along X. Confirm the real rim height and the record's swing when the gantry accelerates; raise the travel height if needed.

**Deck camera view.** Whether the low, oblique view from the end panel sees the headshell over the whole arc and resolves the stylus, or wants a slightly higher mounting; and whether the raking LED at that angle shows the groove bands reliably on dark and on coloured vinyl.

**Skip detection thresholds.** The audio discontinuity and the headshell-radius jump both need thresholds that catch a skip within a second but do not fire on a loud transient or a slightly eccentric pressing. Tune on a deliberately scratched sacrificial record.

**Strobe reading on the clone's platter.** Whether the deck's dot rows are usable under the 50 Hz LED, or whether a printed strobe ring on the rim is the better reference. On a quartz-locked deck the expected result is "no drift"; the test is nudging the pitch fader and watching the number move.

**Wrist camera cable.** CSI over a cable-chain-length extender versus a USB module on the wrist. Try the USB module first; it is the smaller problem.

**Phono stage.** Whether the clone's built-in phono stage on its line output is good enough, or an external phono preamp goes between the deck and the Scarlett. Record the same side both ways and compare before deciding.

**Column height.** The raised column top at about 135 cm is fine on a bench but not under a low shelf; if headroom is short, the Z travel can be reduced by lowering the travel height for horizontal carries, at the cost of a slightly longer cycle.
