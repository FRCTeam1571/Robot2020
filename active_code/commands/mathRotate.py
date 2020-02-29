import wpilib
from wpilib.command import Command

from subsystems.ColorSpinner import ColorSpinner

class SpinColorWheel(Command):
    def __init__(self):
        Command.__init__(self, "SpinColorWheel")

        # self.robot = self.getRobot()

        self.motor = ColorSpinner()

    def execute(self):
        self.motor.engageMotor()
    
    def isFinished(self):
        return False
    
    def end(self):
        self.motor.engageMotor(0)