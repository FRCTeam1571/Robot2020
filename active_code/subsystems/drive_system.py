import wpilib

from wpilib.command.subsystem import Subsystem
import ctre

class DriveTrain(Subsystem):
    def __init__(self):
        # Ensures a single-time initialization
        super().__init__("DriveTrain")

        self.cont_left = ctre.TalonSRX.