#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import LightSensor

# from PID_control import PIDController
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# pid = PIDController(kp=0.4, ki=0.1, kd=0.01, setpoint=100)
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
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S2)
#port S3 is not working
middle_sensor = LightSensor(Port.S4)

# Define thresholds for detecting the black line
RIGHT_THRESHOLD = 20
LEFT_THRESHOLD = 20
RIGTH_BLACK = 4
LEFT_BLACK = 4
INTERSECTION_THRESHOLD = 5 # on the line
MIDDLE_BLACK = 18 #we are on the line if it is 3 or under

# Speed and steering parameters
DRIVE_SPEED = 50  # The base speed of the robot
TURN_RATE = 90   # How sharply the robot turns when correcting

LEFT = -105
RIGHT = 105
STRAIGHT = 0

# INSTRUCTIONS = [LEFT, RIGHT, RIGHT, LEFT, STRAIGHT] # LEFT, RIGHT, RIGHT, LEFT

ev3.speaker.beep()

# Main loop to follow the black line and print reflection values
while True:
    # Get the reflected light intensity from both sensors
    left_reflection = left_sensor.reflection()
    right_reflection = right_sensor.reflection()
    middle_reflection = middle_sensor.reflection() # checking if we are on the line
    # print the battery voltage
    ev3.screen.draw_text(0, 0, "Battery Voltage: {}".format(ev3.battery.voltage()))

    # Print the reflection values to the EV3 Brick's screen
    ev3.screen.clear()  # Clear the screen to avoid overlapping text
    ev3.screen.draw_text(0, 0, "Left: {}".format(left_reflection))
    ev3.screen.draw_text(0, 20, "Right: {}".format(right_reflection))
    # We found an intersection
    if left_reflection <= INTERSECTION_THRESHOLD and right_reflection <= INTERSECTION_THRESHOLD and middle_reflection <= MIDDLE_BLACK:
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "Intersection")
        # robot.straight(90) # Drive a bit
        # instruction = INSTRUCTIONS.pop(0)
        # ev3.screen.draw_text(0, 0, "{}".format(instruction))
        # robot.turn(instruction) # Turn
        robot.drive(DRIVE_SPEED, -TURN_RATE)  # Turn left
        wait(200)
        robot.drive(DRIVE_SPEED, 0) # Continue driving
    # If both sensors detect black, move straight
    elif left_reflection <= LEFT_THRESHOLD and right_reflection <= RIGHT_THRESHOLD and left_reflection >= LEFT_BLACK and right_reflection >= RIGTH_BLACK and middle_reflection <= MIDDLE_BLACK:
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "Straight")
        robot.drive(DRIVE_SPEED, 0)  # Move straight
    # If only the left sensor detects black, turn right
    elif left_reflection <= LEFT_BLACK and middle_reflection <= MIDDLE_BLACK:
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "Left")
        robot.drive(DRIVE_SPEED, -TURN_RATE)  # Turn left
    # If only the right sensor detects black, turn left
    elif right_reflection <= RIGTH_BLACK and middle_reflection <= MIDDLE_BLACK:
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "Right")
        robot.drive(DRIVE_SPEED, TURN_RATE)  # Turn right
        # wait(1000) if this is implemented are we are correcting it will Correct as it was a right turn and not only a small correction to the right
    else:
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "None of above")
        robot.drive(DRIVE_SPEED, 0)
    # Short wait to avoid busy-waiting
    wait(100)