# Sourcing pass, September 2026 — corrections to the bill of materials

Every line of `docs/04-bill-of-materials.md` priced against live German shop pages on 10 September 2026, incl. 19 % VAT, delivered to Germany. Amazon.de and Conrad.de block automated fetching, so they were excluded rather than guessed at.

The itemised result, with product links and three ways of ordering it, is in [bom-shopping-list.md](bom-shopping-list.md).

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

*Change of plan · affects `docs/06-open-questions.md`*

The wrist camera now tops out at 720p. If the tagging stage needs better, the answer is a static high-resolution label camera at the station — not a heavier camera on the moving wrist.

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
