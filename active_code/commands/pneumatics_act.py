import wpilib

from wpilib.command import Command
from subsystems.pneumatics import Pneumatics

class SolenoidControl(Command):
    def __init__(self):
        Command.__init__(self, "SolenoidControl")

        self.pneumatic_subsystem = Pneumatics()
        self.piston = self.pneumatic_subsystem.dsolenoid
        self.sol_value = wpilib.DoubleSolenoid.Value

    def execute(self):
        self.piston.set(self.sol_value.kReverse)

    def isFinished(self):
        return False
    
    def end(self):
        self.piston.set(self.sol_value.kForward)