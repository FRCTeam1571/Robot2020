import wpilib
from wpilib.command import Command
from commandbased import CommandBasedRobot
from subsystems.DriveTrain import DriveTrain
from subsystems.MasterController import MasterController
from commands import drive
from subsystems.gyroscope import Gyroscope

import subsystems
from subsystems.ColorSpinner import ColorSpinner
#from adis16470 import ADIS16470_IMU
#from adis16470 import ADIS16470CalibrationTime

class Robot(CommandBasedRobot):
    ''' Statement of commands '''
    def robotInit(self):
        # self.controller = MasterController()
        # self.driveTrain = DriveTrain()
        # self.colorSpinner = ColorSpinner()
        #self.motor = wpilib.NidecBrushless(0, 0)

        # Command.getRobot = lambda x=0: self
        #self.gyro = ADIS16470_IMU()
        #self.m_imu.GetAngle()
        self.gyro = Gyroscope()


        Command.getRobot = lambda x=0: self

        self.timer = wpilib.Timer() 


    def robotPeriodic(self):
        # add later
        if self.timer.get() == 0.0 :
            self.timer.start()
        elif self.timer.hasPeriodPassed(2) :
            print("Periodic method")
        elif self.timer.hasPeriodPassed(2.5) :
            self.timer.reset()
        self.gyro.gyroControls()

    def autonomousInit(self):
        # add later
        print("Autonomous Mode")

    def autonomousPeriodic(self):
        # add later
        if self.timer.hasPeriodPassed(2) :
            print("Autonomous Run")

    def disabledInit(self):
        # add later
        print("Disabled Mode")

    def disabledPeriodic(self):
        # add later
        if self.timer.hasPeriodPassed(2) :
            print("Disabled Run")

    def testInit(self):
        # add later
        print("Test Mode")

    def testPeriodic(self):
        # add later
        if self.timer.hasPeriodPassed(2) :
            print("Test Run")


    def teleopInit(self):
        # add later
        print("Teleop Mode")

    def teleopPeriodic(self):
        # add later
        if self.timer.hasPeriodPassed(2) :
            print("Teleop method")
            
        spin = self.controller.getYButton()
        if (spin == True) :
            self.colorSpinner.engageMotor()
        else :
            self.colorSpinner.engageMotor(0)


if __name__ == "__main__":
    wpilib.run(Robot)
    

