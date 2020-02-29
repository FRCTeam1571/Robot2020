import wpilib
from wpilib.command import Subsystem
from wpilib import DoubleSolenoid
from wpilib import Compressor

class Pneumatics(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, "Pneumatics")

        self.compressor = wpilib.Compressor(0)
        # self.compressor.setClosedLoopControl(True)

        self.dsolenoid = wpilib.DoubleSolenoid(0, 1)
        # self.offvalve = self.dsolenoid.Value.kOff
        self.offvalve = wpilib.DoubleSolenoid.Value.kOff
        self.dsolenoid.set(self.offvalve)

    def controlSolenoid(self, direction):
        self.dsolenoid.set(direction)