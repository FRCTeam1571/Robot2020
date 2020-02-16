from wpilib.command import Command


class testCommand(Command):
    def __init__(self):
        Command.__init__(self)        
        self.requires(self.getRobot().testSubsystem)
        
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
