#import self.oi

from wpilib.command import Command

from wpilib.command import WaitCommand
#from subsystems import DriveTrain
#from subsystems import MasterController

class Drive(Command):
    def __init__(self):
        Command.__init__(self, "Drive")

        self.oi = self.getOi()
        self.robot = self.getRobot()
        self.speed = 0
        self.rotation = 0
        
        # self.controller = MasterController()
        # self.driveTrain = DriveTrain()
        self.requires(self.getRobot().driveTrain)

    def move(self):
        if self.oi.readRightTrig() != -1:
            self.speed = self.oi.getSpeed()
        elif self.oi.readLeftTrig() != -1:
             self.speed = self.oi.getSpeed()
        else:
            self.speed = 0
        return self.speed
       
    def turn(self):
        if self.oi.readLeftStickX() != 0:
            # Will rotate bot left
            if self.oi.readLeftStickX() < 0:
                self.rotation = self.oi.readLeftStickX()
            # Will rotate bot right
            elif self.oi.readLeftStickX() > 0:
                self.rotation = self.oi.readLeftStickX()
            else:
                self.rotation = 0
        return self.rotation
        
    def execute(self):
        self.robot.driveTrain.engageDrive(self.move(), self.turn())

    def isFinished(self):
        return False
    
    def end(self):
        self.robot.DriveTrain.engageDrive(0, 0)