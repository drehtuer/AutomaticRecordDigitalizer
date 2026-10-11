# Sourcing pass, September 2026 — corrections to the bill of materials

Every line of `docs/04-bill-of-materials.md` priced against live German shop pages on 10 September 2026, incl. 19 % VAT, delivered to Germany. Amazon.de and Conrad.de block automated fetching, so they were excluded rather than guessed at.

The itemised result, with product links, three ways of ordering it and a sheet for the local Baumarkt, is in [bom-shopping-list.md](bom-shopping-list.md). Every priced line was fetched again on 3 October 2026, and the panel material was decided on 4 October; what those changed is at the end of this file.

The headline: the BOM's estimate of ≈ 865 € holds up in aggregate, but only because it is the sum of two large errors in opposite directions plus a lot of accurate lines. The corrections below have been absorbed into the repo docs.

## Corrections

### Micro linear servo: 12 € is wrong by 10×

*Material · affects `docs/04-bill-of-materials.md`*

No sub-30 € linear servo is in stock at any German or EU shop. Verified: Actuonix PQ12-S 123,49 €, MightyZAP 6N 90,95 €. An MG996R metal-gear servo at 6,65 € driving the existing printed pusher rod does what the cue lever needs — a bracket change, not a design change.

### Vacuum switch: the 12 € sensing set cannot cover it

*Material · affects `docs/04-bill-of-materials.md`*

Industrial vacuum switches start at 95,30 € in Germany. An Adafruit MPRLS absolute-pressure breakout at 30,90 € plus a software threshold replaces it — but see the open question below, because it moves where the check lives.

### The solenoid valve must be direct-acting

*Important · affects `docs/04-bill-of-materials.md`*

Pilot-assisted valves (the common 2V025 type) do not open at zero differential pressure, i.e. under vacuum. Verified suitable: 2/2-way G 1/8″ NC, FKM, 12 V, direktgesteuert, 0–16 bar — 42,44 €.

### Motedis cannot supply the extrusion

*Important · affects `docs/04-bill-of-materials.md`*

It is named first under suggested sources, but Motedis carries no V-slot profile at all — only B-Typ Nut 6 and I-Typ Nut 5, which have no wheel-running surface. Use shop.bohrers.de at 12,90 €/m, or Dold at 14,00 €/m plus a 0,50 € cutting fee.

### The computer becomes a Raspberry Pi 4B rev 1.1, 2 GB

*Change of plan · affects `docs/03-electronics-and-software.md`*

Already owned, two of them. One CSI port instead of two, so the wrist camera takes the USB branch the doc already sanctions and the CSI-HDMI extender leaves the BOM entirely. WAVs go to an external USB 3.0 SSD, never the card — about 860 MB per side, 40 GB per magazine. Everything USB on a powered hub with udev-pinned device names. rev 1.1 refuses e-marked USB-C cables.

### Where does the GRIP post-condition live now?

*Material · affects `docs/06-open-questions.md`*

docs/03 puts the vacuum switch on a controller end-stop input and has GRIP wait on it inside Klipper. An MPRLS is an I²C device on the Pi, so that check moves to the orchestrator and a failed grip no longer aborts inside the motion queue. Either keep a cheap digital switch purely as the Klipper interlock, or accept the latency and document it. Needs deciding before anything is wired.

### Are 720p label photographs enough for Discogs matching?

*Change of plan · affects `docs/06-open-questions.md` · retired on 3 October 2026*

The wrist camera now tops out at 720p. If the tagging stage needs better, the answer is a static high-resolution label camera at the station — not a heavier camera on the moving wrist. Retired once record identity was decided to come from the manifest: see the re-verification below.

### Donor table: three corrections

*Change of plan · affects `docs/04-bill-of-materials.md`*

Add the Ender 3 Max Neo near the top — 300×300 frame, dual Z with two motors, 32-bit board, 350 W supply. Add the Ender 3 S1 family as avoid: its frame is smooth-faced extrusion, not open V-slot, so frame and wheels are useless here. And note that TMC drivers on Creality 4.2.x boards are soldered down, so they cannot be harvested.

