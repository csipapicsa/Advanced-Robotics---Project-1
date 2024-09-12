
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor

wheel_diameter = 40  # in millimeters
axle_track = 145  # distance between the two wheels in millimeters

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

from pybricks.ev3devices import Motor

# VARIABLE INIT
TURN_RATE = 45
DRIVE_SPEED = 100  # The base speed of the robot

TURN_COMMANDS = ["left", "right"]
MOVE_COMMANDS = ["forward", "backward"]

def command(command):
    if command in TURN_COMMANDS:
        turn(command)
    if command in MOVE_COMMANDS:
        move(command)

def move():
    # TODO
    # UNTIL WE ARE SURE WE HAVENT REACHED A NEW SECTION
    pass

def turn(direction):
    # TODO
    # until we turned properly 90 degrees
    if direction == "right":
        robot.drive(DRIVE_SPEED, TURN_RATE)  # Turn right
    elif direction == "left":
        robot.drive(DRIVE_SPEED, -TURN_RATE)  # Turn left


def direction_to_command(direction_command):
    if direction_command.contains("-"):
        commands = direction_command.split("-")
        for c in commands:
            command(c)
    else:
        command(direction_command)

