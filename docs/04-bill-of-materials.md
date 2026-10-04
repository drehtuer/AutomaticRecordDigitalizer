# Bill of materials

Prices are typical German retail, rounded, and will drift; check before ordering. Every line was priced against live German shop pages on 10 September 2026 and re-verified on 3 October 2026, and the figures below have been corrected where those passes disagreed with the estimate; the itemised result, with product links, three ways of ordering it and a sheet for the Baumarkt, is in [../sourcing/bom-shopping-list.md](../sourcing/bom-shopping-list.md), and what it changed here is in [../sourcing/2026-09-sourcing-and-bom-corrections.md](../sourcing/2026-09-sourcing-and-bom-corrections.md). Everything listed is stocked by German shops, so nothing depends on imports. Suggested sources: shop.bohrers.de or Dold Mechatronik for V-slot extrusion and the linear rail; roboter-bausatz.de for wheels, belts, pulleys, steppers, the lead screw, the servo and fastener assortments; 3DJake for the Octopus, which roboter-bausatz no longer carries; oyostepper.de for the geared steppers; BerryBase and Reichelt for the Raspberry Pi side, cameras, the display, sensors and LED; Conrad for the multi-core extension wire and the USB cables; druckluft-fachhandel.de for the solenoid valve, tubing and push-in fittings; Filamentworld or 3DJake for filament; Hornbach or any Baumarkt for the sheet material, the corner steel, glue and wood screws. Not Motedis: it carries only B-Typ Nut 6 and I-Typ Nut 5 profile and no V-slot at all, so nothing it sells has a wheel-running surface.

## Bought parts

| Group | Part | Qty | ≈ € |
|---|---|---|---|
| Frame | 18 mm OSB 3, two 2500 × 1250 mm sheets, for the three panels; 18 mm MDF, 2440 × 1220 mm, for the two carousel discs; a 25 × 25 × 3 steel angle for the two inside corners, M4 T-nuts and machine screws for the parts that come off again, penny washers for the beam bolts; a further sheet for the bench top only if there is no bench | 2 + 1 | 137 |
| Frame | 2040 V-slot extrusion 1.3 m (X beams) | 2 | 30 |
| Frame | 2040 V-slot 0.94 m (cross beam, spanning the 86 cm frame with the plates outside it), 2020 0.88 m (end tie), brackets, T-nuts, bolts | 1 set | 42 |
| Linear | Delrin V-wheels, four per carriage plate (X ×2, Y ×1), six of them on eccentric spacers | 12 + 6 | 45 |
| Linear | MGN12H rail 0.8 m with carriage (Z column) | 1 | 30 |
| Motion | NEMA17 stepper, plain (X, Y, Z) | 3 | 36 |
| Motion | NEMA17 with 5:1 planetary gearbox (wrist, carousel index) | 2 | 70 |
| Motion | GT2 belt 5 m, 20T pulleys, idlers, tensioners | 1 set | 25 |
| Motion | T8 lead screw 0.8 m, nut, coupler, bearing block | 1 | 20 |
| Servos | MG996R metal-gear servo working the cue lever through a printed yoke on its horn | 1 | 7 |
| Controller | BIGTREETECH Octopus V1.1 (or: donor printer board + Raspberry Pi Pico, see below) | 1 | 65 |
| Controller | TMC2209 driver (5 with the Octopus, 1 with the donor-board option) | 5 | 30 |
| Power | 24 V 150 W supply; 24 → 5 V 3 A buck for the servo; 24 → 12 V 3 A buck for the pump, the valve and the LED bar, which are all 12 V | 1 set | 38 |
| Cameras | Raspberry Pi Camera Module 3 (deck camera; the Pi 4B has one CSI port, so the wrist camera is USB and owned) with a 500 mm ribbon; the Pi sits on the deck-end panel 30 cm away | 1 | 29 |
| Display | Waveshare 4.3″ capacitive touch display, DSI, 800 × 480, on the Pi's free DSI port, with a 500 mm 15-pin ribbon: cycle state, fault screen, the current side's label photo | 1 | 41 |
| Vacuum | 12 V diaphragm vacuum pump | 1 | 11 |
| Vacuum | 12 V 2/2 solenoid valve, G 1/8 NC, FKM — **direct-acting**, not pilot-assisted | 1 | 42 |
| Vacuum | Adafruit MPRLS 0–25 PSI I²C pressure breakout, in place of a vacuum switch | 1 | 31 |
| Vacuum | 40 mm bellows cup, 7 m of 6 × 4 PU tubing (4.5 m to the cup and a 2.1 m stub to the pressure sensor, with wiggle room), push-in fittings, a tee | 1 set | 40 |
| Sensing | End-stops, Hall sensor, slot optical sensor | 1 set | 12 |
| Deck I/O | 6.3 mm mono plug and cable for the remote start/stop jack, thin wire (relay card: Conrad 393905, owned) | 1 | 4 |
| Light | LED bar (12 V, warm white) and logic-level MOSFET | 1 | 8 |
| Carousel | 608ZZ bearing (rollers) | 10 | 6 |
| Carousel | 6005 bearing, 25 mm stub shaft | 1 | 8 |
| Cabling | Cable chain 10 × 20 mm, 3 m for three chains (X 0.7, Y 0.6, Z 0.6 m); 7 m of 4-core and 15 m of 3-core extension wire (LiYY 0.25 mm², two cores of the 3-core for the button taps), 10 m of 20 AWG pair for the 12 V loads; an active 5 m USB 2.0 repeater for the wrist camera and a 3 m USB-A to USB-C cable from the Pi to the controller; connectors, crimps, sleeving | 1 set | 138 |
| Hardware | M3/M5 screws and nuts, heat-set inserts, felt, rubber sleeve stock, one 97 × 3 NBR O-ring for the ring rest | 1 set | 36 |
| Consumables | PETG 2.5 kg, TPU 0.3 kg | | 70 |
| **Total** | | | **≈ 1 051** |