## Raspberry Pi 4B: the gotchas worth reading before wiring

- rev 1.1 boards refuse power from e-marked USB-C cables — use the official supply or a plain cable. Verify the board with `cat /proc/cpuinfo`, which should show `a03111`.
- rev 1.1 puts the SD-card voltage regulator on the underside next to the slot, where it is easy to knock off. Set the card up once and leave it alone.
- Inside a closed electronics box under sustained vision load, a Pi 4 wants a heatsink and a fan.
- The Pi 4 budgets roughly 1.2 A across all four USB ports. Put the Scarlett, the SSD, the webcam and the relay card on a self-powered hub, and pin every device with a udev rule so `/dev/video*` and the ALSA card index do not shuffle across reboots.
- Do not run the Pi from the servo's 5 V buck converter: an MG996R stalls at about 2.5 A and will brown the Pi out.
- CPU is roughly 2 to 2.5× less than a Pi 5. The workload absorbs it because the only sustained vision load is the deck camera tracking the headshell in a known ROI — keep those frames at about 640 × 480, 10–15 fps, and process the 12 MP label shots one at a time.

## Errata from the consistency check, 14 September 2026

Checking the bill of materials against `cad/params.py` and the planner's actual travel changed these lines after the pricing pass. The shopping list above still shows the lengths as priced; order these instead.

- **2040 cross beam: 940 mm, not 800.** The frame is 860 mm wide over the panels and the X carriage plates sit outside it. The 800 mm cut is the concept's 80 cm frame, which the CAD widened to 86 and the cut list never followed. Same profile, same shop; about 2 € more.
- **2020 end tie: 880 mm, not 800**, over the two X beams. Still cut from the 1 m length.
- **End panel: 842 × 830, not 800 × 830.** It sits between the side panels' inner faces.
- **Plywood: two 1500 × 3000 sheets, not one** — panels on one, both carousel discs on the other — and a third if the bench top is cut rather than existing.
- **V-wheels: 12, not 9.** Four per carriage plate, three plates, six eccentric spacers as priced.
- **A 24 → 12 V buck, about 3 €**, was missing altogether: the pump, the valve and the LED strip are 12 V parts and the list has only a 24 V supply and a 5 V buck.
- **Cable chain: three chains, 700 + 600 + 600 mm.** The Y carriage travels 625 mm along the cross beam, which the concept forgot. The 3 m priced covers it with a metre spare.
- **PU tube: 7 m, not 5.** With the electronics on the frame the run from the pump to the cup is 4.5 m with wiggle room, and a 2.1 m stub carries the vacuum to the pressure sensor beside the Pi.
- **Not on the list at all**: about 6 m of 4-core, 12 m of 3-core and 4 m of 2-core extension wire, because the motors come with about 1 m of lead and the sensors with none; a 2 m USB 2.0 A-to-A extension for the wrist camera; and a 3 m USB-C cable from the Pi to the Octopus, now that the two sit at opposite ends of the frame. The 0.5 m camera ribbon is right: the Pi mounts on the deck-end panel, 30 cm from the camera. The routed lengths are tabulated in `docs/08-assembly-instructions.md`.

## Decided since, 14 September 2026

- The `GRIP` post-condition lives in the orchestrator, on the MPRLS alone; no switch, no Klipper interlock. `docs/05-design-decisions.md`.
- The electronics sit on the frame, not in a box; the Pi is on the deck-end panel and the 0.5 m camera ribbon is right.
- 720p label photographs: still to be tried on a batch. The 1080p webcam already on hand is the first fallback.

## Re-verification, 3 October 2026

Every priced line of the shopping list was fetched again, and the list was checked line by line against `docs/04-bill-of-materials.md` and the cable table in `docs/08-assembly-instructions.md`. Against the 10 September figures the three routes are up by 70 to 80 € each. About 48 € of that is two tools added on 20 September, the SN-01BM crimper and a heat gun. The rest is mostly parts that were missing, not parts that got dearer.

### Two parts discontinued, five lines missing

*Material · affects `sourcing/bom-shopping-list.md`*

