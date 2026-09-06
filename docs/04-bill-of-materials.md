# Bill of materials

Prices are typical German retail in September 2026, rounded, and will drift; check before ordering. Everything listed is stocked by German shops, so nothing depends on imports. Suggested sources: Motedis and Dold Mechatronik for extrusion, rails, screws, belts and pulleys; 3DJake and Amazon.de for the BIGTREETECH board and drivers; BerryBase and Reichelt for Raspberry Pi, cameras and extenders; Reichelt, Conrad and Amazon.de for motors, servos, pump, valve and sensors; Filamentworld or 3DJake for filament; any Baumarkt for plywood, bearings and fasteners.

## Bought parts

| Group | Part | Qty | ≈ € |
|---|---|---|---|
| Frame | 18 mm birch plywood, 1 sheet for panels, bench top, carousel disc and base plate | 1 | 60 |
| Frame | 2040 V-slot extrusion 1.3 m (X beams) | 2 | 30 |
| Frame | 2040 V-slot 0.8 m (cross beam), 2020 0.8 m (end tie), brackets, T-nuts, bolts | 1 set | 40 |
| Linear | Delrin V-wheel kits with eccentric spacers (X ×2 carriages, Y ×1) | 3 sets | 30 |
| Linear | MGN12H rail 0.8 m with carriage (Z column) | 1 | 30 |
| Motion | NEMA17 stepper, plain (X, Y, Z) | 3 | 36 |
| Motion | NEMA17 with 5:1 planetary gearbox (wrist, carousel index) | 2 | 70 |
| Motion | GT2 belt 5 m, 20T pulleys, idlers, tensioners | 1 set | 25 |
| Motion | T8 lead screw 0.8 m, nut, coupler, bearing block | 1 | 20 |
| Servos | Micro linear servo (cue lever) | 1 | 12 |
| Controller | BIGTREETECH Octopus V1.1 (or: donor printer board + Raspberry Pi Pico, see below) | 1 | 65 |
| Controller | TMC2209 driver (5 with the Octopus, 1 with the donor-board option) | 5 | 30 |
| Power | 24 V 150 W supply, 5 V 3 A buck module | 1 set | 35 |
| Computer | Raspberry Pi 5 4 GB, official PSU, 64 GB microSD | 1 | 90 |
| Cameras | Raspberry Pi Camera Module 3 | 2 | 60 |
| Cameras | CSI-to-HDMI extender pair (or USB camera module for the wrist) | 1 | 15 |
| Vacuum | 12 V diaphragm vacuum pump | 1 | 15 |
| Vacuum | 12 V 2/2 solenoid valve, vacuum switch, 40 mm bellows cup, 6 mm tubing, fittings | 1 set | 35 |
| Sensing | End-stops, Hall sensor, slot optical sensor | 1 set | 12 |
| Deck I/O | 6.3 mm mono plug and cable for the remote start/stop jack, thin wire (relay card: Conrad 393905, owned) | 1 | 4 |
| Light | LED bar (12 V, warm white) and logic-level MOSFET | 1 | 8 |
| Carousel | 608ZZ bearing (rollers) | 10 | 6 |
| Carousel | 6005 bearing, 25 mm stub shaft | 1 | 8 |
| Cabling | Cable chain 10 × 20 mm, 2.5 m; wire, connectors, crimps, sleeving | 1 set | 60 |
| Hardware | M3/M5 screws and nuts, heat-set inserts, felt, rubber sleeve stock | 1 set | 35 |
| Consumables | PETG 2.5 kg, TPU 0.3 kg | | 70 |
| **Total** | | | **≈ 865** |

Not included: the 3D printer, the turntable (Omnitronic DD 3120, owned), the Focusrite Scarlett (owned), the Conrad 393905 USB relay card (owned), and an external phono preamp if the deck's own line output is not used (about 40 €).

Where to trim further: a used Raspberry Pi 4 saves about 40 € and a USB camera on the wrist instead of the second Pi camera about 20 €.

## Donor printer

A used 3D printer is the cheapest source for most of the motion parts and is worth buying before anything else on the list. What it has to bring: at least four NEMA17 steppers, a 24 V supply, GT2 belts and pulleys, a T8 lead screw, V-slot extrusion with Delrin wheels and carriage plates, end-stops, and ideally a 32-bit board that runs Klipper. Candidates in rough order of usefulness:

| Donor | What it contributes | Notes |
|---|---|---|
| Creality CR-10 / CR-10S (300–500 mm) | 4–5 steppers, 2040/4040 V-slot up to 60 cm, 1–2 lead screws 40 cm, wheels, 24 V PSU, board | The best fit: longest extrusions and lead screws of the cheap decks; the S5 (500 mm) variant most of all |
| Creality Ender 3 / 3 Pro / V2 | 4 steppers, short 2020/2040 V-slot, 1 lead screw 36 cm, wheels, 24 V PSU, 4.2.x board (Klipper-capable, 4 drivers) | Plentiful and cheap; the long members must still be bought |
| Creality Ender 5 / 5 Plus | 4–5 steppers, 2020/2040 V-slot in a box frame, dual Z screws on the Plus, larger PSU | The Plus gives two lead screws and a 350 W supply |
| Anycubic Kobra / Vyper, Artillery Sidewinder | 4 steppers, 24 V PSU, some extrusion | Less V-slot, boards less Klipper-friendly; take for motors and PSU only |
| Tevo Tornado, Alfawise U20 | CR-10 clones | Same value as a CR-10 if cheap |

Whatever the donor, the long V-slot beams (2 × 1.3 m) and the 80 cm Z rail and lead screw are bought new; the donor covers motors, wheels, belts, pulleys, end-stops, PSU and fasteners, roughly 150 to 200 € of the list above, for a 50 to 100 € machine. Its board can run the four gantry axes under Klipper with a Raspberry Pi Pico (about 5 €) plus one TMC2209 stick as a second MCU for the carousel stepper and the remaining I/O, which replaces the Octopus and its drivers (about 95 €); or it is kept as a spare and the Octopus bought as planned.

## Printed parts

Roughly 30 distinct parts, 50 to 70 hours of printing. PETG unless marked TPU.

| Assembly | Parts |
|---|---|
| Gantry | 2 V-wheel carriage plates for the X beams (or the donor's), cross-beam end brackets, Y wheel plate, Z guide block, Z carriage with outrigger, lead-screw nut holder, column end caps |
| Wrist | hub with bearing seats, arm, cup bracket, hose clip, wrist camera mount, finger-lift fork with TPU lining, Hall sensor mount |
| Carousel | centre hub, 24 slot combs, 8 rim segments, 8 GT2 tooth-ring segments, 10 roller brackets, stepper mount with pulley, home-mark flag and sensor mount |
| Station | ring rest with TPU pads, post bracket, electronics box (or a bought enclosure) |
| Deck interface | cue-servo bracket, pusher rod guide, lever pad, end-stop pin base with TPU sleeve |
| Cameras and light | deck camera bracket, LED bar housing, cable-chain end brackets |

TPU goes on every surface that touches a record: the cup lip if it is not bought, the fork lining, the ring rest pads, the end-stop sleeve.

## Wood and other cut parts

From the plywood sheet: two side panels 121 × 83 cm with windows, one end panel 80 × 83 cm with a window, the bench top 190 × 100 cm (or an existing bench), the carousel disc Ø 86 cm, and the carousel base plate Ø 88 cm. None of the cuts needs to be better than a few millimetres; the precise surfaces are all bought (rails on extrusion) or printed (carousel hub and rim).