Not included, because they are already on hand: the 3D printer, the turntable (Omnitronic DD 3120), the Focusrite Scarlett, the Conrad 393905 USB relay card, the Raspberry Pi 4B (two of them, the second a cold spare) with its 15 W supply and 32 GB card, the external USB 3.0 SSD the recordings are written to, the self-powered USB 3.0 hub everything else hangs off, and the USB webcams for the wrist (two on hand, a 720p Logitech C270 and a 1080p module). Together those are roughly 185 to 195 € that do not have to be spent. Also not included: an external phono preamp if the deck's own line output is not used (about 40 €).

The table above is the planning estimate, rounded, and it counts the sheet material and the filament. The [sourcing pass](../sourcing/bom-shopping-list.md) priced every line against live shop pages on 10 September and again on 3 October 2026, and costed three ways of actually ordering it, including shipping and excluding filament, sheet material and the other Baumarkt items. The routes include the crimp tool and the heat gun, about 48 €, which this table leaves out with the other tools; parts already ordered on 3 October count as owned. The Baumarkt sheet, priced at Hornbach for pickup, comes on top of whichever route is ordered:

| Route | Parts | Shipping | Delivered |
|---|---|---|---|
| Cheapest per line, 12 suppliers, 12 parcels | 905,67 | 57,30 | **962,97** |
| Consolidated into 8 suppliers | 839,22 | 37,60 | **876,82** |
| With a donor printer, 7 suppliers and the donor | 673,69 | 37,60 | **711,29** |
| Baumarkt, Hornbach pickup, on top of any route | 226,89 | — | **226,89** |

Consolidating is close to free rather than a discount: it costs about 28 € more on parts (the MGN12 rail, the camera, the energy chain) and saves about 30 € on shipping. The gap between the first two routes is almost entirely the servo substitution. Five suppliers is not reachable for the complete list. No German general-purpose shop stocks a NEMA17 with a 5:1 planetary gearbox, so either take 10:1 from Dold, which is fine for the wrist and the carousel since both are slow, or accept another shop; and since October the Octopus and the multi-core wire each pull in one more, 3DJake and Conrad. Six is the realistic floor: 10:1 motors from Dold and the wire from Reichelt.

Where to trim further: the donor printer route above is the real saving. The panels are already the cheap option, OSB 3 instead of birch multiplex, about 136 € less with the steel that makes up for OSB's weak edges (see `05-design-decisions.md`). The two obvious earlier trims are already taken — the computer is an owned Pi 4B, and the wrist camera is an owned USB webcam rather than a second Pi camera.

## Donor printer

A used 3D printer is the cheapest source for most of the motion parts and is worth buying before anything else on the list. What it has to bring: at least four NEMA17 steppers, a 24 V supply, GT2 belts and pulleys, a T8 lead screw, V-slot extrusion with Delrin wheels and carriage plates, end-stops, and ideally a 32-bit board that runs Klipper. Candidates in rough order of usefulness:

| Donor | What it contributes | Notes |
|---|---|---|
| Creality CR-10 / CR-10S (300–500 mm) | 4–5 steppers, 2040/4040 V-slot up to 60 cm, 1–2 lead screws 40 cm, wheels, 24 V PSU, board | The best fit: longest extrusions and lead screws of the cheap decks; the S5 (500 mm) variant most of all |
| Creality Ender 3 Max Neo | 4 steppers, dual Z with two motors, 300 × 300 frame so longer 2040 members than a plain Ender 3, wheels, 350 W supply, 32-bit board | Second only to a CR-10: the bigger frame and the second Z motor and screw are exactly what this machine wants |
| Creality Ender 3 / 3 Pro / V2 | 4 steppers, short 2020/2040 V-slot, 1 lead screw 36 cm, wheels, 24 V PSU, 4.2.x board (Klipper-capable, 4 drivers) | Plentiful and cheap; the long members must still be bought |
| Creality Ender 5 / 5 Plus | 4–5 steppers, 2020/2040 V-slot in a box frame, dual Z screws on the Plus, larger PSU | The Plus gives two lead screws and a 350 W supply |
| Anycubic Kobra / Vyper, Artillery Sidewinder | 4 steppers, 24 V PSU, some extrusion | Less V-slot, boards less Klipper-friendly; take for motors and PSU only |
| Tevo Tornado, Alfawise U20 | CR-10 clones | Same value as a CR-10 if cheap |
| Creality Ender 3 S1 / S1 Pro / S1 Plus | **Avoid.** Steppers and PSU only | Its frame is smooth-faced extrusion, not open V-slot: there is no groove for a wheel to run in, so neither the profile nor the wheels are reusable here |

Whatever the donor, the long V-slot beams (2 × 1.3 m) and the 80 cm Z rail and lead screw are bought new; the donor covers motors, wheels, belts, pulleys, end-stops, PSU and fasteners, roughly 150 to 200 € of the list above, for a 50 to 100 € machine. Its board can run the four gantry axes under Klipper with a Raspberry Pi Pico (about 4 €) plus one TMC2209 stick (about 6 €) as a second MCU for the carousel stepper and the remaining I/O, which replaces the Octopus and its five drivers, about 92 € of the list for about 10 €; or it is kept as a spare and the Octopus bought as planned.

Two things to check on the donor before counting on its board. Only the 32-bit Creality 4.2.2 and 4.2.7 boards run Klipper; an 8-bit 1.1.4 board does not, and then the Octopus goes back on the list. And the TMC drivers on the 4.2.x boards are soldered down, not socketed sticks, so they cannot be harvested — whatever else the donor gives, the drivers for any axis it does not run itself are bought new.

## Printed parts

Roughly 30 distinct parts, 50 to 70 hours of printing. PETG unless marked TPU.

| Assembly | Parts |
|---|---|
| Gantry | 2 V-wheel carriage plates for the X beams (or the donor's), cross-beam end brackets, Y wheel plate, Z guide block, Z carriage with outrigger, lead-screw nut holder, column end caps |
| Wrist | hub with bearing seats, arm, cup bracket, hose clip, wrist camera mount, finger-lift fork with TPU lining, Hall sensor mount |
| Carousel | centre hub, 24 slot combs with V floors, 8 GT2 tooth-ring segments, 10 roller brackets, stepper mount with pulley, home-mark flag and sensor mount |
| Station | ring rest with a rubber O-ring in its top groove, post foot; controller plate and Pi plate for the panel outsides, pump mount on rubber feet |
| Deck interface | cue-servo post and beam, horn yoke for the lever, end-stop bar and pin base with TPU sleeve |
| Cameras and light | deck camera bracket, LED bar housing, cable-chain end brackets |

Something soft goes on every surface that touches a record: TPU for the cup lip if it is not bought, the fork lining and the end-stop sleeve; a bought rubber O-ring on the ring rest.

## Wood and other cut parts

From the sheet material: two side panels 121 × 83 cm with windows, one end panel 84 × 83 cm with a window (it sits between the side panels, whose inner faces are 84.2 cm apart), the bench top 190 × 100 cm (or an existing bench), the carousel disc Ø 86 cm, and the carousel base plate Ø 88 cm. That is two 2500 × 1250 OSB sheets for the panels, both side panels on one and the end panel on the other, and one 2440 × 1220 MDF sheet for the discs, which fit side by side with 700 mm to spare, plus a further sheet for the bench top. The cut list with the window sizes and the nesting is in `08-assembly-instructions.md`. None of the cuts needs to be better than a few millimetres; the precise surfaces are all bought (rails on extrusion) or printed (carousel hub and combs).