roboter-bausatz has dropped the Octopus V1.1, now from 3DJake at 65,99 € with free shipping and only two in stock, and the 17HS4417P1 stepper; the 17HS4417P1-X4 is the same motor with a different cable, at 11,95 € instead of 15,54 €. Against `docs/04` the list lacked the second buck converter, the pneumatic tee, both USB cables and the multi-core extension wire, and still carried the cross beam at 800 mm (940), the end tie at 800 (880), nine wheels (twelve) and 5 m of tube (7) — the errata of 14 September below, which the list itself had never absorbed. Eleven roboter-bausatz prices had moved and three of the September prices were the wrong quantity tier. druckluft-fachhandel adds 9,90 € of Anbruchkosten to any tube order under 50 m, now its own row. The multi-core wire forces Conrad into the order: it is the only shop with verified multi-core meterware, though Reichelt very likely has the same LiYY and blocked the re-check.

### Wood: the disc sheet halves, the panel sheet is a choice

*Material · affects `docs/04-bill-of-materials.md`, `docs/08-assembly-instructions.md`*

The bill of materials' 120 € for two sheets was wrong by a factor of about 3.5. The two carousel discs fit an MDF E1 sheet 2440 × 1220 × 18 at 49,95 €, in stock — MDF is right for the discs, which need flatness rather than stiffness. The three frame panels fit one sheet only if it is 3000 × 1500, which at Hornbach means birch multiplex at 222,80 €, a store order of four to five weeks. Every cheaper material needs two 2500 × 1250 or 2440 × 1220 sheets: OSB 3 at 62,18 € (rough, chips at the cut-outs, holds the bracket screws less well), maritime-pine plywood at 188,00 €, birch-faced eucalyptus at 218,00 € (in stock, no wait). Wood for the whole machine: 272,75 € in birch and MDF, 112,13 € at the cheapest.

### New line: a 4.3″ DSI status display

*Change of plan · affects `docs/03-electronics-and-software.md`, `docs/04-bill-of-materials.md`*

A Waveshare 4.3″ capacitive touch display, 800 × 480, shows the cycle state, the fault screen and the current side's label photograph. It uses the Pi 4B's free DSI port — the camera is on CSI — so it needs no GPIO, no separate supply and no adapter: one 15-pin ribbon carries video, touch and power at 1.2 W. 37,90 € plus a 2,90 € 500 mm ribbon. It sits on the deck-end panel's front post, a 41 cm ribbon run from the Pi, is drawn by a small Python renderer straight to the framebuffer rather than by a browser, and must be mounted so its light misses the platter, or it corrupts the strobe speed measurement.

### Decided: record identity comes from the manifest

*Decision · affects `docs/03-electronics-and-software.md`*

Artist, title and label are entered by the user when loading the carousel, ideally as a Discogs release ID resolved once at load time, and never read from the label photograph. The manifest grows to carry them. This retires the 720p question above: matching never depends on the label photographs, so they only need to let a person confirm a record later.

### What catches a mis-loaded magazine?

*Open question · affects `docs/06-open-questions.md`*

With identity coming from the manifest, nothing checks that slot 7 physically holds the record the manifest claims, and the machine will label the recording confidently and wrongly. The label photograph is captured anyway, so show it beside the manifest text in a per-side review screen. It is the only thing between a slip while loading and a mislabelled archive.

### Cable check against the CAD routes

*Material · affects `docs/04-bill-of-materials.md`, `docs/08-assembly-instructions.md`*

Everything Klipper-side reaches as tabulated. Three things did not. The wrist webcam is read by the Pi, so its cable starts at the hub in the Pi group and runs the length of both panels before the chains: about 4.9 m routed, 5.6 m with margin, past the 5 m passive USB 2.0 limit, so the 2 m passive extension becomes an active 5 m repeater. The Oyostepper geared motors come with 500 mm bare leads, not the 1 m assumed, so the 4-core is 7 m rather than 6. And the 3 m of thin 2-core for the 33/45 button taps had no line anywhere, so the 3-core is 15 m rather than 12 and two of its cores serve. The Pi-to-Octopus cable is USB-A on the Pi to USB-C on the board. The Z chain carries the hose, the USB cable, the 4-core and the 3-core side by side at about 19 of its 20 mm width: full, and accepted, so nothing more goes into it later.

