# Open questions

Things the concept could not settle and that the first hardware has to answer. Each one names what to measure and what depends on it.

**The turntable's exact geometry.** Measured on the deck itself: the outline, 44.9 × 35.1 × 8.6 cm from the feet to the case top; the platter, 1.8 cm above the case; the spindle, 17.9 cm from the left edge and 17.4 cm from the rear; the arm pivot, 6.95 cm from the right edge and 9.35 cm from the rear; and the cue lever's top, 4 cm from the right edge, travelling from 14.6 to 12.2 cm from the rear edge as it lifts. The photo had every one of these off by 5 to 20 mm, so what is still taken from it (`images/dd-3120-top.jpg`) should be trusted to a centimetre or two and no better. Still to measure: the arm rest's position, the heights above the case of the arm tube, the lever's top and the finger lift, and the finger lift's shape. The servo's yoke, the end-stop pin and the fork's approach hang on these numbers.

**Whether the re-grip earns its keep.** The flip station is the one place a record is set down and picked up again with nothing centring it, and the decision log keeps it on the condition that it works. Count, over the first batches, how often the re-grip fails to find the hole or to seal, and how often a record on the ring is off its nominal centre by more than the cup's bellows absorb. If it is often, the one-side mode in `02-operating-cycle.md` is the machine's mode and the station comes off; if it is rare, the station stays and the mode remains the fallback.

**Slipmat.** Replace the felt DJ slipmat with a rubber or cork mat before the first batch and check that the vacuum-cup release a few millimetres above it still centres the record on the spindle. The Baumarkt sheet prices a 4 mm cork sheet to cut the mat from, where the CAD assumes a 3 mm mat (`MAT_T` in `cad/params.py`): either set `MAT_T` to the mat actually fitted and rerun the collision sweep, or buy a 3 mm rubber mat.

**The remote start/stop jack's behaviour.** Fader start suggests the platter runs while the contact is held and stops when it opens; confirm that it is not a toggle, and whether the front-panel button still works while the remote contact is closed.

**The pitch output.** What signal the DD 3120's pitch output carries: a control voltage, a tacho pulse train, or something else. A pulse train proportional to platter speed would be a second, strobe-independent speed reference for the sidecar file.

**Stylus for the archive pass.** The Ortofon DJ S is spherical and robust, which is right for commissioning and for worn records. Decide after the first batches whether an elliptical stylus is worth a second pass on the records that matter.

**Cue lever force and lift.** The throw is measured: the lever's top moves 24 mm front to back. Still open: how much force it takes, whether the lever stays where it is put in both positions or springs back from one, how high its top stands above the case, and whether it lifts the arm enough for the fork to walk it without the stylus touching a warped record. The MG996R has torque to spare and its yoke carries the lever both ways, so none of the answers changes the mechanism; they set the yoke's height and slot, the horn angles for up and down, and the lift height the deck camera must confirm. The top of a pivoting lever also moves in an arc, so the yoke's slot has to allow for its rise and fall over the stroke.

**Where the end stop really stands.** The pin is drawn on the arm tube's centre line at the angle where the stylus is 53 mm from the spindle, but the tube is drawn 11 mm thick and the pin's sleeve 18 mm, and the real arm is an S, not the straight tube of the model. Drawn as it is, the straight tube would meet the sleeve with the stylus still about 12 cm out. The pin's place has to be found on the deck, with the arm swung by hand to the run-out groove, and put back into `cad/params.py`. It also has to stay in the narrow gap between the platter's rim and the arm base, about 2 cm in the model.

**Finger-lift shape.** Whether the fork's U straddles the actual finger lift cleanly across the whole arc from rest to run-out, or needs a different opening width or a slight yaw. A printed test fork on a hand-held handle answers this in an afternoon before any gantry exists.

**Cup size against 7" labels.** A 40 mm bellows cup on an 88 mm label leaves margin; confirm the seal on printed and glossy labels, on labels with embossed text, and on a shaped picture disc's centre.

**What catches a mis-loaded magazine.** A record's identity comes from the manifest the user fills in at loading, not from the label photograph, so nothing the machine measures checks that slot 7 actually holds the record its manifest line names; a slip while loading produces a recording labelled confidently and wrongly. The planned answer is a per-side review screen that shows the label photograph beside the manifest text. Try it on the first batches: is a glance at a 720p photograph enough to catch a swapped record, how long does reviewing a full magazine take, and does anything cheaper, such as flagging sides whose label photo looks unlike the one stored for that release, earn its keep.

**Gap at the pick slot.** 65 mm between spoke faces at the arm's radius against 48 mm of cup, neck, bracket and arm, leaving 8 mm of approach and 9 mm of margin. Print the wrist's cup end first and check it in a mock-up of three slots; if it is too tight, the fix is 22 slots at 16.4° rather than a wider carousel. The camera is no longer in the gap.

**Carousel indexing accuracy.** Whether a printed GT2 ring in eight segments indexes to within a millimetre at the rim over many revolutions, or whether the per-slot optical mark is needed for every index rather than only for homing.

**Vertical record at travel height.** The planned travel height leaves about 5 cm between the lower edge of a hanging 12" record and the tops of the carousel's combs while it moves along X. Confirm the record's swing when the gantry accelerates; raise the travel height if needed.

**Deck camera view.** Whether the low, oblique view from the end panel sees the headshell over the whole arc and resolves the stylus, or wants a slightly higher mounting; and whether the raking LED at that angle shows the groove bands reliably on dark and on coloured vinyl.

**Skip detection thresholds.** The audio discontinuity and the headshell-radius jump both need thresholds that catch a skip within a second but do not fire on a loud transient or a slightly eccentric pressing. Tune on a deliberately scratched sacrificial record.

**Strobe reading on the clone's platter.** Whether the deck's dot rows are usable under the 50 Hz LED, or whether a printed strobe ring on the rim is the better reference. On a quartz-locked deck the expected result is "no drift"; the test is nudging the pitch fader and watching the number move.

**Phono stage.** Whether the clone's built-in phono stage on its line output is good enough, or an external phono preamp goes between the deck and the Scarlett. Record the same side both ways and compare before deciding.

**Column height.** The raised column top at about 135 cm is fine on a bench but not under a low shelf; if headroom is short, the Z travel can be reduced by lowering the travel height for horizontal carries, at the cost of a slightly longer cycle.

**V-wheel play on X.** With Delrin wheels on V-slot the carriages must be adjusted with their eccentric spacers until there is no rock and no binding over the whole 1.3 m; check that the cup's position at the pick slot repeats to within half a millimetre after a full X traverse, and fall back to a rail on X if it does not.

**Pick without a camera.** The pick relies on the record's centre being within about a millimetre of its nominal position when it has rolled to the apex of the V in its comb. Check this on a printed comb with a 12", a 10" and a 7": drop each into the slot anywhere along its length and measure where it comes to rest. A record that stops short on the 5° slope needs a steeper V, which is one number in `cad/params.py`; if a size still sits off, the wrist camera can take one look from above the slot before the arm descends, at the cost of a few seconds.

**Spindle in the cup.** The spindle tip enters the hollow bellows cup by about 10 mm when a record is released 3 mm above the mat. Confirm the cup's inner depth allows that with the chosen cup; otherwise release from a little higher.
