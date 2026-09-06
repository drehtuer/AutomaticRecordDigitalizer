# Design specification

This document describes the machine as it stands after the concept review. Dimensions are the ones used in the concept model and are good to a centimetre; the CAD phase fixes them to the millimetre. The coordinate system is the machine's: X runs along the bench from the carousel towards the deck, Y runs across the bench (positive towards the front), Z is up. The origin is at the bench top under the flip station.

## Overview and footprint

The bench is about 190 × 100 cm. From left to right it carries the carousel magazine (Ø 86 cm, standing free on the bench), then the frame (125 × 80 × 90 cm) that spans the flip station and the turntable. The gantry rides on top of the frame; its Z column rises to about 135 cm when fully raised, so the machine wants a metre and a half of headroom.

The frame's left end is open and its rails overhang it by 8 cm so that the gantry can reach the carousel's pick slot, which is the only point where the two halves of the machine meet. The carousel can be lifted off the bench for loading without touching the frame.

## Frame

The frame is a glued box of 18 mm birch plywood: two side panels at Y = ±40 cm and one end panel at the deck end, each cut as a frame around a large window so the interior stays open and reachable. The panels give the racking stiffness; there are no diagonals and no corner posts. A 2040 aluminium extrusion is bolted along the top edge of each side panel and carries an MGN12 linear rail, the X axis. One 2020 tie across the open end keeps the two beams parallel. Brackets for the brush module, the cue-lever servo, the deck camera and the LED bar screw directly to the panels' inner faces.

The Pi, the controller board and the vacuum pump live in a box under the flip station, whose post stands on that box.

## Gantry

The gantry is a Cartesian XYZ with one rotary axis:

| Axis | Mechanism | Travel | Notes |
|---|---|---|---|
| X | GT2 belt, NEMA17, MGN12 rails on both beams | ≈ 80 cm | From the carousel pick slot to the tonearm rest |
| Y | GT2 belt, NEMA17, MGN12 rail on the cross beam | ≈ 45 cm | Set by the two station poses, 22 cm either side of the ring |
| Z | T8 lead screw, NEMA17, moving column | ≈ 60 cm | Column slides through a guide on the cross beam; self-locking |
| Wrist | NEMA17 with ≈ 5:1 planetary gearbox, Hall home sensor | −90° … 180° | Axis parallel to X |

The Z axis is a moving column rather than a fixed tower: the 76 cm rail is part of the carriage and slides up through a guide block on the cross beam, so when the carriage is raised nothing hangs below it. Every X move happens at travel height and clears the deck, the station and the brush by construction. The lead screw is self-locking, so a power loss leaves the record where it is.

The wrist sits on a 9 cm outrigger beside the column so the arm can swing without meeting it. It carries three things: the vacuum arm (22 cm, with the cup on its end pointing perpendicular to the arm), the wrist camera looking along the cup's axis, and the finger-lift fork on the opposite side of the hub, 10 cm long, which points down when the arm points up.

## Gripper

The gripper is a single 40 mm bellows vacuum cup on the label area, fed by a 12 V diaphragm pump through a solenoid release valve, with a vacuum switch that confirms a seal before any move and aborts a move if the seal is lost. The label area is the one thing every record has in common, so the cup handles 12", 10" and 7" records and shaped discs alike; 7" singles with the large jukebox hole are out of scope.

The cup's bellows give about 5 mm of compliance, which is what lets the cup land on a spoke standing slightly off its nominal position.

## Carousel magazine

The magazine is a horizontal disc with 24 radial slots at 15° pitch. Records stand vertically in the slots like spokes, resting against an outer rim ring at a radius of 41 cm, so that every size sits at the same outer radius and the gap between neighbours at the label radius is about 6.5 cm, enough for the 5 cm gripper assembly to descend beside a record.