### Order status

*Status · affects `sourcing/bom-shopping-list.md`*

The BerryBase part of the list was ordered on 3 October: the Camera Module 3, the display, the pump, the MPRLS, the KY-003 Hall sensor, the JST connector kit and an Armor aluminium shell with twin fans for the Pi. Those rows are now at 0,00 € like the other owned hardware. The heat gun and both USB cables moved to Conrad, which is in the order for the wire anyway and passes its free-shipping line with them, and the two 50 cm ribbons to welectron.

## Decided 4 October 2026: OSB panels, steel where OSB is weak, MDF discs

*Decision · affects `docs/01-design-specification.md`, `docs/04-bill-of-materials.md`, `docs/05-design-decisions.md`, `docs/08-assembly-instructions.md`*

The three frame panels are OSB 3, 18 mm, from two 2500 × 1250 sheets at 31,09 € each, in place of the 222,80 € birch sheet with its four-to-five-week store order. Both side panels come from one sheet and the end panel from the other, cut to rectangles at the Markt so nothing larger than 1210 × 830 has to go in the car; the second sheet leaves about 1.1 m² of offcut. The maritime-pine and birch-faced eucalyptus alternatives priced on 3 October are out. The discs stay MDF E1, cut at the Markt into an 880 and an 860 square.

OSB is stiff enough for a glued box but weak in three places, and each gets steel or a fastener instead:

- Screws into its edge hold poorly, so the two corners where the side panels meet the end panel get a 25 × 25 × 3 steel angle the full 830 mm height, screwed into both faces with 3.5 × 16 screws every 120 mm. The glue and the edge screws stay as well.
- Wood screws strip it when taken out and put back, so every part that comes off again sits on M4 T-nuts pressed in from the far face, with M4 × 30 machine screws: the controller plate, the Pi plate, the cue-servo and camera brackets, the display mount and the pump mount, about 18 positions. Printed parts that stay put still go on 3.5 mm wood screws into the face, which hold fine.
- A bolt head pulls into its strands, so the M5 beam bolts get 15 mm penny washers on the panels' outer faces.

The window corners get a 20 to 26 mm hole drilled first, so the jigsaw never has to turn in OSB; round corners stop both chipping and cracks. The metal and fasteners add 24,70 €. Wood and metal together come to 136,83 €, where birch and MDF alone were 272,75 €, and the Hornbach sheet drops from 362,81 € to 226,89 €, all shelf stock with no lead time.

The sheet bought for the carousel base plate is 18 mm, where `cad/params.py` had drawn the plate 15 mm thick (`CAR_BASE_T`), a figure that predated the material decision. The model now draws it at 18 mm, and the disc sits on its rollers 3 mm higher with it, so every pick height follows; exports, renders and the collision sweep were regenerated with the change.

## Donor bought, 6 October 2026

*Status · affects `sourcing/bom-shopping-list.md`, `docs/04-bill-of-materials.md`, `docs/07-status-and-next-steps.md`*

The donor for the third route is a Creality Ender 3 V2, bought on eBay for 55 € including delivery, against the 75 € the route had been priced with; it arrives the week of 12 October. The donor route drops to 653,69 € of parts and 691,29 € delivered. What it actually contains still decides several of that route's lines: run it once before stripping it, note the board revision and the MCU marking (an STM32F103, or a GD32 clone that needs different Klipper build options), and count the wheels and eccentrics against the 12 and 6 the build needs before ordering the rest.

## Orders received, 11 October 2026

*Status · affects `sourcing/bom-shopping-list.md`, `docs/04-bill-of-materials.md`, `docs/07-status-and-next-steps.md`*

