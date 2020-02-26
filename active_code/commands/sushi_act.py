from subsystems import sushi_wheel as sw
from wpilib.command import Command

class SushiSpin(Command):
    def __init__(self):
        self.robot = getRobot()
        self.sushi_wheel = sw.SushiRotator()

        self.requires(self.getRobot().SushiRotator)

        self.rpm = 0.5
        self.toggle = False
    
    def rotateSushi(self):
        print('placeholder')

    def execute(self):
        self.robot.SushiRotator.engageDrive(self.rpm)

    def isFinished(self):
        return False

    def end(self):
        self.robot.SushiRotator.engageDrive(0.0)
