import wpilib
from wpilib.command import Command
from commandbased import CommandBasedRobot
from subsystems.DriveTrain import DriveTrain
from subsystems.MasterController import MasterController
from commands import drive

class Robot(CommandBasedRobot):
    ''' Statement of commands '''
    def robotInit(self):
        self.controller = MasterController()
        self.driveTrain = DriveTrain()

        Command.getRobot = lambda x=0: self

        

    def autonomousInit(self):
        # add later
        print("Autonomous")


if __name__ == "__main__":
    wpilib.run(Robot)
    

