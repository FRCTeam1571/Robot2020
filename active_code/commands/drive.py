from wpilib.command import Command

from wpilib.command import WaitCommand
#from subsystems import DriveTrain
#from subsystems import MasterController

class Drive(Command):
    def __init__(self):
        Command.__init__(self, "Drive")
        # self.controller = MasterController()
        # self.driveTrain = DriveTrain()
        # self.requires(self.getRobot().driveTrain)
        
    def execute(self):
        robot = self.getRobot()

        self.getRobot().controller.readController()
        speed = self.getRobot().controller.getSpeed()
        
        rotation = self.getRobot().controller.getLeftStick_x()
        self.getRobot().driveTrain.engageDrive(speed, rotation)

<<<<<<< .merge_file_a32524
=======
    def isFinished(self):
        return False

>>>>>>> .merge_file_a29852
    # def initialize(self):
        # 


    # def end(self):
        # 
