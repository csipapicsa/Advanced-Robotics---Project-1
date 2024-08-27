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

#Motor to port B
motorA = Motor(Port.A)
motorB = Motor(Port.B)

# Write your program here.
#Play beep sound
ev3.speaker.beep() 


# from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_B
# from ev3dev2.motor import SpeedPercent

# # Initialize the MoveSteering object
# steering_drive = MoveSteering(Port.A, Port.B)

# # Run both motors at the same speed (straight line)
# steering_drive.on_for_seconds(steering=0, speed=SpeedPercent(50), seconds=5)



# Run motor 500 degress per second + target angel 90 degress
# test_motor.run_target(speed=500, angle=90)

#angle to turn to
length_a = 200
length_b = 100
target_position_angle = 90 #length_a / length_B
motorA.run_target(speed=500, target_angle=target_position_angle)
motorB.run_target(speed=500, target_angle=target_position_angle)

# #going straight for a certain time


motorA.run_time(speed=500, time=5000)
motorB.run_time(speed=500, time=5000)

# #Go to target angle
# target_angle = 90
# motorA.run_target(speed=500, target_angle)
# motorB.run_target(speed=500, target_angle)


# Play another beep sound.
ev3.speaker.beep(frequency=1000, duration=500)
