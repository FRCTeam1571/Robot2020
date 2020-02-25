import wpilib

from wpilib.command import Subsytem
from wpilib.doublesolenoid import doublesolenoid

class WheelPneumatics(Subsystem):
    def __init__(self):
        self.compressor = wpilib.compressor
        # self.compressor.setClosedLoopControl(True)

        self.dsolenoid = wpilib.doublesolenoid(1, 2)
        