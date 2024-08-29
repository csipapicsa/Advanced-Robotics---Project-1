#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Create your objects here.
ev3 = EV3Brick()

#Motors
motorA = Motor(Port.A)
motorB = Motor(Port.B)

driver = DriveBase(left_motor=motorA, left_motor=motorB, wheel_diameter=40, axle_track=130)

#Sensor
sensorA = ColorSensor(Port.S1)
sensorB = ColorSensor(Port.S2)


# Write your program here.
#Play beep sound
ev3.speaker.beep() 

for i in range(6):
    target_angle = 150
    if (sensorA.reflection() < 10): # on the black line with sensor A
        motorA.run_angle(speed=-600, rotation_angle=target_angle, wait=True)
    
    elif (sensorB.reflection() < 10): # on the black line with sensor A
        motorB.run_angle(speed=-600, rotation_angle=target_angle, wait=True)
    
    else: # continue straight
        motorA.run_time(speed=-600, time=1000, then=Stop.HOLD, wait=False)
        motorB.run_time(speed=-600, time=1000, then=Stop.HOLD, wait=True)


# #Play beep sound
# ev3.speaker.beep() 

# #going straight for a certain time = 22 cm
# for i in range(1):
#     motorA.run_time(speed=-600, time=1000, then=Stop.HOLD, wait=False)
#     motorB.run_time(speed=-600, time=1000, then=Stop.HOLD, wait=True)
#     # motorA.stop()
#     # motorB.stop()
#     # Play another beep sound.
#     # ev3.speaker.beep(1000, 500)

# # Play another beep sound.
# ev3.speaker.beep(1000, 500)
