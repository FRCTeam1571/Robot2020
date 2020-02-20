# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import wpilib
from wpilib.command import Command
from wpilib.command import Scheduler
from commandbased import CommandBasedRobot


from oi import OI
from subsystems.sampsubsystem import SampSubsystem
from subsystems.testsubsystem import TestSubsystem
from commands.sampcommand import SampCommand
from commands.testcommand import TestCommand
from commands.seqcommandgr import SeqCommandGr
from commands.paracommandgr import ParaCommandGr
from commands.combinecommandgr import CombineCommandGr



class Robot(CommandBasedRobot):
    ''' Statement of commands '''
    def robotInit(self):
        Command.getRobot = lambda x=0: self

        self.timer = wpilib.Timer() 
        self.oneShot = False

        self.sampSubsystem = SampSubsystem()
        self.testSubsystem = TestSubsystem()
        self.autonomousCommand = SampCommand()
        self.oi = OI()

    #----------------------------------------------------
    def robotPeriodic(self):
        if self.timer.get() == 0.0 :
            self.timer.start()
        elif self.timer.hasPeriodPassed(2) :
            print("Robot Periodic method run")
        elif self.timer.hasPeriodPassed(2.5) :
            self.timer.reset()
   
    #----------------------------------------------------
    def disabledInit(self):
        print("Disabled Mode")

    def disabledPeriodic(self):
        if self.timer.hasPeriodPassed(2) :
            print("Disabled Run")

    #----------------------------------------------------
    def testInit(self):
        print("Test Mode")

    def testPeriodic(self):
        if self.timer.hasPeriodPassed(2) :
            print("Test Run")

    #----------------------------------------------------
    def autonomousInit(self) :
        # add later
        print("Autonomous Mode")
        if (self.autonomousCommand != None) : 
            self.autonomousCommand.start()

    def autonomousPeriodic(self):
        if self.timer.hasPeriodPassed(2) :
            print("Autonomous Run")
        
        if (self.oneShot == False) : 
            Scheduler.getInstance().addCommand(ParaCommandGr()) 
            self.oneShot = True

        Scheduler.getInstance().run()

    #----------------------------------------------------
    def teleopInit(self):
        print("Teleop Mode")

    def teleopPeriodic(self):
        if self.timer.hasPeriodPassed(2) :
            print("Teleop method")

        Scheduler.getInstance().run()


    #----------------------------------------------------
#----------------------------------------------------
if __name__ == "__main__":
    wpilib.run(Robot)