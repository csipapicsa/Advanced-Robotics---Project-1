#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

# Initialize motors connected to Ports A and D
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Create a DriveBase object
wheel_diameter = 40  # in millimeters
axle_track = 145  # distance between the two wheels in millimeters
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Initialize the color sensors connected to Ports S1 and S2
right_sensor = ColorSensor(Port.S1)
left_sensor = ColorSensor(Port.S2)

# Define thresholds for detecting the black line
RIGHT_THRESHOLD = 20
LEFT_THRESHOLD = 20
INTERSECTION_THRESHOLD = 3 # on the line

# Speed and steering parameters
DRIVE_SPEED = -100  # The base speed of the robot
TURN_RATE = 50   # How sharply the robot turns when correcting

LEFT = -105
RIGHT = 105
STRAIGHT = 0

INSTRUCTIONS = [LEFT, RIGHT, RIGHT, LEFT, STRAIGHT] # LEFT, RIGHT, RIGHT, LEFT

ev3.speaker.beep()

# Main loop to follow the black line and print reflection values
while True:
    # Get the reflected light intensity from both sensors
    left_reflection = left_sensor.reflection()
    right_reflection = right_sensor.reflection()

    # Print the reflection values to the EV3 Brick's screen
    ev3.screen.clear()  # Clear the screen to avoid overlapping text
    ev3.screen.draw_text(0, 0, "Left: {}".format(left_reflection))
    ev3.screen.draw_text(0, 20, "Right: {}".format(right_reflection))
    # If neither sensor detects black, stop the robot
    if left_reflection >= LEFT_THRESHOLD and right_reflection >= RIGHT_THRESHOLD:
        None
        #robot.stop()
    # We found an intersection
    elif left_reflection < INTERSECTION_THRESHOLD and right_reflection < INTERSECTION_THRESHOLD:
        robot.straight(90) # Drive a bit
        instruction = INSTRUCTIONS.pop(0)
        ev3.screen.draw_text(0, 0, "{}".format(instruction))
        robot.turn(instruction) # Turn
        wait(200)
        robot.drive(DRIVE_SPEED, 0) # Continue driving
    # If both sensors detect black, move straight
    elif left_reflection < LEFT_THRESHOLD and right_reflection < RIGHT_THRESHOLD:
        robot.drive(DRIVE_SPEED, 0)  # Move straight
    # If only the left sensor detects black, turn right
    elif left_reflection < LEFT_THRESHOLD:
        robot.drive(DRIVE_SPEED, -TURN_RATE)  # Turn left
    # If only the right sensor detects black, turn left
    elif right_reflection < RIGHT_THRESHOLD:
        robot.drive(DRIVE_SPEED, TURN_RATE)  # Turn right

    # Short wait to avoid busy-waiting
    wait(100)