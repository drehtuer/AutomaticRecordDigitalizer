# Sourcing pass, September 2026 — corrections to the bill of materials

Every line of `docs/04-bill-of-materials.md` priced against live German shop pages on 10 September 2026, incl. 19 % VAT, delivered to Germany. Amazon.de and Conrad.de block automated fetching, so they were excluded rather than guessed at.

The itemised result, with product links, three ways of ordering it and a sheet for the local Baumarkt, is in [bom-shopping-list.md](bom-shopping-list.md). Every priced line was fetched again on 3 October 2026; what that re-check changed is at the end of this file.

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
