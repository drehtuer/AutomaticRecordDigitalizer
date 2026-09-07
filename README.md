# AutomaticRecordDigitalizer

[![CI](https://github.com/drehtuer/AutomaticRecordDigitalizer/actions/workflows/ci.yml/badge.svg)](https://github.com/drehtuer/AutomaticRecordDigitalizer/actions/workflows/ci.yml)
[![Documentation](https://github.com/drehtuer/AutomaticRecordDigitalizer/actions/workflows/documentation.yml/badge.svg)](https://github.com/drehtuer/AutomaticRecordDigitalizer/actions/workflows/documentation.yml)
[![Dependabot Updates](https://github.com/drehtuer/AutomaticRecordDigitalizer/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/drehtuer/AutomaticRecordDigitalizer/actions/workflows/dependabot/dependabot-updates)
[![License: GPL-2.0](https://img.shields.io/github/license/drehtuer/AutomaticRecordDigitalizer)](https://github.com/drehtuer/AutomaticRecordDigitalizer/blob/main/LICENSE)

A DIY machine that digitises a vinyl record collection unattended: it takes a record from a magazine, puts it on a Technics-style turntable (an Omnitronic DD 3120), cues the stylus, records the side, flips the record, records the other side, and puts it back — 10 to 20 records per eight-hour run, a full 24-slot magazine over a weekend, with a photo of both labels for the tags. Records are brushed by hand before they go into the magazine.

The project exists because the cheap way of doing this, a second-hand stacking record changer, drops records onto each other and the recordings show it. Here nothing ever touches a record except a vacuum cup on the label, a felt-lined slot, and the turntable mat.

## Status

Concept design finished and reviewed in September 2026; first parametric CAD in place, with the whole cycle passing a scripted collision check. Nothing has been bought or printed yet. [docs/07-status-and-next-steps.md](docs/07-status-and-next-steps.md) records exactly where the project stands, what is already on hand, and what to do first.

## What is in this repository

[cad-model.html](cad-model.html) is the machine in the browser: orbit and zoom it, play the cycle, or jump to any of the fourteen steps. Both halves come from the parametric model — the geometry from `python -m cad.export_web`, the motion from the planner's own keyframes in `cad/cycle.json` — so it shows the machine the collision checker sweeps, moving the way it sweeps it.

[concept-model.html](concept-model.html) is an interactive 3D model that steps through the complete operating cycle, including the B-side flip and the fault case, with every step's motion planned as real waypoints in the order the controller will use. Its geometry is its own, written during the concept phase, and predates the five corrections the CAD found: read it for the sequence, not for dimensions.

`cad/` is the parametric CadQuery model with the motion planner and the collision checker; `cad/README.md` explains how to run it, and `cad/export/` holds STEP files that open in FreeCAD, STL files of the first printed parts, and `web/` holds the glTF and the scene description the viewer loads.

`docs/` holds the design in detail:

| Document | Contents |
|---|---|
| [01-design-specification.md](docs/01-design-specification.md) | Mechanical layout, every subsystem, dimensions, materials |
| [02-operating-cycle.md](docs/02-operating-cycle.md) | The cycle step by step, motion-planning rules, fault handling |
| [03-electronics-and-software.md](docs/03-electronics-and-software.md) | Controller, wiring, Klipper, orchestrator, vision, web UI, recording |
| [04-bill-of-materials.md](docs/04-bill-of-materials.md) | Parts with German sources, printed-part list, cost |
| [05-design-decisions.md](docs/05-design-decisions.md) | Why the machine is the way it is, including rejected alternatives |
| [06-open-questions.md](docs/06-open-questions.md) | What has to be verified on real hardware |
| [07-status-and-next-steps.md](docs/07-status-and-next-steps.md) | Current state, parts on hand, build order |

## The machine in one paragraph

Records stand like spokes in a 24-slot carousel. A small XYZ gantry with a rotary wrist carries a vacuum cup that takes each record by its label, lifts it out of its slot, turns it flat over the deck and sets it on the spindle. The deck's own cue lever, worked by a servo, lifts the tonearm while a fork on the wrist walks it to the lead-in groove found by a camera; the platter is stopped before every needle placement and removal. After the run-out, the record goes to a ring rest where the cup lets go and re-grips the other face, both labels get photographed, and side B is recorded the same way. The record returns to its own slot and the carousel indexes to the next one. The deck's remote start/stop connector starts and stops the platter. Recording runs through a Focusrite Scarlett into a Raspberry Pi, which also runs the cameras, the web interface for the batch list, and the orchestration on top of Klipper running on a printer mainboard, with a USB relay card working the deck's remote start/stop jack and speed buttons.

## Follow-up project

Cutting the recordings into tracks, mastering, and tagging (using the label photos and the batch manifest) is deliberately out of scope until the changer has proven itself on real records.

## License

Copyright (C) 2026 drehtuer

This project is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. The text of version 2 is in [LICENSE](LICENSE); the SPDX identifier is `GPL-2.0-or-later`.

It is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

The licence covers everything here: the CadQuery model and the planner as source code, and the design documents and the concept model as the machine's design.
