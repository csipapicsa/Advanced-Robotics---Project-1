#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

ev3.speaker.beep()

from PID_control import PIDController

ev3.speaker.beep()

import time
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
motorA = Motor(Port.A)
motorB = Motor(Port.B)

# Create your objects here.


# Write your program here.
ev3.speaker.beep()

pid = PIDController(kp=0.4, ki=0.1, kd=0.01, setpoint=1000)

speed_variable = 0

driver = DriveBase(left_motor=motorA, right_motor=motorB, wheel_diameter=40, axle_track=130)


 for i in range(100):
        # Get the control signal from PID controller
        control_signal = pid.update(process_variable)
        
        if control_signal is not None:
            # Apply control signal to the process variable (simple simulation)
            speed_variable += control_signal * 0.1
            #motorA.run_time(speed=-speed_variable, time=1000, then=Stop.HOLD, wait=False)
            #motorB.run_time(speed=-speed_variable, time=1000, then=Stop.HOLD, wait=False)
            driver.drive(control_signal, 30)
    time.sleep(0.01)

