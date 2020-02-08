import wpilib

from wpilib.command import Subsystem

class ColorSpinner(Subsystem):
    def __init__(self):

        self.motor = wpilib.NidecBrushless(0, 0)