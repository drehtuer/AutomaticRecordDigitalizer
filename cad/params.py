"""All dimensions of the AutomaticRecordDigitalizer in millimetres.

Machine coordinate system: X along the bench from the carousel towards the deck,
Y across the bench (positive towards the front), Z up. Origin: bench top,
20 cm left of the flip station post (the same origin the concept model uses).

Values marked MEASURE were taken from a photo of the deck and must be confirmed
with a ruler; everything else comes from the concept design.
"""
from math import radians

# ---------------------------------------------------------------- records
RECORD_12_R = 150.0
RECORD_10_R = 125.0
RECORD_7_R = 88.0
RECORD_T = 3.0            # nominal thickness used for clearances
LABEL_R = 50.0
HOLE_R = 3.62             # 7.24 mm hole

# ---------------------------------------------------------------- bench
BENCH_L, BENCH_W, BENCH_T = 1900.0, 1000.0, 18.0
BENCH_CX = 60.0           # bench centre X

# ---------------------------------------------------------------- carousel
CAR_CX, CAR_CY = -400.0, 0.0
CAR_SLOTS = 24
CAR_PITCH = radians(360.0 / CAR_SLOTS)
CAR_BASE_R, CAR_BASE_T = 440.0, 15.0        # fixed plywood base plate
CAR_DISC_R, CAR_DISC_T = 430.0, 18.0        # rotating plywood floor
CAR_DISC_Z = 60.0                           # underside of the disc
CAR_HUB_R, CAR_HUB_H = 90.0, 220.0          # printed centre hub, from disc top
CAR_RIM_R, CAR_RIM_TUBE = 420.0, 9.0        # printed rim ring (records rest against it)
CAR_RIM_Z = 130.0
CAR_REC_R = 260.0                           # radius of a 12" record's centre
CAR_REC_Z = CAR_DISC_Z + CAR_DISC_T + RECORD_12_R   # record centre height, standing on the disc
CAR_COMB_L, CAR_COMB_H, CAR_COMB_T = 300.0, 30.0, 12.0
CAR_COMB_R = 240.0                          # comb centre radius
CAR_ROLLER_N, CAR_ROLLER_R = 10, 360.0      # 608 bearings on a ring
CAR_TOOTH_R, CAR_TOOTH_T = 215.0, 10.0      # GT2 ring under the disc
CAR_SHAFT_R = 12.5                          # 25 mm stub shaft, 6005 bearing
CAR_PICK_ANGLE = 0.0                        # slot 0 points along +X towards the deck

# ---------------------------------------------------------------- frame (birch ply box)
PLY = 18.0
FRAME_Y = 430.0                             # side panel centre planes at ±FRAME_Y (86 cm wide: the fork must clear the rear panel at the re-grip pose)
FRAME_X0, FRAME_X1 = -220.0, 990.0          # side panel extent
FRAME_H = 830.0
PANEL_BOTTOM_STRIP, PANEL_TOP_STRIP, PANEL_POST_W = 120.0, 140.0, 120.0
PANEL_MID_POST_X = 380.0
BEAM_X0, BEAM_X1 = -300.0, 990.0            # 2040 V-slot X beams, overhanging the open end
BEAM_Z = 850.0                              # beam centre height (2040: 40 tall, 20 wide)
TIE_X = BEAM_X0 + 15.0                      # 2020 tie across the open end

