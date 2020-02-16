from wpilib.command import Command
from wpilib.command import GroupCommand

class paraCommandGr(GroupCommand) :
    def __init__(self):
        Command.__init__(self)        
        self.requires(self.getRobot().sampSubsystem)
        
    def execute(self):
        robot = self.getRobot()

        self.getRobot().controller.readController()
        speed = self.getRobot().controller.getSpeed()
        
        rotation = self.getRobot().controller.getLeftStick_x()
        self.getRobot().driveTrain.engageDrive(speed, rotation)

    # def initialize(self):
        # 


    # def end(self):
        # 