The Conrad, cnc-zubehoer and welectron orders placed on 7 October have arrived, and their rows are at 0,00 € like the other owned hardware. From Conrad: the heat gun, the active USB repeater, 7 m of the 4-core and 15 m of the 3-core LifYY. From cnc-zubehoer: the three 1 m cable chains, 22,73 € with shipping. On the fewest-suppliers and donor routes they replace the Dold CK10 chain and its connection elements, so Dold's order there is 33,71 € smaller. From welectron: both 50 cm ribbons, which shipped free.

Conrad charged more than the 3 October re-check found. The four lines kept cost 113,86 € against 93,86 € listed: the heat gun 29,99 € instead of 19,32 €, the repeater 10,99 € instead of 10,08 €, and the wire 3,49 and 3,23 €/m instead of 2,93 €/m, without the 10 m tier.

The USB-A to USB-C cable for the Octopus was not in the order; the invoice carries a Hama Lightning-to-USB-A 1 m cable instead, which fits neither the Pi nor the Octopus. It is the one Conrad line left, below the free-shipping threshold, so it now carries 4,95 € of shipping on every route. With the bought lines out, the three routes stand at 840,58, 743,45 and 557,92 € delivered.

## Donor route fixed as the build, 11 October 2026

*Decision and corrections · affects `sourcing/bom-shopping-list.md`, `README.md`, `docs/01`, `03`, `04`, `05`, `06`, `07`, `08`, `cad/README.md`*

With the Ender 3 V2 bought, the build follows the donor route and the documents were brought to it. The controller is the donor's Creality 4.2.x board for X, Y, Z and the wrist, and a Raspberry Pi Pico on a small carrier board as the second Klipper MCU for the carousel stepper (one TMC2209 stick), the cue servo, the pump, the valve and the LED bar (three IRLZ44N, where the list had two) and the two home sensors; the Octopus stays priced as the fallback. `03` describes the two-MCU configuration, `05` records the decision, `08` wires it and commissions it, including the Vref trimmers of the board's soldered drivers, and `06` gains the one question it opens, whether those drivers hold the wrist's 1.68 A geared motor.

Checking the donor route against what an Ender 3 V2 actually contains moved two rows onto the donor — the 5 → 8 mm Z coupler, which is the V2's own, and the frame's inside corner brackets — and three off it: the belts, since the V2's 0.75 m lengths cannot cover a 1.29 m X run and a 0.94 m Y loop; a third idler; and a third pulley. That pulley exposed an error older than the donor route: the carousel's pulley sits on the Oyostepper gearbox's output shaft, which is 8 mm (verified on the product page on 11 October), and every sheet had bought 5 mm bores since September. All three routes now buy two 5 mm pulleys and one 8 mm. The end-stop count on the Octopus routes dropped from five to the three the build has, and the wrist hub, whose printed seats never had a bearing on any list, gets two more 608s on the Dold order.

Two Baumarkt leftovers had fallen between the sheets: the ring rest's O-ring and the pump's four rubber-metal buffers, which the Hornbach notes send to an online order that no route carried. They have rows now, on druckluft-fachhandel and Reichelt. The wrist camera is the Logitech C270 on every sheet, as `01`, `03` and `08` had said all along; the shopping list had named the Trust 1080p. The Pi's leads to the controller group are two 3 m USB-A to micro-B cables, since the 4.2.x board and the Pico both take micro-USB, so the USB-C cable the Octopus routes buy — and the Lightning cable Conrad sent in its place — are not wanted; Conrad leaves the donor route. The display's mount joins the printed-parts table, with the display's own M2.5 standoffs, and so does the TPU cup lip the routes without a bought cup rely on. In `08` the Y-axis paragraph, which had described a belt fixed at both ends with the motor on a fixed bracket, now describes the loop the CAD and the cable table imply.

The `01` specification's last line, which still said plywood, now says OSB and MDF.

