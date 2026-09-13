# Shopping list, priced 10 September 2026

Every line of `docs/04-bill-of-materials.md` against live German shop pages, incl. 19 % VAT, delivered to Germany, excluding shipping in the unit prices and adding it per supplier at the end of each route.

Three ways to order the same machine. Rows at 0,00 € are hardware already owned or supplied by a donor printer; they are listed so the build stays complete, and they carry no cost so the totals stay honest. Plywood, Baumarkt items and filament are excluded throughout.

Prices drift — re-check before ordering. Lines marked ESTIMATE could not be fetched, because Amazon.de and Conrad.de block automated access.

| Route | Parts | Shipping | Delivered |
|---|---|---|---|
| [Cheapest per item](#cheapest-per-item) | 821,60 | 67,15 | **888,75** |
| [Fewest suppliers](#fewest-suppliers) | 758,70 | 37,60 | **796,30** |
| [Donor printer route](#donor-printer-route) | 599,69 | 42,05 | **641,74** |

The notes under each route call them sheet 1, sheet 2 and sheet 3, in the order of the table above.

The corrections this pass produced, and which repo documents absorbed them, are in [2026-09-sourcing-and-bom-corrections.md](2026-09-sourcing-and-bom-corrections.md).

## Cheapest per item

Sourced from German shops, delivered to Germany. Prices incl. 19% VAT, verified 10 September 2026. Source BOM: github.com/drehtuer/AutomaticRecordDigitalizer/blob/main/docs/04-bill-of-materials.md

| Group | Part | Qty | Unit € | Line € | Supplier | Note |
|---|---|---|---|---|---|---|
| Frame | [Aluprofil 2040 V-Slot Nut 6 black, cut 1300 mm (12,90 €/m)](https://shop.bohrers.de/V-Slot-2040-Zuschnitt.html) | 2 | 16,77 | 33,54 | shop.bohrers.de | verified 10.09.2026; X beams, max cut 1450 mm |
| Frame | [Aluprofil 2040 V-Slot Nut 6 black, cut 800 mm (cross beam)](https://shop.bohrers.de/V-Slot-2040-Zuschnitt.html) | 1 | 10,32 | 10,32 | shop.bohrers.de | verified 10.09.2026 |
| Frame | [V-Slot 2020 profile, black, 1 m (end tie, cut to 800 mm)](https://www.roboter-bausatz.de/p/v-slot-aluminiumprofil-2020-1-meter-schwarz) | 1 | 5,95 | 5,95 | roboter-bausatz.de | verified 10.09.2026 |
| Frame | [2020 Winkel Nut 6 mit Nutfuehrung, silver (brackets)](https://www.roboter-bausatz.de/p/2020-winkel-fuer-aluminiumprofile-nut-6-mit-nutfuehrung-silber) | 20 | 0,55 | 11,00 | roboter-bausatz.de | verified 10.09.2026; 0,55 € from 20 pcs |
| Frame | [Nutenstein M5 Nut 6, slide-in (T-nuts)](https://www.roboter-bausatz.de/p/nutenstein-m5-nut-6-einschiebbar) | 50 | 0,25 | 12,50 | roboter-bausatz.de | verified 10.09.2026; 0,25 € from 100 pcs -> order 100 |
| Frame | [20x M5 Hammerkopfschraube Nut 6, 10 mm (T-head bolts, 5 packs = 100)](https://www.roboter-bausatz.de/p/20x-m5-hammerkopfschraube-nut-6-10mm) | 5 | 1,49 | 7,45 | roboter-bausatz.de | verified 10.09.2026 |
| Linear | [Solid Delrin V Wheel Kit (wheel + 2x 625 bearings + shim + nut + screw)](https://www.roboter-bausatz.de/p/solid-delrin-v-wheel-kit-fuer-openbuilds-v-slot-rail) | 9 | 4,15 | 37,35 | roboter-bausatz.de | verified 10.09.2026; Dual V-Wheel Kit at 2,65 €/pc saves 13,50 € |
| Linear | [Exzentrischer Abstandshalter 5 mm (eccentric spacers)](https://www.roboter-bausatz.de/p/exzentrischer-abstandshalter-fuer-v-slot-rollen-5mm-bohrung) | 6 | 1,29 | 7,74 | roboter-bausatz.de | verified 10.09.2026; never included in wheel kits |
| Linear | [MGN12 linear rail, cut 800 mm (35,00 €/m) - Z column](https://shop.bohrers.de/linearfuehrung-fuer-mgn12.html) | 1 | 28,00 | 28,00 | shop.bohrers.de | verified 10.09.2026; ships oiled, clean and re-lube |
| Linear | [MGN12H carriage / Lagerbock](https://shop.bohrers.de/mgn12h-lagerbock.html) | 1 | 11,00 | 11,00 | shop.bohrers.de | verified 10.09.2026 |
| Motion | [NEMA17 stepper 17HS4417P1, 1.7 A, 40 Ncm, 40 mm (X, Y, Z)](https://www.roboter-bausatz.de/p/nema-17-schrittmotor-17hs4417p1-2.6v-1.7a-40mm) | 3 | 15,54 | 46,62 | roboter-bausatz.de | verified 10.09.2026 |
| Motion | [NEMA17 planetary gearbox 5:1, 44 Ncm, 1.68 A (wrist, carousel)](https://www.oyostepper.de/goods-298-NEMA-17-Planetengetriebe-Schrittmotor-5-1-Nema17-28V-44Ncm-035-Grad-168A-Getriebe-Schrittmotor.html) | 2 | 32,38 | 64,76 | oyostepper.de | verified 10.09.2026; no German shop consolidates this |
| Motion | [GT2 open timing belt 6 mm, 10 m](https://www.roboter-bausatz.de/p/10-meter-gt2-zahnriemen-offen-6mm) | 1 | 9,99 | 9,99 | roboter-bausatz.de | verified 10.09.2026; 10 m cheaper than the 5 m rolls |
| Motion | [GT2 pulley 20T, bore 5 mm, for 6 mm belt](https://www.roboter-bausatz.de/p/gt2-riemenscheibe-20-zaehne-5mm-bohrung-fuer-6mm-riemen) | 4 | 0,77 | 3,08 | roboter-bausatz.de | verified 10.09.2026 |
| Motion | [GT2 idler 20T, bore 5 mm, dual ball bearing](https://www.roboter-bausatz.de/p/gt2-riemenscheibe-20-zaehne-5mm-bohrung-mit-dual-kugellager) | 4 | 1,55 | 6,20 | roboter-bausatz.de | verified 10.09.2026 |
| Motion | [Smooth Idler Spannrolle Kit (belt tensioner)](https://www.roboter-bausatz.de/p/smooth-idler-spannrolle-kit) | 2 | 5,15 | 10,30 | roboter-bausatz.de | verified 10.09.2026 |
| Motion | [Trapezgewindespindel T8 800x8 mm with brass nut](https://www.roboter-bausatz.de/p/trapezgewindespindel-800x8mm-mit-messingmutter) | 1 | 15,29 | 15,29 | roboter-bausatz.de | verified 10.09.2026 |
| Motion | [Shaft coupling 5 mm -> 8 mm (rigid)](https://www.roboter-bausatz.de/p/wellenkupplung-5mm-auf-8mm) | 1 | 1,99 | 1,99 | roboter-bausatz.de | verified 10.09.2026; flexible jaw coupler out of stock at RB |
| Motion | [KFL08 flange bearing block, 2 pcs](https://www.roboter-bausatz.de/p/kfl08-stehlager-mit-flansch-2-stueck) | 1 | 2,87 | 2,87 | roboter-bausatz.de | verified 10.09.2026 |
| Servos | [Actuonix PQ12-S micro linear actuator, 20 mm stroke, limit switches](https://www.nodna.de/Actuonix-PQ12-S-Micro-Linear-Actuator-Linear-Servo-Actuator-with-Limit-Switches_1) | 1 | 123,49 | 123,49 | nodna.de | verified 10.09.2026; BOM budgets 12 € - see note 3, MG996R servo + printed linkage = 6,65 € |
| Controller | [BIGTREETECH BIQU Octopus V1.1 mainboard](https://www.roboter-bausatz.de/p/bigtreetech-biqu-octopus-v1.1-3d-drucker-mainboard) | 1 | 65,95 | 65,95 | roboter-bausatz.de | verified 10.09.2026 |
| Controller | [5x BIGTREETECH TMC2209 V1.3 UART incl. heatsinks](https://www.roboter-bausatz.de/p/5x-bigtreetech-tmc2209-v1.3-schrittmotortreiber-uart) | 1 | 25,75 | 25,75 | roboter-bausatz.de | verified 10.09.2026; 5-pack saves 3,70 € vs singles |
| Power | [MEAN WELL LRS-150-24, 24 V / 6.5 A / 150 W](https://www.reichelt.de/de/de/shop/produkt/schaltnetzteile_156_w_24_v_6_5_a-202987) | 1 | 18,50 | 18,50 | reichelt.de | verified 10.09.2026; Pollin has it at 17,40 € - not worth a 13th order |
| Power | [Mini step-down module 3 A, 4.5-28 V in -> 5 V](https://www.roboter-bausatz.de/p/mini-spannungswandler-step-down-modul-3a) | 1 | 1,29 | 1,29 | roboter-bausatz.de | verified 10.09.2026 |
| Computer | Raspberry Pi 4 Model B rev 1.1, 2 GB RAM (2 on hand; 2nd = cold spare) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - saves 120,60 € and dodges the Pi 5 backorder. REV 1.1 WARNING: refuses power from e-marked USB-C cables; use the official PSU or a plain cable. Verify: cat /proc/cpuinfo -> a03111 |
| Computer | Official Raspberry Pi 15W USB-C PSU (Pi 4 takes 15 W, not 27 W) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED presumed - check you still have the Pi 4 supplies. Do NOT run the Pi off the servo 5 V buck: an MG996R stalls at ~2.5 A and will brown out the Pi |
| Computer | microSD card 32 GB (OS, Klipper, orchestrator, logs only) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - 32 GB is ample; nothing the machine records is written to it |
| Computer | External USB 3.0 SSD for the WAV files, >=500 GB | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED / to hand. ~860 MB per side, ~40 GB per full 24-slot magazine. SSD not HDD: a bus-powered 2.5in HDD pulls ~0.9 A on spin-up and is a vibration source next to the turntable |
| Computer | Self-powered USB 3.0 hub (Scarlett + SSD + webcam + relay card) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - the Pi 4 budgets only ~1.2 A across all four ports. Route everything through the powered hub, and pin device names with udev rules so /dev/video* and the ALSA index do not shuffle on reboot |
| Cameras | [Raspberry Pi Camera Module 3, 12 MP (deck camera)](https://www.welectron.com/Official-Raspberry-Pi-Camera-Module-3) | 1 | 25,90 | 25,90 | welectron.com | verified 10.09.2026; only one needed now - the Pi 4B has a single CSI port |
| Cameras | [Raspberry Pi camera cable Standard-Mini, 500 mm](https://www.berrybase.de/raspberry-pi-camera-cable-standard-mini-500mm) | 1 | 3,50 | 3,50 | berrybase.de | verified 10.09.2026; the 200 mm cable in the box may already reach; Pi 4 uses the standard 15-pin, no adapter needed |
| Cameras | Trust HD1080p USB webcam (wrist camera) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - replaces the 2nd Cam Module 3 AND the CSI-HDMI extender. Lock focus, exposure, gain and white balance before use; check what the model exposes: v4l2-ctl -d /dev/video0 --list-ctrls-menus |
| Vacuum | [Miniature diaphragm vacuum pump 12 V DC, 3 W, ca. 80 kPa](https://funduinoshop.com/en/electronic-modules/valves-pumps/pumps/miniature-diaphragm-vacuum-pump-12v-dc-3w) | 1 | 10,59 | 10,59 | funduinoshop.com | verified 10.09.2026; 16 in stock |
| Vacuum | [2/2-way solenoid valve G 1/8 NC, FKM, 12 V, direct acting (DA142426)](https://www.druckluft-fachhandel.de/2-2-wege-magnetventil-g-1-8-stromlos-geschlossen-nc-fkm-12v) | 1 | 42,44 | 42,44 | druckluft-fachhandel.de | verified 10.09.2026; MUST be direct acting - pilot valves do not open under vacuum |
| Vacuum | [Adafruit MPRLS pressure sensor breakout 0-25 PSI, I2C](https://www.berrybase.de/adafruit-mprls-drucksensor-breakout-mit-anschluss-0-bis-25-psi) | 1 | 30,90 | 30,90 | berrybase.de | verified 10.09.2026; OUT OF STOCK. Industrial vacuum switch = 95,30 € |
| Vacuum | [Balgensauger D 40 mm, 1.5 folds, NBR, with G 1/4 fitting](https://morali.de/vakuumsauger/balgensauger/19/bellows-suction-cup-d-40-mm-1-5-folds-with-fit) | 1 | 21,37 | 21,37 | morali.de | verified 10.09.2026; or print the cup lip in TPU per the BOM printed-parts list |
| Vacuum | [Polyurethane tube 6 x 4 mm, natural, per metre](https://www.druckluft-fachhandel.de/polyurethan-schlauch-6-x-4-mm-natur) | 5 | 1,05 | 5,25 | druckluft-fachhandel.de | verified 10.09.2026 |
| Vacuum | [Straight push-in fitting G 1/8 - 6 mm, IQS, -0.95 to 20 bar](https://www.druckluft-fachhandel.de/gerader-steckanschluss-g-1-8-6mm-iqs-standard) | 8 | 1,38 | 11,04 | druckluft-fachhandel.de | verified 10.09.2026; vacuum rated |
| Sensing | [3x mechanical end-stop with 50 cm cable, 3-pin](https://www.roboter-bausatz.de/p/3er-set-mechanischer-endschalter-mit-50-cm-kabelsatz-3-pin-fuer-cnc-reprap-3d-drucker) | 1 | 3,49 | 3,49 | roboter-bausatz.de | verified 10.09.2026 |
| Sensing | [Mechanical end-stop with 50 cm cable, single](https://www.roboter-bausatz.de/p/mechanischer-endschalter-mit-50-cm-kabelsatz-3-pin-fuer-cnc-reprap-3d-drucker) | 2 | 0,75 | 1,50 | roboter-bausatz.de | verified 10.09.2026 |
| Sensing | [Hall magnetic sensor module KY-003 (A3144), digital](https://www.berrybase.de/berrybase-hall-magnetic-sensor-module-ky-003-digitaler-ausgang-hall-effekt-arduino-3.3-5v) | 1 | 0,90 | 0,90 | berrybase.de | verified 10.09.2026; 100+ in stock |
| Sensing | [KY-010 photo interrupter / slot optical sensor module](https://www.roboter-bausatz.de/p/ky-010-lichtschranke-modul) | 1 | 1,25 | 1,25 | roboter-bausatz.de | verified 10.09.2026 |
| Deck I/O | [NFKE MG 63 audio cable, 6.3 mm mono jack, 1.8 m (cut one end)](https://www.reichelt.de/de/de/shop/produkt/nf-kabel_6_3_mm_mono_klinkenstecker_gerade_1_8_m_2-pol-109580) | 1 | 1,56 | 1,56 | reichelt.de | verified 10.09.2026; remote start/stop jack |
| Light | [LED strip warm white, 12 V, 5 m (cut to 50 cm)](https://www.reichelt.de/de/de/shop/produkt/led-streifen_warmweiss_5000_mm-235875) | 1 | 5,85 | 5,85 | reichelt.de | verified 10.09.2026 |
| Light | [INFINEON IRLZ44N logic-level MOSFET, N-Ch 55 V 47 A, TO-220](https://www.reichelt.de/de/de/shop/produkt/mosfet_n-ch_55v_47a_110w_to-220ab-129819) | 2 | 0,67 | 1,34 | reichelt.de | verified 10.09.2026; do NOT use IRF520 modules - not logic level |
| Carousel | [Miniature ball bearing 608-ZZ 8x22x7 mm (rollers)](https://www.dold-mechatronik.de/Miniature-ball-bearings-608-ZZ-8x22x7-mm) | 10 | 0,79 | 7,90 | dold-mechatronik.de | verified 10.09.2026 |
| Carousel | [Deep groove ball bearing 6005-2RS 25x47x12 mm](https://www.dold-mechatronik.de/Deep-groove-ball-bearings-6005-2RS-25x47x12-mm) | 1 | 1,79 | 1,79 | dold-mechatronik.de | verified 10.09.2026; cheaper than Kugellager-Express at 2,08 € |
| Carousel | [Precision shaft 25 mm h6, hardened, cut 100 mm (stub shaft)](https://www.dold-mechatronik.de/Precision-shaft-25mm-h6,-ground-and-hardened,-material-CF53-(1.1213),-3.85kg-m,-cut-50-3000mm) | 1 | 3,29 | 3,29 | dold-mechatronik.de | verified 10.09.2026 |
| Cabling | [Energiekette 10x20 R28, open, 1 m (end brackets included)](https://www.cnc-zubehoer.eu/1-m-Energiekette-Schleppkette-leicht-offen-10x20-R28/EK.10x20.R28.o) | 3 | 5,61 | 16,83 | cnc-zubehoer.eu | verified 10.09.2026; cheapest chain found; Dold CK10 is 9,57 €/m plus connectors |
| Cabling | [610-piece Dupont crimp connector set in box](https://www.berrybase.de/en/610-piece-dupont-crimp-connector-set-in-plastic-box) | 1 | 9,90 | 9,90 | berrybase.de | verified 10.09.2026 |
| Cabling | [200-piece jumper wire connector kit, JST-SM / Dupont 2.54 mm](https://www.berrybase.de/en/berrybase-200-piece-jumper-wire-connector-kit-jst-sm-dupont-2.54mm-2-5-pin-male-female) | 1 | 3,90 | 3,90 | berrybase.de | verified 10.09.2026 |
| Cabling | [Silicone wire 20 AWG, red + black, per metre](https://www.roboter-bausatz.de/search?search=silikonkabel) | 10 | 1,55 | 15,50 | roboter-bausatz.de | verified 10.09.2026 |
| Cabling | [Heat shrink assortment Delock 86278, 230 pcs, 1.5-13 mm](https://www.reichelt.de/de/de/shop/produkt/schrumpfschlauch_sortiment_-_230-teilig_farbig_box-167391) | 1 | 6,99 | 6,99 | reichelt.de | verified 10.09.2026 |
| Hardware | [Hex socket screw / nut / washer assortment, 520 pcs, M3-M6, stainless](https://www.roboter-bausatz.de/p/sortiment-innensechskantschrauben-set-520-teile) | 1 | 18,70 | 18,70 | roboter-bausatz.de | verified 10.09.2026 |
| Hardware | [ruthex M3x5.7 heat-set threaded inserts, 100 pcs](https://www.reichelt.com/de/en/shop/product/3d_printing_threaded_inserts_m3x5_7_pack_of_100-332213) | 1 | 8,99 | 8,99 | reichelt.de | verified 10.09.2026; same price at 3DJake |

Totals for this route: parts 821,60 €, shipping 67,15 €, delivered **888,75 €**.

### Shipping

| Supplier | Order value € | Shipping € | Rule |
|---|---|---|---|
| shop.bohrers.de | 82,86 | 12,90 | Long goods >1 m - estimate, cart shows final |
| roboter-bausatz.de | 311,76 | 0,00 | Free from 99 € gross - reached |
| dold-mechatronik.de | 12,98 | 6,90 | DHL up to 1 m, <=2 kg: 6,90 €. No free threshold |
| berrybase.de | 49,10 | 4,95 | DHL 4,95 €; free from 150 € - not reached |
| reichelt.de | 43,23 | 5,95 | DHL <=10 kg 5,95 €. No free threshold |
| oyostepper.de | 64,76 | 6,90 | Estimate - no published rate |
| welectron.com | 25,90 | 4,95 | DPD 4,95 € - basket now under the 49 € free threshold (one camera instead of two plus extender) |
| nodna.de | 123,49 | 0,00 | Free within DE from 90 € - reached |
| funduinoshop.com | 10,59 | 4,90 | Estimate |
| druckluft-fachhandel.de | 58,73 | 6,90 | Estimate |
| morali.de | 21,37 | 6,90 | Estimate |
| cnc-zubehoer.eu | 16,83 | 5,90 | Estimate |

### Notes

- Prices verified by fetching the live product pages on 10.09.2026, incl. 19% German VAT, excl. shipping. Anything marked ESTIMATE could not be fetched (Amazon and Conrad block automated access) - check before ordering.
- Plywood, bench top and Baumarkt items are NOT in this list (your decision). Budget ~60 € locally for the 18 mm birch plywood sheet. Filament (PETG 2.5 kg + TPU 0.3 kg, ~70 €) is also not included.
- Biggest deviation from the BOM: the micro linear servo. The BOM budgets 12 €, but no sub-30 € linear servo is in stock at any German/EU shop. Verified options start at 90-123 €. An MG996R servo (6,65 € at roboter-bausatz.de) plus a printed pusher rod does the same job - that is what sheet 2 uses.
- Second deviation: the BOM's 12 € vacuum switch. Industrial vacuum switches start at 95 € in Germany. The Adafruit MPRLS absolute pressure sensor (30,90 €) plus a software threshold replaces it.
- The Raspberry Pi line is gone: the build now runs on a Pi 4B 2 GB you already own. That also sidesteps the Pi 5 4 GB being out of stock at BerryBase, welectron and rasppishop, with Reichelt backordered to 27.10.2026. The trade is roughly 2 to 2.5x less CPU, which the workload absorbs - the only sustained vision load is the deck camera tracking the headshell in a known ROI, so keep those frames downscaled to around 640x480 at 10-15 fps and process the 12 MP label shots one at a time.
- Motedis carries no true V-slot profile (only B-Typ / I-Typ). It cannot be used for the wheel-running beams.
- This sheet buys every line as the BOM literally specifies it, each at its cheapest verified source - 12 suppliers, 12 parcels. Sheet 2 lands about 100 € LOWER, which is not a consolidation discount: about 117 € of it is the servo substitution and about 16 € the printed suction cup, offset by roughly 28 € of consolidation premium on rails, cameras and cable chain, and about 30 € less shipping. On identical parts the two sheets are within about 30 € of each other.
- ALREADY OWNED, shown as 0,00 € rows: 2x Raspberry Pi 4B rev 1.1 / 2 GB (one is the cold spare), their 32 GB cards and 15 W supplies, an external USB 3.0 SSD, a self-powered USB 3.0 hub, and the Trust HD1080p webcam as the wrist camera. Together that removes roughly 185 to 195 € depending on the sheet. Also already on hand and never in these lists: the Omnitronic DD 3120, the Focusrite Scarlett, the Conrad 393905 relay card and the 3D printer.
- Three Pi 4 gotchas worth reading before you wire anything: rev 1.1 boards refuse e-marked USB-C cables (use the official supply); rev 1.1 puts the SD-card voltage regulator on the underside next to the slot where it can be knocked off, so set the card up once and leave it; and the enclosed electronics box needs a heatsink and a fan on a Pi 4 under sustained vision load.
- Put the Scarlett, the SSD, the webcam and the relay card on the powered hub, not on the Pi. The Pi 4 budgets roughly 1.2 A across all four ports and this machine runs unattended for a weekend - a brown-out mid-side is a lost recording. Pin every device with a udev rule so /dev/video* and the ALSA card index do not shuffle across reboots.

## Fewest suppliers

Same build, consolidated into 6 orders instead of 12. Prices incl. 19% VAT, verified 10 September 2026.

| Group | Part | Qty | Unit € | Line € | Supplier | Note |
|---|---|---|---|---|---|---|
| Frame | [Aluprofil 20x40 V-Typ Nut 6, cut 1300 mm (14,00 €/m + 0,50 € cut)](https://www.dold-mechatronik.de/Aluminiumprofil-20x40-V-Typ-Nut-6-062kg-m-Zuschnitt-50-6000mm) | 2 | 18,70 | 37,40 | dold-mechatronik.de | verified 10.09.2026; price basis €/m + cut fee confirmed on page |
| Frame | [Aluprofil 20x40 V-Typ Nut 6, cut 800 mm](https://www.dold-mechatronik.de/Aluminiumprofil-20x40-V-Typ-Nut-6-062kg-m-Zuschnitt-50-6000mm) | 1 | 11,70 | 11,70 | dold-mechatronik.de | verified 10.09.2026 |
| Frame | [Aluprofil 20x20 V-Typ Nut 6, cut 800 mm (8,00 €/m + 0,50 € cut)](https://www.dold-mechatronik.de/Aluminiumprofil-20x20-V-Typ-Nut-6-044kg-m-Zuschnitt-50-6000mm) | 1 | 6,90 | 6,90 | dold-mechatronik.de | verified 10.09.2026 |
| Frame | [Innenwinkel Stahl verzinkt 20 Nut 6, incl. 2x M4x6](https://www.dold-mechatronik.de/Winkel-und-Verbinder-20-B-Typ-Nut-6) | 20 | 1,18 | 23,60 | dold-mechatronik.de | verified 10.09.2026 |
| Frame | [Nutenstein M5 Nut 6, slide-in (T-nuts)](https://www.roboter-bausatz.de/p/nutenstein-m5-nut-6-einschiebbar) | 50 | 0,25 | 12,50 | roboter-bausatz.de | verified 10.09.2026; Dold charges 0,81 €/pc - 28 € more |
| Frame | [20x M5 Hammerkopfschraube Nut 6, 10 mm (5 packs = 100)](https://www.roboter-bausatz.de/p/20x-m5-hammerkopfschraube-nut-6-10mm) | 5 | 1,49 | 7,45 | roboter-bausatz.de | verified 10.09.2026 |
| Linear | [Solid Delrin V Wheel Kit](https://www.roboter-bausatz.de/p/solid-delrin-v-wheel-kit-fuer-openbuilds-v-slot-rail) | 9 | 4,15 | 37,35 | roboter-bausatz.de | verified 10.09.2026; Dold's Rad D24x11 is unconfirmed as V-profile - do not risk it |
| Linear | [Exzentrischer Abstandshalter 5 mm (eccentric spacers)](https://www.roboter-bausatz.de/p/exzentrischer-abstandshalter-fuer-v-slot-rollen-5mm-bohrung) | 6 | 1,29 | 7,74 | roboter-bausatz.de | verified 10.09.2026 |
| Linear | [Linearfuehrung MGN12R, 800 mm](https://www.dold-mechatronik.de/Linear-Guide-MGN12R-800mm) | 1 | 37,60 | 37,60 | dold-mechatronik.de | verified 10.09.2026; 9,60 € more than bohrers, saves one supplier |
| Linear | [Linearwagen MGN12H](https://www.dold-mechatronik.de/Linear-carriage-MGN12H) | 1 | 13,00 | 13,00 | dold-mechatronik.de | verified 10.09.2026 |
| Motion | [NEMA17 stepper 17HS4417P1, 1.7 A, 40 Ncm (X, Y, Z)](https://www.roboter-bausatz.de/p/nema-17-schrittmotor-17hs4417p1-2.6v-1.7a-40mm) | 3 | 15,54 | 46,62 | roboter-bausatz.de | verified 10.09.2026 |
| Motion | [NEMA17 planetary gearbox 5:1, 44 Ncm (wrist, carousel)](https://www.oyostepper.de/goods-298-NEMA-17-Planetengetriebe-Schrittmotor-5-1-Nema17-28V-44Ncm-035-Grad-168A-Getriebe-Schrittmotor.html) | 2 | 32,38 | 64,76 | oyostepper.de | verified 10.09.2026; the one line that cannot be consolidated - see note 2 |
| Motion | [GT2 timing belt 6 mm, per metre](https://www.dold-mechatronik.de/Toothed-belt-GT2,-width-6mm-meter,-length-selectable) | 5 | 2,50 | 12,50 | dold-mechatronik.de | verified 10.09.2026 |
| Motion | [GT2 pulley 20T, bore 5.00 mm H7, with clamping screws](https://www.dold-mechatronik.de/Toothed-belt-GT2-6mm-wide-20-teeth,-bore-5.00mm-H7-with-clamping-screws) | 4 | 2,90 | 11,60 | dold-mechatronik.de | verified 10.09.2026 |
| Motion | [Deflection pulley (smooth idler) 6 mm, D 12.73 mm, bore 5.00 mm](https://www.dold-mechatronik.de/6mm-wide-deflection-pulley-for-timing-belt-12,73mm-diameter,-bore-5.00mm) | 4 | 3,20 | 12,80 | dold-mechatronik.de | verified 10.09.2026; genuinely smooth, better than a toothed idler |
| Motion | [Smooth Idler Spannrolle Kit (belt tensioner)](https://www.roboter-bausatz.de/p/smooth-idler-spannrolle-kit) | 2 | 5,15 | 10,30 | roboter-bausatz.de | verified 10.09.2026 |
| Motion | [Trapezgewindespindel T8 800x8 mm with brass nut](https://www.roboter-bausatz.de/p/trapezgewindespindel-800x8mm-mit-messingmutter) | 1 | 15,29 | 15,29 | roboter-bausatz.de | verified 10.09.2026; Dold has no 8x8 pitch |
| Motion | [Shaft coupling 5 mm -> 8 mm (rigid)](https://www.roboter-bausatz.de/p/wellenkupplung-5mm-auf-8mm) | 1 | 1,99 | 1,99 | roboter-bausatz.de | verified 10.09.2026 |
| Motion | [KFL08 flange bearing block, 2 pcs](https://www.roboter-bausatz.de/p/kfl08-stehlager-mit-flansch-2-stueck) | 1 | 2,87 | 2,87 | roboter-bausatz.de | verified 10.09.2026 |
| Servos | [MG996R digital servo, metal gears (cue lever, with printed pusher rod)](https://www.roboter-bausatz.de/p/mg996r-digital-servo-motor-mit-metall-getriebe) | 1 | 6,65 | 6,65 | roboter-bausatz.de | verified 10.09.2026; SUBSTITUTE for the linear servo - saves 117 € and one supplier |
| Controller | [BIGTREETECH BIQU Octopus V1.1 mainboard](https://www.roboter-bausatz.de/p/bigtreetech-biqu-octopus-v1.1-3d-drucker-mainboard) | 1 | 65,95 | 65,95 | roboter-bausatz.de | verified 10.09.2026 |
| Controller | [5x BIGTREETECH TMC2209 V1.3 UART incl. heatsinks](https://www.roboter-bausatz.de/p/5x-bigtreetech-tmc2209-v1.3-schrittmotortreiber-uart) | 1 | 25,75 | 25,75 | roboter-bausatz.de | verified 10.09.2026 |
| Power | [MEAN WELL LRS-150-24, 24 V / 6.5 A / 150 W](https://www.reichelt.de/de/de/shop/produkt/schaltnetzteile_156_w_24_v_6_5_a-202987) | 1 | 18,50 | 18,50 | reichelt.de | verified 10.09.2026 |
| Power | [Mini step-down module 3 A -> 5 V](https://www.roboter-bausatz.de/p/mini-spannungswandler-step-down-modul-3a) | 1 | 1,29 | 1,29 | roboter-bausatz.de | verified 10.09.2026 |
| Computer | Raspberry Pi 4 Model B rev 1.1, 2 GB RAM (2 on hand; 2nd = cold spare) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - saves 118,50 €. REV 1.1: refuses e-marked USB-C cables, use the official PSU. Verify: cat /proc/cpuinfo -> a03111 |
| Computer | Official Raspberry Pi 15W USB-C PSU (Pi 4 takes 15 W, not 27 W) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED presumed. Do NOT run the Pi off the servo 5 V buck - an MG996R stalls at ~2.5 A |
| Computer | microSD card 32 GB (OS, Klipper, orchestrator, logs only) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - nothing the machine records goes on it |
| Computer | External USB 3.0 SSD for the WAV files, >=500 GB | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED / to hand. ~860 MB per side, ~40 GB per magazine. SSD not HDD - spin-up current and vibration |
| Computer | Self-powered USB 3.0 hub (Scarlett + SSD + webcam + relay card) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - Pi 4 gives only ~1.2 A across all ports. Pin device names with udev rules |
| Cameras | [Raspberry Pi Camera Module 3, 12 MP (deck camera)](https://www.berrybase.de/raspberry-pi-camera-module-3-12mp) | 1 | 28,90 | 28,90 | berrybase.de | verified 10.09.2026; only one needed - the Pi 4B has a single CSI port |
| Cameras | [Raspberry Pi camera cable Standard-Mini, 500 mm (deck camera)](https://www.berrybase.de/raspberry-pi-camera-cable-standard-mini-500mm) | 1 | 3,50 | 3,50 | berrybase.de | verified 10.09.2026; the 200 mm cable in the box may already reach |
| Cameras | Trust HD1080p USB webcam (wrist camera) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - one CSI port means the wrist camera goes USB, which docs/03 already sanctions as simpler and adequate. Lock focus/exposure/gain/WB: v4l2-ctl -d /dev/video0 --list-ctrls-menus |
| Vacuum | [Mikro Membran-Vakuumpumpe 12 V (YW11-DC12), 1 L/min](https://www.berrybase.de/mikro-membran-vakuumpumpe-fuer-gas-fluessigkeiten-12v) | 1 | 11,40 | 11,40 | berrybase.de | verified 10.09.2026; currently not available - Funduinoshop has one at 10,59 € |
| Vacuum | [2/2-way solenoid valve G 1/8 NC, FKM, 12 V, direct acting](https://www.druckluft-fachhandel.de/2-2-wege-magnetventil-g-1-8-stromlos-geschlossen-nc-fkm-12v) | 1 | 42,44 | 42,44 | druckluft-fachhandel.de | verified 10.09.2026 |
| Vacuum | [Adafruit MPRLS pressure sensor breakout 0-25 PSI, I2C](https://www.berrybase.de/adafruit-mprls-drucksensor-breakout-mit-anschluss-0-bis-25-psi) | 1 | 30,90 | 30,90 | berrybase.de | verified 10.09.2026; out of stock |
| Vacuum | [Saugeranschlussnippel NW 2.40 mm, G 1/8 AG (cup lip printed in TPU)](https://www.druckluft-fachhandel.de/saugeranschlussnippel-nw-2-40-mm-g-1-8-ag-laenge-5-mm-108465) | 1 | 5,00 | 5,00 | druckluft-fachhandel.de | ESTIMATE - not verified; the BOM lists the TPU cup lip as a printed part |
| Vacuum | [Polyurethane tube 6 x 4 mm, natural, per metre](https://www.druckluft-fachhandel.de/polyurethan-schlauch-6-x-4-mm-natur) | 5 | 1,05 | 5,25 | druckluft-fachhandel.de | verified 10.09.2026 |
| Vacuum | [Straight push-in fitting G 1/8 - 6 mm, IQS](https://www.druckluft-fachhandel.de/gerader-steckanschluss-g-1-8-6mm-iqs-standard) | 8 | 1,38 | 11,04 | druckluft-fachhandel.de | verified 10.09.2026 |
| Sensing | [3x mechanical end-stop with 50 cm cable, 3-pin](https://www.roboter-bausatz.de/p/3er-set-mechanischer-endschalter-mit-50-cm-kabelsatz-3-pin-fuer-cnc-reprap-3d-drucker) | 1 | 3,49 | 3,49 | roboter-bausatz.de | verified 10.09.2026 |
| Sensing | [Mechanical end-stop with 50 cm cable, single](https://www.roboter-bausatz.de/p/mechanischer-endschalter-mit-50-cm-kabelsatz-3-pin-fuer-cnc-reprap-3d-drucker) | 2 | 0,75 | 1,50 | roboter-bausatz.de | verified 10.09.2026 |
| Sensing | [Hall magnetic sensor module KY-003 (A3144)](https://www.berrybase.de/berrybase-hall-magnetic-sensor-module-ky-003-digitaler-ausgang-hall-effekt-arduino-3.3-5v) | 1 | 0,90 | 0,90 | berrybase.de | verified 10.09.2026 |
| Sensing | [KY-010 photo interrupter / slot optical sensor module](https://www.roboter-bausatz.de/p/ky-010-lichtschranke-modul) | 1 | 1,25 | 1,25 | roboter-bausatz.de | verified 10.09.2026 |
| Deck I/O | [NFKE MG 63 audio cable, 6.3 mm mono jack, 1.8 m](https://www.reichelt.de/de/de/shop/produkt/nf-kabel_6_3_mm_mono_klinkenstecker_gerade_1_8_m_2-pol-109580) | 1 | 1,56 | 1,56 | reichelt.de | verified 10.09.2026 |
| Light | [LED strip warm white, 12 V, 5 m](https://www.reichelt.de/de/de/shop/produkt/led-streifen_warmweiss_5000_mm-235875) | 1 | 5,85 | 5,85 | reichelt.de | verified 10.09.2026 |
| Light | [INFINEON IRLZ44N logic-level MOSFET, TO-220](https://www.reichelt.de/de/de/shop/produkt/mosfet_n-ch_55v_47a_110w_to-220ab-129819) | 2 | 0,67 | 1,34 | reichelt.de | verified 10.09.2026 |
| Carousel | [Miniature ball bearing 608-ZZ 8x22x7 mm](https://www.dold-mechatronik.de/Miniature-ball-bearings-608-ZZ-8x22x7-mm) | 10 | 0,79 | 7,90 | dold-mechatronik.de | verified 10.09.2026 |
| Carousel | [Deep groove ball bearing 6005-2RS 25x47x12 mm](https://www.dold-mechatronik.de/Deep-groove-ball-bearings-6005-2RS-25x47x12-mm) | 1 | 1,79 | 1,79 | dold-mechatronik.de | verified 10.09.2026 |
| Carousel | [Precision shaft 25 mm h6, hardened, cut 100 mm](https://www.dold-mechatronik.de/Precision-shaft-25mm-h6,-ground-and-hardened,-material-CF53-(1.1213),-3.85kg-m,-cut-50-3000mm) | 1 | 3,29 | 3,29 | dold-mechatronik.de | verified 10.09.2026 |
| Cabling | [Energiekette CK10, 20 mm wide, 1000 mm, inner 10x20](https://www.dold-mechatronik.de/Energy-chain-CK-10-20mm-wide-1000mm-chain-length-without-connecting-elements) | 3 | 9,57 | 28,71 | dold-mechatronik.de | verified 10.09.2026; 12 € more than cnc-zubehoer, saves a supplier |
| Cabling | [Energiekette CK10 connection elements, 1 pair](https://www.dold-mechatronik.de/Energy-chain-CK-10-20mm-wide-connection-elements-1-pair) | 2 | 2,50 | 5,00 | dold-mechatronik.de | verified 10.09.2026; not included with the chain |
| Cabling | [610-piece Dupont crimp connector set in box](https://www.berrybase.de/en/610-piece-dupont-crimp-connector-set-in-plastic-box) | 1 | 9,90 | 9,90 | berrybase.de | verified 10.09.2026 |
| Cabling | [200-piece jumper wire connector kit, JST-SM / Dupont](https://www.berrybase.de/en/berrybase-200-piece-jumper-wire-connector-kit-jst-sm-dupont-2.54mm-2-5-pin-male-female) | 1 | 3,90 | 3,90 | berrybase.de | verified 10.09.2026 |
| Cabling | [Silicone wire 20 AWG, red + black, per metre](https://www.roboter-bausatz.de/search?search=silikonkabel) | 10 | 1,55 | 15,50 | roboter-bausatz.de | verified 10.09.2026 |
| Cabling | [Nylon braided sleeving 15 mm, per metre](https://www.roboter-bausatz.de/search?search=gewebeschlauch) | 5 | 0,32 | 1,60 | roboter-bausatz.de | verified 10.09.2026 |
| Cabling | [Heat shrink assortment Delock 86278, 230 pcs](https://www.reichelt.de/de/de/shop/produkt/schrumpfschlauch_sortiment_-_230-teilig_farbig_box-167391) | 1 | 6,99 | 6,99 | reichelt.de | verified 10.09.2026 |
| Hardware | [Hex socket screw / nut / washer assortment, 520 pcs, M3-M6](https://www.roboter-bausatz.de/p/sortiment-innensechskantschrauben-set-520-teile) | 1 | 18,70 | 18,70 | roboter-bausatz.de | verified 10.09.2026 |
| Hardware | [ruthex M3x5.7 heat-set threaded inserts, 100 pcs](https://www.reichelt.com/de/en/shop/product/3d_printing_threaded_inserts_m3x5_7_pack_of_100-332213) | 1 | 8,99 | 8,99 | reichelt.de | verified 10.09.2026 |

Totals for this route: parts 758,70 €, shipping 37,60 €, delivered **796,30 €**.

### Shipping

| Supplier | Order value € | Shipping € | Rule |
|---|---|---|---|
| dold-mechatronik.de | 213,79 | 12,90 | DPD up to 1.5 m, <=10 kg - required for the 1.3 m profiles |
| roboter-bausatz.de | 283,79 | 0,00 | Free from 99 € gross - reached |
| berrybase.de | 89,40 | 4,95 | DHL 4,95 € - basket now under the 150 € free threshold since the Pi 5 came out |
| reichelt.de | 43,23 | 5,95 | DHL <=10 kg |
| oyostepper.de | 64,76 | 6,90 | Estimate - no published rate |
| druckluft-fachhandel.de | 63,73 | 6,90 | Estimate |

### Notes

- Six suppliers, every part of the BOM covered, six parcels instead of twelve. The delivered total is about 100 € below sheet 1, but read that carefully: consolidating actually COSTS about 28 € on parts (see note 4) and saves about 30 € on shipping - roughly a wash. The 100 € gap comes from the two substitutions in note 3, mainly the 6,65 € servo standing in for the 123,49 € linear actuator. Those substitutions are available on sheet 1 too if you want them there.
- YOUR QUESTION - can it be done with 5? Not for the complete BOM. The one line no German general-purpose shop carries is the NEMA17 with a 5:1 planetary gearbox: roboter-bausatz has none (discontinued), Dold lists only 10:1, BerryBase and Reichelt none at all. Drop to 5 suppliers by either (a) buying 10:1 geared motors from Dold instead of 5:1 - fine for the wrist and the carousel index, both slow axes - or (b) buying the two geared motors from a 6th shop and accepting it. Everything else on this sheet already consolidates.
- Substitutions made to reduce supplier count, each flagged in the Notes column: MG996R servo + printed pusher rod instead of the 123 € Actuonix linear actuator; 50 cm Raspberry Pi camera ribbon instead of the Arducam CSI-HDMI extender pair; TPU-printed cup lip on a bought nipple instead of the 21 € Balgensauger; Dold's energy chain instead of cnc-zubehoer's.
- Extra cost of consolidating, line by line: MGN12 rail +9,60 €, camera modules +6,00 €, energy chain +12,00 €, T-nuts kept at RB to avoid +28 € at Dold. Total parts premium about 28 €, shipping saving about 30 €.
- Dold prices its cut profiles as €/m plus a 0,50 € cutting fee per piece - that is what the unit prices here reflect. Quantity discount of 4.75% applies from 2 pieces of the same configured 20x40 profile.
- Plywood, Baumarkt items and filament are not included, same as sheet 1.
- ALREADY OWNED, shown as 0,00 € rows: 2x Raspberry Pi 4B rev 1.1 / 2 GB (one is the cold spare), their 32 GB cards and 15 W supplies, an external USB 3.0 SSD, a self-powered USB 3.0 hub, and the Trust HD1080p webcam as the wrist camera. Together that removes roughly 185 to 195 € depending on the sheet. Also already on hand and never in these lists: the Omnitronic DD 3120, the Focusrite Scarlett, the Conrad 393905 relay card and the 3D printer.
- Three Pi 4 gotchas worth reading before you wire anything: rev 1.1 boards refuse e-marked USB-C cables (use the official supply); rev 1.1 puts the SD-card voltage regulator on the underside next to the slot where it can be knocked off, so set the card up once and leave it; and the enclosed electronics box needs a heatsink and a fan on a Pi 4 under sustained vision load.
- Put the Scarlett, the SSD, the webcam and the relay card on the powered hub, not on the Pi. The Pi 4 budgets roughly 1.2 A across all four ports and this machine runs unattended for a weekend - a brown-out mid-side is a lost recording. Pin every device with a udev rule so /dev/video* and the ALSA card index do not shuffle across reboots.

## Donor printer route

A used 3D printer supplies the motion hardware; a Pi Pico + 1 TMC2209 replaces the Octopus. Prices incl. 19% VAT, verified 10 September 2026.

| Group | Part | Qty | Unit € | Line € | Supplier | Note |
|---|---|---|---|---|---|---|
| Donor | [Used 3D printer (Creality Ender 3 / CR-10 / Ender 5) as donor](https://www.kleinanzeigen.de/s-3d-drucker/k0) | 1 | 75,00 | 75,00 | eBay Kleinanzeigen / used | ESTIMATE - not verified; local pickup. Supplies 4-5 NEMA17, 24 V PSU, GT2 belt+pulleys+idlers, wheels, carriage plates, end-stops, board |
| Frame | [Aluprofil 20x40 V-Typ Nut 6, cut 1300 mm (X beams - too long for any donor)](https://www.dold-mechatronik.de/Aluminiumprofil-20x40-V-Typ-Nut-6-062kg-m-Zuschnitt-50-6000mm) | 2 | 18,70 | 37,40 | dold-mechatronik.de | verified 10.09.2026 |
| Frame | [Aluprofil 20x40 V-Typ Nut 6, cut 800 mm (cross beam)](https://www.dold-mechatronik.de/Aluminiumprofil-20x40-V-Typ-Nut-6-062kg-m-Zuschnitt-50-6000mm) | 1 | 11,70 | 11,70 | dold-mechatronik.de | verified 10.09.2026; an Ender 5 Plus donor may cover this |
| Frame | [Aluprofil 20x20 V-Typ Nut 6, cut 800 mm (end tie)](https://www.dold-mechatronik.de/Aluminiumprofil-20x20-V-Typ-Nut-6-044kg-m-Zuschnitt-50-6000mm) | 1 | 6,90 | 6,90 | dold-mechatronik.de | verified 10.09.2026 |
| Frame | [Innenwinkel Stahl verzinkt 20 Nut 6, incl. 2x M4x6](https://www.dold-mechatronik.de/Winkel-und-Verbinder-20-B-Typ-Nut-6) | 20 | 1,18 | 23,60 | dold-mechatronik.de | verified 10.09.2026 |
| Frame | [Nutenstein M5 Nut 6, slide-in](https://www.roboter-bausatz.de/p/nutenstein-m5-nut-6-einschiebbar) | 50 | 0,25 | 12,50 | roboter-bausatz.de | verified 10.09.2026 |
| Frame | [20x M5 Hammerkopfschraube Nut 6, 10 mm (5 packs)](https://www.roboter-bausatz.de/p/20x-m5-hammerkopfschraube-nut-6-10mm) | 5 | 1,49 | 7,45 | roboter-bausatz.de | verified 10.09.2026 |
| Linear | V-wheels, eccentric spacers, carriage plates | — | — | 0,00 | from donor printer | FROM DONOR - an Ender 3 carries 9-12 Delrin wheels with eccentrics |
| Linear | [Linearfuehrung MGN12R, 800 mm (Z column - no donor has this)](https://www.dold-mechatronik.de/Linear-Guide-MGN12R-800mm) | 1 | 37,60 | 37,60 | dold-mechatronik.de | verified 10.09.2026 |
| Linear | [Linearwagen MGN12H](https://www.dold-mechatronik.de/Linear-carriage-MGN12H) | 1 | 13,00 | 13,00 | dold-mechatronik.de | verified 10.09.2026 |
| Motion | NEMA17 steppers X, Y, Z | — | — | 0,00 | from donor printer | FROM DONOR - 4 to 5 motors, saves 46,62 € |
| Motion | [NEMA17 planetary gearbox 5:1, 44 Ncm (wrist, carousel)](https://www.oyostepper.de/goods-298-NEMA-17-Planetengetriebe-Schrittmotor-5-1-Nema17-28V-44Ncm-035-Grad-168A-Getriebe-Schrittmotor.html) | 2 | 32,38 | 64,76 | oyostepper.de | verified 10.09.2026; no donor has geared motors |
| Motion | GT2 belt, 20T pulleys, idlers | — | — | 0,00 | from donor printer | FROM DONOR - saves about 30 €. Buy a 5 m belt if the donor's is worn |
| Motion | [Smooth Idler Spannrolle Kit (belt tensioner)](https://www.roboter-bausatz.de/p/smooth-idler-spannrolle-kit) | 2 | 5,15 | 10,30 | roboter-bausatz.de | verified 10.09.2026; donor tensioners rarely fit a new frame |
| Motion | [Trapezgewindespindel T8 800x8 mm with brass nut](https://www.roboter-bausatz.de/p/trapezgewindespindel-800x8mm-mit-messingmutter) | 1 | 15,29 | 15,29 | roboter-bausatz.de | verified 10.09.2026; donor screws are 36-40 cm, too short for the 80 cm Z |
| Motion | [Shaft coupling 5 mm -> 8 mm (rigid)](https://www.roboter-bausatz.de/p/wellenkupplung-5mm-auf-8mm) | 1 | 1,99 | 1,99 | roboter-bausatz.de | verified 10.09.2026; donor may supply one |
| Motion | [KFL08 flange bearing block, 2 pcs](https://www.roboter-bausatz.de/p/kfl08-stehlager-mit-flansch-2-stueck) | 1 | 2,87 | 2,87 | roboter-bausatz.de | verified 10.09.2026 |
| Servos | [MG996R digital servo, metal gears (cue lever)](https://www.roboter-bausatz.de/p/mg996r-digital-servo-motor-mit-metall-getriebe) | 1 | 6,65 | 6,65 | roboter-bausatz.de | verified 10.09.2026 |
| Controller | Donor 32-bit board (Creality 4.2.x) running Klipper - 4 axes | — | — | 0,00 | from donor printer | FROM DONOR - replaces the 65,95 € Octopus |
| Controller | [Raspberry Pi Pico RP2040 (2nd MCU: carousel stepper + remaining I/O)](https://www.berrybase.de/raspberry-pi-pico-rp2040-mikrocontroller-board) | 1 | 4,10 | 4,10 | berrybase.de | verified 10.09.2026; 100+ in stock |
| Controller | [BIGTREETECH TMC2209 V1.3 UART, single (carousel stepper)](https://www.roboter-bausatz.de/p/bigtreetech-tmc2209-v1.3-schrittmotortreiber-uart) | 1 | 5,69 | 5,69 | roboter-bausatz.de | verified 10.09.2026; donor board covers the other 4 axes |
| Power | 24 V power supply | — | — | 0,00 | from donor printer | FROM DONOR - Ender 3 has 24 V / 350 W, saves 18,50 € |
| Power | [Mini step-down module 3 A -> 5 V](https://www.roboter-bausatz.de/p/mini-spannungswandler-step-down-modul-3a) | 1 | 1,29 | 1,29 | roboter-bausatz.de | verified 10.09.2026 |
| Computer | Raspberry Pi 4 Model B rev 1.1, 2 GB RAM (2 on hand; 2nd = cold spare) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - saves 118,50 €. REV 1.1: refuses e-marked USB-C cables, use the official PSU. Verify: cat /proc/cpuinfo -> a03111 |
| Computer | Official Raspberry Pi 15W USB-C PSU (Pi 4 takes 15 W, not 27 W) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED presumed. Do NOT run the Pi off the servo 5 V buck - an MG996R stalls at ~2.5 A |
| Computer | microSD card 32 GB (OS, Klipper, orchestrator, logs only) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - nothing the machine records goes on it |
| Computer | External USB 3.0 SSD for the WAV files, >=500 GB | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED / to hand. ~860 MB per side, ~40 GB per magazine. SSD not HDD - spin-up current and vibration |
| Computer | Self-powered USB 3.0 hub (Scarlett + SSD + webcam + relay card) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - Pi 4 gives only ~1.2 A across all ports. Pin device names with udev rules |
| Cameras | [Raspberry Pi Camera Module 3, 12 MP (deck camera)](https://www.berrybase.de/raspberry-pi-camera-module-3-12mp) | 1 | 28,90 | 28,90 | berrybase.de | verified 10.09.2026; only one needed - the Pi 4B has a single CSI port |
| Cameras | [Raspberry Pi camera cable Standard-Mini, 500 mm (deck camera)](https://www.berrybase.de/raspberry-pi-camera-cable-standard-mini-500mm) | 1 | 3,50 | 3,50 | berrybase.de | verified 10.09.2026; the 200 mm cable in the box may already reach |
| Cameras | Trust HD1080p USB webcam (wrist camera) | — | — | 0,00 | ALREADY OWNED | ALREADY OWNED - one CSI port means the wrist camera goes USB. Lock focus/exposure/gain/WB via v4l2-ctl |
| Vacuum | [Mikro Membran-Vakuumpumpe 12 V (YW11-DC12)](https://www.berrybase.de/mikro-membran-vakuumpumpe-fuer-gas-fluessigkeiten-12v) | 1 | 11,40 | 11,40 | berrybase.de | verified 10.09.2026; out of stock |
| Vacuum | [2/2-way solenoid valve G 1/8 NC, FKM, 12 V, direct acting](https://www.druckluft-fachhandel.de/2-2-wege-magnetventil-g-1-8-stromlos-geschlossen-nc-fkm-12v) | 1 | 42,44 | 42,44 | druckluft-fachhandel.de | verified 10.09.2026 |
| Vacuum | [Adafruit MPRLS pressure sensor breakout 0-25 PSI](https://www.berrybase.de/adafruit-mprls-drucksensor-breakout-mit-anschluss-0-bis-25-psi) | 1 | 30,90 | 30,90 | berrybase.de | verified 10.09.2026; out of stock |
| Vacuum | [Saugeranschlussnippel NW 2.40 mm, G 1/8 AG (TPU cup lip printed)](https://www.druckluft-fachhandel.de/saugeranschlussnippel-nw-2-40-mm-g-1-8-ag-laenge-5-mm-108465) | 1 | 5,00 | 5,00 | druckluft-fachhandel.de | ESTIMATE - not verified |
| Vacuum | [Polyurethane tube 6 x 4 mm, natural, per metre](https://www.druckluft-fachhandel.de/polyurethan-schlauch-6-x-4-mm-natur) | 5 | 1,05 | 5,25 | druckluft-fachhandel.de | verified 10.09.2026 |
| Vacuum | [Straight push-in fitting G 1/8 - 6 mm, IQS](https://www.druckluft-fachhandel.de/gerader-steckanschluss-g-1-8-6mm-iqs-standard) | 8 | 1,38 | 11,04 | druckluft-fachhandel.de | verified 10.09.2026 |
| Sensing | End-stop switches | — | — | 0,00 | from donor printer | FROM DONOR - 3 to 4 mechanical end-stops with cables |
| Sensing | [Hall magnetic sensor module KY-003 (A3144)](https://www.berrybase.de/berrybase-hall-magnetic-sensor-module-ky-003-digitaler-ausgang-hall-effekt-arduino-3.3-5v) | 1 | 0,90 | 0,90 | berrybase.de | verified 10.09.2026 |
| Sensing | [KY-010 photo interrupter / slot optical sensor module](https://www.roboter-bausatz.de/p/ky-010-lichtschranke-modul) | 1 | 1,25 | 1,25 | roboter-bausatz.de | verified 10.09.2026 |
| Deck I/O | [NFKE MG 63 audio cable, 6.3 mm mono jack, 1.8 m](https://www.reichelt.de/de/de/shop/produkt/nf-kabel_6_3_mm_mono_klinkenstecker_gerade_1_8_m_2-pol-109580) | 1 | 1,56 | 1,56 | reichelt.de | verified 10.09.2026 |
| Light | [LED strip warm white, 12 V, 5 m](https://www.reichelt.de/de/de/shop/produkt/led-streifen_warmweiss_5000_mm-235875) | 1 | 5,85 | 5,85 | reichelt.de | verified 10.09.2026 |
| Light | [INFINEON IRLZ44N logic-level MOSFET, TO-220](https://www.reichelt.de/de/de/shop/produkt/mosfet_n-ch_55v_47a_110w_to-220ab-129819) | 2 | 0,67 | 1,34 | reichelt.de | verified 10.09.2026 |
| Carousel | [Miniature ball bearing 608-ZZ 8x22x7 mm](https://www.dold-mechatronik.de/Miniature-ball-bearings-608-ZZ-8x22x7-mm) | 10 | 0,79 | 7,90 | dold-mechatronik.de | verified 10.09.2026 |
| Carousel | [Deep groove ball bearing 6005-2RS 25x47x12 mm](https://www.dold-mechatronik.de/Deep-groove-ball-bearings-6005-2RS-25x47x12-mm) | 1 | 1,79 | 1,79 | dold-mechatronik.de | verified 10.09.2026 |
| Carousel | [Precision shaft 25 mm h6, hardened, cut 100 mm](https://www.dold-mechatronik.de/Precision-shaft-25mm-h6,-ground-and-hardened,-material-CF53-(1.1213),-3.85kg-m,-cut-50-3000mm) | 1 | 3,29 | 3,29 | dold-mechatronik.de | verified 10.09.2026 |
| Cabling | [Energiekette CK10, 20 mm wide, 1000 mm](https://www.dold-mechatronik.de/Energy-chain-CK-10-20mm-wide-1000mm-chain-length-without-connecting-elements) | 3 | 9,57 | 28,71 | dold-mechatronik.de | verified 10.09.2026 |
| Cabling | [Energiekette CK10 connection elements, 1 pair](https://www.dold-mechatronik.de/Energy-chain-CK-10-20mm-wide-connection-elements-1-pair) | 2 | 2,50 | 5,00 | dold-mechatronik.de | verified 10.09.2026 |
| Cabling | [610-piece Dupont crimp connector set in box](https://www.berrybase.de/en/610-piece-dupont-crimp-connector-set-in-plastic-box) | 1 | 9,90 | 9,90 | berrybase.de | verified 10.09.2026 |
| Cabling | [200-piece jumper wire connector kit, JST-SM / Dupont](https://www.berrybase.de/en/berrybase-200-piece-jumper-wire-connector-kit-jst-sm-dupont-2.54mm-2-5-pin-male-female) | 1 | 3,90 | 3,90 | berrybase.de | verified 10.09.2026 |
| Cabling | [Silicone wire 20 AWG, red + black, per metre](https://www.roboter-bausatz.de/search?search=silikonkabel) | 10 | 1,55 | 15,50 | roboter-bausatz.de | verified 10.09.2026 |
| Cabling | [Nylon braided sleeving 15 mm, per metre](https://www.roboter-bausatz.de/search?search=gewebeschlauch) | 5 | 0,32 | 1,60 | roboter-bausatz.de | verified 10.09.2026 |
| Cabling | [Heat shrink assortment Delock 86278, 230 pcs](https://www.reichelt.de/de/de/shop/produkt/schrumpfschlauch_sortiment_-_230-teilig_farbig_box-167391) | 1 | 6,99 | 6,99 | reichelt.de | verified 10.09.2026 |
| Hardware | [Hex socket screw / nut / washer assortment, 520 pcs, M3-M6](https://www.roboter-bausatz.de/p/sortiment-innensechskantschrauben-set-520-teile) | 1 | 18,70 | 18,70 | roboter-bausatz.de | verified 10.09.2026 |
| Hardware | [ruthex M3x5.7 heat-set threaded inserts, 100 pcs](https://www.reichelt.com/de/en/shop/product/3d_printing_threaded_inserts_m3x5_7_pack_of_100-332213) | 1 | 8,99 | 8,99 | reichelt.de | verified 10.09.2026 |

Totals for this route: parts 599,69 €, shipping 42,05 €, delivered **641,74 €**.

### Shipping

| Supplier | Order value € | Shipping € | Rule |
|---|---|---|---|
| eBay Kleinanzeigen / used | 75,00 | 0,00 | Local pickup - a donor printer is not worth shipping |
| dold-mechatronik.de | 176,89 | 12,90 | DPD up to 1.5 m, <=10 kg |
| roboter-bausatz.de | 101,08 | 4,45 | DHL 4,45 €; free from 99 € - NOT reached on this basket |
| berrybase.de | 93,50 | 4,95 | DHL 4,95 € - basket now under the 150 € free threshold since the Pi 5 came out |
| reichelt.de | 24,73 | 5,95 | DHL <=10 kg |
| oyostepper.de | 64,76 | 6,90 | Estimate |
| druckluft-fachhandel.de | 63,73 | 6,90 | Estimate |

### Notes

- Same six shops as sheet 2 plus the donor printer itself. Rows with quantity 0 and supplier 'donor' are the parts the used printer supplies - they carry 0,00 € so the total stays honest.
- What the donor covers: 4-5 NEMA17 steppers, the 24 V power supply, GT2 belt with pulleys and idlers, Delrin V-wheels with eccentrics and carriage plates, mechanical end-stops, the 32-bit board, and a bag of M3/M4 fasteners. Roughly 175 € of parts for a 50-100 € machine.
- Controller: the donor's Creality 4.2.x board runs the four gantry axes under Klipper. A Raspberry Pi Pico (4,10 €) plus one TMC2209 (5,69 €) acts as a second MCU for the carousel stepper and the remaining I/O. That replaces the Octopus and its five drivers - 91,70 € saved for 9,79 €.
- What the donor cannot cover, whatever you buy: the 2x 1.3 m V-slot beams, the 800 mm Z rail and lead screw, the two geared steppers, and everything electronic on the Raspberry Pi side.
- Donor ranking from the BOM: CR-10 / CR-10S (especially the S5) is best - longest extrusions and lead screws. Ender 3 / 3 Pro / V2 is the cheapest and most plentiful but its profiles are short. Ender 5 Plus gives two lead screws and a 350 W supply. Anycubic and Artillery: take for motors and PSU only.
- Buy the donor FIRST. What it turns out to contain decides several lines above, and a worn belt or a seized wheel is worth replacing rather than fitting.
- Check the donor's board revision before counting on it: only 32-bit Creality 4.2.2 / 4.2.7 boards run Klipper. An 8-bit 1.1.4 board does not, and then you are back to the Octopus. The TMC drivers on 4.2.x boards are soldered down, so they cannot be harvested for anything else.
- ALREADY OWNED, shown as 0,00 € rows: 2x Raspberry Pi 4B rev 1.1 / 2 GB (one is the cold spare), their 32 GB cards and 15 W supplies, an external USB 3.0 SSD, a self-powered USB 3.0 hub, and the Trust HD1080p webcam as the wrist camera. Together that removes roughly 185 to 195 € depending on the sheet. Also already on hand and never in these lists: the Omnitronic DD 3120, the Focusrite Scarlett, the Conrad 393905 relay card and the 3D printer.
- Three Pi 4 gotchas worth reading before you wire anything: rev 1.1 boards refuse e-marked USB-C cables (use the official supply); rev 1.1 puts the SD-card voltage regulator on the underside next to the slot where it can be knocked off, so set the card up once and leave it; and the enclosed electronics box needs a heatsink and a fan on a Pi 4 under sustained vision load.
- Put the Scarlett, the SSD, the webcam and the relay card on the powered hub, not on the Pi. The Pi 4 budgets roughly 1.2 A across all four ports and this machine runs unattended for a weekend - a brown-out mid-side is a lost recording. Pin every device with a udev rule so /dev/video* and the ALSA card index do not shuffle across reboots.
