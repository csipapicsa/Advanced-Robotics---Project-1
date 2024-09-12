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
axle_track = 190 #145 # distance between the two wheels in millimeters
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Initialize the color sensors connected to Ports S1 and S2
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S2)
#port S3 is not working
middle_sensor = LightSensor(Port.S4)

# Define thresholds for detecting the black line
RIGHT_THRESHOLD = 20
LEFT_THRESHOLD = 20
RIGTH_BLACK = 7
LEFT_BLACK = 9
MIDDLE_BLACK = 28 #we are on the line if it is 34 or under
MIDDLE_THRESHOLD = 47

# Speed and steering parameters
DRIVE_SPEED = 70 #50  # The base speed of the robot
TURN_RATE = 90 # How sharply the robot turns when correcting

LEFT = -105
RIGHT = 105
STRAIGHT = 0

# INSTRUCTIONS = [LEFT, RIGHT, RIGHT, LEFT, STRAIGHT] # LEFT, RIGHT, RIGHT, LEFT

ev3.speaker.beep()

maze = [[1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 1, 0, 1, 0, 1], 
        [1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 1, 0, 1, 0, 1], 
        [1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 1, 0, 1, 0, 1], 
        [1, 1, 1, 1, 1, 1, 1]]


# commands = ["forward", "right", "backwards"]
commands = ["forward", "backwards", "left", "backwards", "right", "backwards"]


# Main loop to follow the black line and print reflection values
while True:
    # Get the reflected light intensity from both sensors
    left_reflection = left_sensor.reflection()
    right_reflection = right_sensor.reflection()
    middle_reflection = middle_sensor.reflection() # checking if we are on the line
    
    # Print the reflection values to the EV3 Brick's screen
    ev3.screen.clear()  # Clear the screen to avoid overlapping text
    

    #If corner of any kind (thereby also intersection)
    if ((left_reflection <= LEFT_BLACK and middle_reflection <= MIDDLE_BLACK) or (left_reflection <= LEFT_BLACK and middle_reflection > MIDDLE_BLACK and right_reflection > RIGTH_BLACK)) or ((right_reflection <= RIGTH_BLACK and middle_reflection <= MIDDLE_BLACK) or (right_reflection <= RIGTH_BLACK and middle_reflection > MIDDLE_BLACK and left_reflection > LEFT_BLACK)):
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "INTERSECTION")
        if len(commands) == 0:
            robot.stop()
            break
        currentCommand = commands.pop(0)

        if currentCommand == "right":
            ev3.screen.clear()
            ev3.screen.draw_text(0, 0, "Right")
            robot.straight(35)
            robot.turn(TURN_RATE-10)  # Turn right
            robot.straight(25)
        elif currentCommand == "left":
            ev3.screen.clear()
            ev3.screen.draw_text(0, 0, "Left")
            robot.straight(65)
            robot.turn(-TURN_RATE)  # Turn left
            robot.straight(25)
        elif currentCommand == "forward":
            ev3.screen.clear()
            ev3.screen.draw_text(0, 0, "Forward")
            robot.straight(75)
        elif currentCommand == "backwards":
            ev3.screen.clear()
            ev3.screen.draw_text(0, 0, "Backwards")
            robot.straight(-100)
            robot.turn(-180) #turn left all the around
            robot.straight(-50)
            ev3.speaker.beep()
        else: 
            ev3.screen.clear()
            ev3.screen.draw_text(0, 0, "WHAT TO DO???")
            robot.stop()
            ev3.speaker.beep()
            ev3.speaker.beep()
    

    #BOTH left and right --> all sensors 
    # if ((left_reflection <= LEFT_BLACK and middle_reflection <= MIDDLE_BLACK) or (left_reflection <= LEFT_BLACK and middle_reflection > MIDDLE_BLACK and right_reflection > RIGTH_BLACK)) and ((right_reflection <= RIGTH_BLACK and middle_reflection <= MIDDLE_BLACK) or (right_reflection <= RIGTH_BLACK and middle_reflection > MIDDLE_BLACK and left_reflection > LEFT_BLACK)):
    #     ev3.screen.clear()
    #     ev3.screen.draw_text(0, 0, "INTERSECTION")
    #     robot.straight(35)
    #     robot.turn(TURN_RATE-10)  # Turn right
    #     robot.straight(25)

    # # If only the left sensor detects black, turn left OR left if detecting but the middle and right are not
    # elif (left_reflection <= LEFT_BLACK and middle_reflection <= MIDDLE_BLACK) or (left_reflection <= LEFT_BLACK and middle_reflection > MIDDLE_BLACK and right_reflection > RIGTH_BLACK):
    #     ev3.screen.clear()
    #     ev3.screen.draw_text(0, 0, "Left")
    #     robot.straight(65)
    #     robot.turn(-TURN_RATE)  # Turn left
    #     robot.straight(25)
    
    # # If only the right sensor detects black, turn right
    # elif (right_reflection <= RIGTH_BLACK and middle_reflection <= MIDDLE_BLACK) or (right_reflection <= RIGTH_BLACK and middle_reflection > MIDDLE_BLACK and left_reflection > LEFT_BLACK):
    #     ev3.screen.clear()
    #     ev3.screen.draw_text(0, 0, "Right")
    #     robot.straight(35)
    #     robot.turn(TURN_RATE-10)  # Turn right
    #     robot.straight(25)
    
    # if slightly on the black line with the middel sensor
    elif middle_reflection <= MIDDLE_THRESHOLD:
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "ALMOST Straight on the line")
        adjustValue = 27 - middle_reflection #it is 27, because it is the median value of the middle sensor reading all balck and all grey
        robot.drive(DRIVE_SPEED, adjustValue/2) #multiplly with 2 in order to turn enough 

    #If on the black line go straight
    #probaly never used as the slightly on the line is more powerful
    # elif middle_reflection <= MIDDLE_BLACK: 
    #     ev3.screen.clear()
    #     ev3.screen.draw_text(0, 0, "Straight on the line")
    #     robot.drive(DRIVE_SPEED, 0)

    # Not on the line.. turn slight angle of 5 degrees to left
    else:
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "No line, go left 5")
        robot.turn(-5)
        wait(200)
    # Short wait to avoid busy-waiting
    wait(100)
