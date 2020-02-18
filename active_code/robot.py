import wpilib
from wpilib.command import Command
from commandbased import CommandBasedRobot
from subsystems.DriveTrain import DriveTrain
from subsystems.MasterController import MasterController
from commands import drive
from commands import colorWheel as cW

# import subsystems
from subsystems.ColorSpinner import ColorSpinner
#from adis16470 import ADIS16470_IMU
#from adis16470 import ADIS16470CalibrationTime

# from oi import OI
# from subsystems.sampsubsystem import SampSubsystem
# from subsystems.testsubsystem import TestSubsystem
# from commands.sampcommand import SampCommand
# from commands.testcommand import TestCommand
# from commands import seqcommandgr as SeqCommandGr
# from commands import paracommandgr as ParaCommandGr
# from commands import combinecommandgr as CombineCommandGr



class Robot(CommandBasedRobot):
    ''' Statement of commands '''
    def robotInit(self):
        self.controller = MasterController()
        self.driveTrain = DriveTrain()
        self.colorSpinner = ColorSpinner()

        Command.getRobot = lambda x=0: self
        #self.gyro = ADIS16470_IMU()
        #self.m_imu.GetAngle()


        Command.getRobot = lambda x=0: self

        self.timer = wpilib.Timer() 

        # self.sampSubsystem = SampSubsystem()
        # self.testSubsystem = TestSubsystem()
        # self.autonomousCommand = SampCommand()
        # self.oi = OI()


    def robotPeriodic(self):
        # add later
        if self.timer.get() == 0.0 :
            self.timer.start()
        elif self.timer.hasPeriodPassed(2) :
            print("Periodic method")
        elif self.timer.hasPeriodPassed(2.5) :
            self.timer.reset()

    def autonomousInit(self):
        # add later
        print("Autonomous Mode")
        if (self.autonomousCommand != None) : 
            self.autonomousCommand.start()

    def autonomousPeriodic(self):
        if self.timer.hasPeriodPassed(2) :
            print("Autonomous Run")
        
        # self.scheduler.addCommand(ParaCommandGr()) 
        # self.scheduler.run()


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

         #self.controller.readController()

        #call a command to run other commands after checking the controller
        # wheel = cW.colorWheel()
        # wheel.execute()
        
            
        #Turn on motor while Y is pressed
        # spin = self.controller.getYButton()
        # if (spin):
        #     self.colorSpinner.engageMotor()
        # else :
        #     self.colorSpinner.engageMotor(0)


if __name__ == "__main__":
    wpilib.run(Robot)