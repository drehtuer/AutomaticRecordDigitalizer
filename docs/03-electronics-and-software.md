# Electronics and software

The guiding idea is that the machine is a strangely shaped 3D printer. Motion runs on a printer mainboard under Klipper, which already solves homing, stepper drivers, end-stops, servos, PWM outputs and G-code macros; everything the printer world does not have (cameras, orchestration, recording, the web interface) runs in Python on a Raspberry Pi that is also Klipper's host.

## Hardware

**Controller.** BIGTREETECH Octopus V1.1 with five TMC2209 drivers: X, Y, Z, wrist, carousel index. The board's remaining driver slots stay free. Its servo header drives the brush servo and the cue-lever servo; its fan/heater MOSFET outputs drive the vacuum pump, the release valve and the LED bar (the LED output must be a proper PWM pin so the strobe can run at 50.000 Hz); its end-stop inputs take the axis end-stops, the wrist Hall sensor, the carousel home sensor and the vacuum switch. A 24 V 150 W supply feeds the board, and the board's 5 V rail or a separate buck converter feeds the servos.

**Computer.** Raspberry Pi 5 (4 GB). It runs Klipper's host process, Moonraker, the orchestrator, the vision code, the web interface and the audio capture. The Scarlett connects over USB; second-generation and later Scarletts are USB class compliant and need no driver on Linux.

**Cameras.** Two Pi Camera Module 3 units. The deck camera connects directly to the Pi by ribbon cable. The wrist camera rides on the gantry, so its cable runs through 1.5 m of cable chain; either a CSI-to-HDMI extender pair carries the ribbon signal that far, or the wrist camera is a small USB module, which is simpler and adequate for its job.

**Deck interface.** Start/stop uses the DD 3120's remote start/stop jack (6.3 mm), a contact-closure input for the fader-start feature of older mixers: one optocoupler or small relay on a 6.3 mm plug, driven from Octopus GPIO, no soldering in the deck. Fader start normally means the platter runs while the contact is closed and stops when it opens, so `DECK_START` closes the contact and holds it, `DECK_STOP` opens it; confirm on the deck that it is level-driven rather than a toggle, and note that the jack has no effect on speed. The 33 and 45 buttons (there is a 78 too, unused) are momentary switches and get one optocoupler each wired in parallel with the switch. The quartz-lock button should be left engaged; the deck camera can confirm its LED. The deck's pitch output, if it carries a speed or tacho signal, can feed a counter input on the Octopus as a second speed reference beside the strobe; what it actually outputs is an open question.

**Sensors.** Mechanical or optical end-stops on X, Y and Z at the home ends; a Hall sensor for the wrist's home position; a slot-type optical sensor reading a home mark on the carousel's tooth ring; a vacuum switch in the cup line; optionally a record-present reflective sensor at the pick position, though the wrist camera makes it redundant.

**Cabling.** Two cable chains: one along the X beam carrying the Y and Z motors, the wrist motor, the wrist camera, the pump line and the end-stops; one along the Z column to the wrist. The vacuum hose runs the same way.

## Klipper configuration

The `printer.cfg` declares the four motion axes as a Cartesian kinematics with X, Y, Z, and the wrist as an additional manual stepper, the carousel as a second manual stepper, both servos as `servo` sections, the pump, valve and LED as `output_pin` sections (the LED with `pwm: True` and a 20 ms cycle time for the strobe), and the three optocouplers (remote start/stop, 33, 45) as `output_pin` outputs with a macro that pulses each for 150 ms.

G-code macros implement the primitives the orchestrator composes: `HOME_ALL`, `GRIP` (pump on, wait for the vacuum switch, else error), `RELEASE`, `CUE_UP`, `CUE_DOWN`, `DECK_START`, `DECK_STOP`, `DECK_33`, `DECK_45`, `BRUSH_DEPLOY`, `BRUSH_PARK`, `CAROUSEL_INDEX`, `STROBE_ON`, `LIGHT_ON`, `LIGHT_OFF`, and `EMERGENCY_LIFT`, which is `CUE_UP` followed by `DECK_STOP` and a motion halt, bound so it can be fired without waiting for the queue.

Klipper's own safety features do the low-level work: TMC stall detection on every axis, soft limits, and a hard limit on Z so the carriage cannot be driven below its lowest working height.

## Orchestrator

A Python service on the Pi that talks to Klipper through Moonraker's API and owns the state machine of the cycle. Each step of the cycle in `02-operating-cycle.md` is one state; each state issues a planned list of waypoints as G-code, waits for completion, checks its post-condition (vacuum seal, camera confirmation, sensor state), and either advances or raises a fault.

The motion planner is the same one the concept model uses: retreat, raise, ordered horizontal moves, lower, approach, with per-pose exceptions for the station. Poses are computed from a small set of calibrated datums: the pick slot's centre, the spindle, the ring rest, the arm pivot and the arm's rest, lead-in and run-out angles for the deck in use. Calibration is a guided procedure in the web interface that jogs the axes to each datum with the camera live.

Faults never attempt recovery. The orchestrator fires `EMERGENCY_LIFT` when a side is playing, stops everything else in place, records the state, and notifies the user.

## Vision

OpenCV in Python on the Pi, with picamera2 for the Pi cameras.

The wrist camera does four things on each face it sees: finds the centre hole (a dark circle of known size; its offset from the camera axis gives the cup-to-hole offset used when placing on the spindle), finds the label edge, finds the transition from label to lead-out band and from lead-in band to the outer edge (the groove bands differ from the smooth bands in reflectance), and saves a face-on label photograph named by slot and side.

The deck camera tracks the headshell as a dark rectangle in a known region, converts its image position to an arm angle through a calibration, and from the angle derives the stylus radius. It detects the run-out as the radius reaching the value measured on the face-on photo, and a skip as a radius jump larger than the groove pitch between frames. For speed, it tracks either the strobe-lit dots' drift or a single marker on the rim between timestamped frames and reports mean rotation rate and wow; both values go into the recording's sidecar file.

## Recording

`arecord` or a small sounddevice loop captures from the Scarlett at 96 kHz / 24 bit into one WAV file per side, started before the stylus is lowered and stopped after the arm is parked. The phono signal passes through the deck's own phono stage (line output) or an external phono preamp before the Scarlett; the Scarlett has no phono input. A silence detector on the live stream provides the run-out confirmation and the skip detector's audio half.

Each side produces a WAV, both label photos (side A's from the pick, side B's from the re-grip), and a JSON sidecar with slot, manifest line, measured speed and wow, cue and run-out radii, and timestamps. Track cutting, mastering and tagging operate on these later and are out of scope here.

## Web interface

A FastAPI service with a small single-page front end, served from the Pi on the local network. It provides the batch manifest editor (slot, size, speed, flags), the live views of both cameras, a jog panel and the calibration procedure, a step-through mode that runs the cycle one state at a time for commissioning, the batch status with the current step and the queue, a pause and a resume, and the fault screen with the manual "retry from here". Later the same interface hosts the Discogs lookup and tag review of the follow-up project.