# ---------------------------------------------------------------- gantry
XCAR_PLATE = (80.0, 80.0, 30.0)             # V-wheel plate on each beam (X, Y, Z)
CROSS_BEAM_L = 940.0                        # 2040 V-slot along Y
CROSS_BEAM_Z = BEAM_Z + 40.0                # centre height
GUIDE_BLOCK = (80.0, 80.0, 120.0)           # Z guide on the Y carriage
ZCAR_BLOCK = (70.0, 70.0, 80.0)
COLUMN_L = 760.0                            # moving Z column (MGN12 rail on it)
COLUMN_W = 40.0
WRIST_X = 90.0                              # pivot offset from the column, along +X
ARM_L = 220.0                               # pivot to cup centre line
ARM_W = 24.0
CUP_R, CUP_H = 28.0, 16.0                   # 40 mm bellows cup envelope
CUP_OFF = 28.0                              # cup centre from the arm axis (towards -Y at wrist 0°)
HELD_OFF = CUP_OFF + CUP_H / 2 + RECORD_T / 2   # held record centre from the arm axis
FORK_L = 55.0                               # hub to U crossbar, opposite the arm (short, so it stays inside the frame at the re-grip pose)
FORK_PRONG_GAP = 28.0
CAM_OFF = (50.0, 0.0, 110.0)                # wrist camera centre relative to the arm end (X, Y, Z-up along the arm); +X side, 110 mm up the arm so it clears the ring rest
TRAVEL_Z = 540.0                            # pivot height for travelling
TRAVEL_Z_STATION = 580.0                    # pivot height while crossing the station

# ---------------------------------------------------------------- flip station
ST_X, ST_Y, ST_Z = 200.0, -120.0, 300.0     # ring rest centre
ST_RING_R, ST_RING_TUBE = 78.0, 8.0
ST_GAP = radians(60.0)                      # opening towards +Y
ST_POST_Y = ST_Y - 140.0
ST_ARM_Z = ST_Z - 19.0                      # the post's horizontal arm sits under the ring so a record on the ring never touches it
ST_BOX = (260.0, 180.0, 90.0)               # electronics box under the station
ST_BOX_Y = ST_Y - 80.0

# ---------------------------------------------------------------- deck (Omnitronic DD 3120)
DECK_SPINDLE_X, DECK_SPINDLE_Y = 550.0, 0.0
DECK_W, DECK_D, DECK_H = 450.0, 360.0, 90.0
DECK_SPINDLE_FROM_LEFT = 184.0              # MEASURE
DECK_SPINDLE_FROM_REAR = 186.0              # MEASURE
DECK_CX = DECK_SPINDLE_X - DECK_SPINDLE_FROM_LEFT + DECK_W / 2
DECK_CY = DECK_SPINDLE_Y + DECK_SPINDLE_FROM_REAR - DECK_D / 2   # rear edge is -Y
PLATTER_R, PLATTER_T = 165.0, 15.0
MAT_T = 3.0
SPINDLE_R, SPINDLE_H = 3.6, 22.0
ARM_PIVOT = (DECK_SPINDLE_X + 194.0, DECK_SPINDLE_Y - 84.0, 130.0)   # MEASURE
ARM_EFF_L = 230.0                           # pivot to stylus
ARM_REST_XY = (DECK_SPINDLE_X + 189.0, DECK_SPINDLE_Y + 125.0)       # MEASURE
ARM_ANGLE = {                               # stylus azimuth from the pivot, degrees, recomputed for the measured pivot
    "rest": 91.3, "leadin": 118.0, "runout": 140.0, "mid": 129.0,
}
ARM_LIFT = 10.0                             # cue lift height
FINGER_LIFT_LOCAL = (ARM_EFF_L - 6.0, 22.0, -4.0)   # relative to the pivot, arm along +X (X, Y outward, Z)
CUE_LEVER = (DECK_SPINDLE_X + 235.0, DECK_SPINDLE_Y - 46.0, 102.0)   # MEASURE
END_STOP_ANGLE, END_STOP_R = 143.8, 45.0   # arm-tube azimuth and radius from the pivot at which the stop stands (45 mm keeps the pin outside a 12" record's outline)
DECK_CAM = (FRAME_X1 - 30.0, 20.0, 155.0)

# ---------------------------------------------------------------- deck interface hardware
CUE_SERVO_Y = CUE_LEVER[1]
CUE_SERVO_Z = CUE_LEVER[2]