The disc is 8 mm plywood cut roughly round and is nothing but a floor. It rolls on ten identical printed brackets, each holding a 608 bearing, arranged on a 72 cm circle, and is located by a 6005 bearing on a stub shaft at the centre. A printed GT2 tooth ring in eight dovetailed segments on the disc's underside is driven by a NEMA17 with a small pulley, about 40:1, and an optical sensor reads a home mark; one slot index is therefore repeatable to a fraction of a millimetre at the rim. The 24 slot combs plug into a printed centre hub and printed rim segments, which carry the angular positions, so the wood never has to be cut precisely.

Each record returns to the slot it came from, so the magazine is both infeed and outfeed, records never touch each other, and pick and return happen at one fixed position: the slot that points along X towards the deck.

## Flip and photo station

A ring rest on a post 12 cm behind the machine's centreline, at X = 20 cm, Z = 30 cm: an annulus of 70 mm inner and 86 mm outer diameter, TPU-padded, so it touches only the label of any record size, with a 60° opening towards the front through which the vacuum arm enters. The station is deliberately off the centreline so that a vertical record travelling along X at travel height passes beside it.

## Turntable interface

The deck is an Omnitronic DD 3120: a Technics-type direct drive, 45 × 35 × 9 cm, with a manual cue lever, a remote start/stop connector, a pitch output and no auto-return. (A Stanton T.92 USB is also available but has no cue lever, which would bring back a separate arm-lift mechanism; it stays the spare.) The cartridge is an Ortofon DJ S, a spherical DJ stylus tracking at about 3 g, robust against the kind of handling this machine does; an elliptical stylus can be swapped in for a final archive pass once the machine is trusted. The machine touches the deck in four places, none of them modifications:

Start and stop go through the deck's own remote start/stop connector, the fader-start input meant for DJ mixers, which expects a contact closure: a relay or optocoupler on a 3.5 mm plug, with no wire soldered inside the deck. The 33 and 45 buttons are momentary switches and are tapped through two optocouplers wired in parallel with them.

The cue lever is worked by a small linear-push servo mounted on the rear panel, whose rod comes in along Y at lever height, below the arm's swing. The same bracket carries a soft-sleeved end-stop pin that stands in the arm tube's path at about 6 cm from the arm pivot, so the arm cannot swing past a stylus radius of roughly 53 mm: the stylus physically cannot reach the label.

The tonearm is moved only while the cue lever holds it up, by the fork straddling the headshell's finger lift with prongs fore and aft of it. The fork never carries the arm's weight.

The arm rest clip stays open.

## Brush module

A carbon-fibre record brush on a servo arm, mounted on a bracket on the rear panel with an outrigger reaching behind the deck. It swings over the spinning record, is lowered for a few revolutions, swept outward to carry dust to the edge, and on its way back to park drags its bristles across a dust edge: a thin aluminium comb running radially, as long as the brush, perpendicular to the sweep, with a slide-out tray under it that pulls out towards the back of the frame for emptying.

## Cameras and light

The wrist camera (Pi Camera Module 3 or a small USB module) sits on the wrist arm looking along the cup axis, 6 cm from the cup. Before every grip it sees the face it is about to grip: at the carousel it reads the centre hole position, the label, and the lead-in and run-out radii of side A; at the station it does the same for side B. Both label photographs come from it.

The deck camera (Pi Camera Module 3) is mounted low on the deck-end panel at platter height, facing the headshell across the platter from 20 to 40 cm. It sees the stylus in profile, the groove bands edge-on and the strobe dots on the platter rim. It tracks the headshell to locate the arm wherever a side ended, confirms the stylus landed on the lead-in, watches for the run-out and for skips, and reads the platter speed.

An LED bar beside the deck camera has two modes: pulsed at 50.000 Hz from the controller's crystal it is a strobe that makes the rim dots (or a printed strobe ring on a deck without dots) show the speed error as a drift; run continuously it is a low-angle raking light that makes the grooves and the stylus contact visible.

## Materials and printing

Printed parts are PETG for structure and TPU wherever a record is touched: the cup lip if not bought, the fork lining, the ring rest pads, the end-stop sleeve. Bought parts are everything long, stiff or precise: extrusion, rails, screws, bearings, motors, electronics. Plywood is used for the frame panels, the bench top, the carousel disc and its base plate, and never for anything whose position matters.
