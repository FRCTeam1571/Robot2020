import wpilib

from wpilib.command import Command

class colorWheel(Command):
    def __init__(self):
        Command.__init__(self)

    def execute(self):
        robot = self.getRobot()

        mathPressed = self.getRobot().colorSpinner.getXButton()

        # colorPressed = self.getRobot().colorSpinner.getYButton()

        # if (mathPressed):
        #     mathRotate()

