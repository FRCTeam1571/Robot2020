import wpilib

from wpilib.command.subsystem import Subsystem



class ColorSpinner(Subsystem):
    def __init__(self):

        self.motor = wpilib.NidecBrushless(0, 0)


