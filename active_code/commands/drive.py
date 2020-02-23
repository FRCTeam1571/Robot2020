from wpilib.command import Command

from wpilib.command import WaitCommand
from oi import OI as oi
#from subsystems import DriveTrain
#from subsystems import MasterController

class Drive(Command):
    def __init__(self):
        Command.__init__(self, "Drive")

        self.robot = self.getRobot()
        self.speed = 0
        self.rotation = 0
        
        # self.controller = MasterController()
        # self.driveTrain = DriveTrain()
        # self.requires(self.getRobot().driveTrain)

    def move(self):
        if oi.readRightTrig() != -1:
            self.speed = oi.getSpeed()
        elif oi.readLeftTrig() != -1:
             self.speed = oi.getSpeed()
        else:
            self.speed = 0
        return self.speed
       
    def turn(self):
        if oi.readLeftStickX() != 0:
            # Will rotate bot left
            if oi.readLeftStickX < 0:
                self.rotation = oi.readLeftStickX
            # Will rotate bot right
            elif oi.readLeftStickX > 0:
                self.rotation = oi.readLeftStickX
            else:
                self.rotation = 0
        return self.rotation
        
    def execute(self):
        self.robot.driveTrain.engageDrive(move(), turn())

    def isFinished(self):
        return False
    
    def end(self):
        self.robot.DriveTrain.engageDrive(0, 0)