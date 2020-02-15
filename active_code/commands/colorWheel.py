import wpilib

from wpilib.command import Command
from subsystems import MasterController
from commands import mathRotate
from commands import readColor

class colorWheel(Command):
    def __init__(self):
        Command.__init__(self)

    def execute(self):
        robot = self.getRobot()

        mathPressed = self.getRobot().colorSpinner.getXButton()

        colorPressed = self.getRobot().colorSpinner.getYButton()

        if (mathPressed):
            mathRotate.mathRotate


