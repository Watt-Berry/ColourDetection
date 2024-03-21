import PiMotor
import time
import RPi.GPIO as GPIO

class MotorController:
    def __init__(self):
        #Name of Individual MOTORS
        self.m1 = PiMotor.Motor("MOTOR1",1)
        self.m2 = PiMotor.Motor("MOTOR2",1)
        self.m3 = PiMotor.Motor("MOTOR3",1)
        self.m4 = PiMotor.Motor("MOTOR4",1)

        #To drive all motors together
        self.motorAll = PiMotor.LinkedMotors(self.m1, self.m2, self.m3, self.m4)

        #Names for Individual Arrows
        self.ab = PiMotor.Arrow(1)
        self.al = PiMotor.Arrow(2)
        self.af = PiMotor.Arrow(3)
        self.ar = PiMotor.Arrow(4)

        self.reached = False

    def reached_wrapper(func):
        def wrapper(self):
            self.reached = False
            func(self)
            self.reached = True
        return wrapper

    @reached_wrapper
    def drive_forward(self):
        try:
            print("Robot Moving Forward ")
            self.af.on()
            self.motorAll.forward(100)
            time.sleep(5)
        except: pass

    @reached_wrapper
    def turn_left(self):
        try:
            print("Robot Moving Left ")
            self.ab.off()
            self.al.on()
            self.m1.reverse(100)
            self.m2.forward(100)
            self.m3.forward(100)
            self.m4.reverse(100)
            time.sleep(5)
        except: pass

    @reached_wrapper
    def turn_right(self):
        try:
            print("Robot Moving Right ")
            self.ar.on()
            self.al.off()
            self.m1.forward(100)
            self.m2.reverse(100)
            self.m3.reverse(100)
            self.m4.forward(100)
            time.sleep(5)
        except: pass

    @reached_wrapper
    def drive_backwards(self):
        try:
            print("Robot Moving Backward ")
            self.af.off()
            self.ab.on()
            self.motorAll.reverse(100)
            time.sleep(5)
        except: pass

    def stop(self):
        try:
            print("Robot Stop ")
            self.al.off()
            self.af.off()
            self.ar.off()
            self.motorAll.stop()
            time.sleep(5)
        except: pass

    def reached_destination(self):
        return self.reached