The same evening, at the owner's request, Amazon joined every route for the small parts: all of Reichelt's lines (the jack lead, the LED strip, the MOSFETs, the heat-shrink box, the heat-set inserts, the micro-USB leads, the pump buffers; on the Octopus routes also the Mean Well supply and the Conrad USB-C lead) and the pneumatic consumables from druckluft-fachhandel (tube, push-in fittings, tee, O-ring), which takes that shop's 9,90 € cut-length surcharge with them and leaves it the valve and the nipple. Reichelt and Conrad leave the sheets. The point is one parcel fewer, Prime delivery and availability that can be checked in a browser, not price: Amazon sells in packs where Reichelt sold singles, so the donor route rises by about 15 € to 533,65 € of parts and 560,35 € delivered; the bill of materials for the whole machine, donor included, is about 892 €. The roboter-bausatz basket stays whole, since it ships free only above 99 €. Every Amazon row was then looked up in Chrome the same evening, so the list links each listing by ASIN with the price shown and names the plainer or cheaper alternative beside it; two of the lookups changed the part itself: the deck's remote lead is a solder-type 6.35 mm mono plug on the 3-core wire already bought, as the bill of materials had always said, rather than a ready-made lead, and the Octopus routes' supply is the genuine Mean Well at 19,95 €.

## Link check, 12 October 2026

*Corrections · affects `sourcing/bom-shopping-list.md`, `docs/04-bill-of-materials.md`, `docs/06-open-questions.md`, `docs/07-status-and-next-steps.md`*

Every link on the donor route and the Hornbach sheet, 76 of them, was opened in Chrome. Four were wrong: the Dold stub shaft's URL carried parentheses, which Markdown cannot, so the link stopped at the first one and the shop's clean URL replaces it; the Dold corner-bracket link pointed at a category; and the two roboter-bausatz search links now point at the products, the 8 mm pulley at 1,29 € and the sleeving at 0,45 €/m. The 'StepStick breakout' estimate had no product behind it and needs none — the Pico carrier is a 1,45 € perfboard with 4,48 € of female headers — and the Saugeranschlussnippel link was dead: the live part is the FGN 016 18 I, G 1/8 female, 3,14 €, on request, and the shop stocks no bellows cup above 25 mm, which the open question on the cup now notes. Every other link opened on its product, and all 21 Hornbach prices were unchanged.

roboter-bausatz's prices had drifted since September, mostly up — Nutensteine 0,47 € instead of 0,25 €, which is 11 € on the fifty the beams need, Hammerkopfschrauben 2,41 € a pack, the belt 11,39 € — and down on the idler, the TMC2209, the KFL08, the bucks, the KY-010 and the MG996R, which is 4,95 € on offer. Oyostepper had raised the geared motor to 37,02 € and its shipping, from the owner's basket, is 15,27 €, 89,31 € for the pair delivered; the same STEPPERONLINE motor is on Amazon, sold by STEPPERONLINE with Prime, at 43,00 €, so the donor route takes it there, 86,00 € for the pair, and Oyostepper leaves the route. STEPPERONLINE's newer MG-series 5:1 motor at 37,99 € would save 10 € more but its Amazon page states neither current nor shaft diameter, so it stays a note. druckluft-fachhandel then turned out unable to supply the nipple at all, so it is the same Riegler part (314.018) from Blumenbecker on Amazon, 2,95 € plus a 5,55 € marketplace parcel, and druckluft keeps only the valve. The donor route stood at 590,35 € delivered.

Asked whether five packs of M5 T-head bolts and fifty slide-in nuts were needed, the count said no: about 25 T-head bolts go into slots across the build and the Ender 3 V2 brings its own bag of slot hardware, so one pack of 20; and the slide-in nuts bolt the two X beams to the panels, 16 of them, so 25. The count also found the Z column on no sheet. The CAD has always drawn a 760 mm, 40 mm wide column with the MGN12 rail on its face, and `08` bolts the rail to it, but `01` and `04` had read the rail itself as the column and nothing bought it; a 12 mm rail cannot carry a 90 mm outrigger over 760 mm on its own. A 760 mm 2040 cut joins the Dold order at 11,14 €, M3 spring-ball T-nuts from Amazon fix the rail to it, and `01`, `04` and `08` now say so. The X beams are ordered at the CAD's 1290 mm rather than 1300, since Dold cuts to the millimetre. The donor route stands at 563,46 € of parts and 588,81 € delivered, four online suppliers and the donor; the bill of materials at about 921 €.
