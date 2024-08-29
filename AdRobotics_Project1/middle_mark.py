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

#Motor to port B
motorA = Motor(Port.A)
motorB = Motor(Port.B)

# Write your program here.
#Play beep sound
ev3.speaker.beep() 

target_angle = 1500 #180 degrees
motorA.run_angle(speed=-600, rotation_angle=target_angle, wait=True)

#Play beep sound
ev3.speaker.beep() 

# #going straight for a certain time = 22 cm
for i in range(9):
    motorA.run_time(speed=-600, time=1000, then=Stop.HOLD, wait=False)
    motorB.run_time(speed=-600, time=1000, then=Stop.HOLD, wait=True)
    # motorA.stop()
    # motorB.stop()
    # Play another beep sound.
    # ev3.speaker.beep(1000, 500)

# Play another beep sound.
ev3.speaker.beep(1000, 500)
 
target_angle = 350 #45 degrees
motorA.run_angle(speed=-300, rotation_angle=target_angle, wait=True)

# Play another beep sound.
ev3.speaker.beep(1000, 500)