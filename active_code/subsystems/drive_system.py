import wpilib

from wpilib.command.subsystem import Subsystem
import ctre

class DriveTrain(Subsystem):
    def __init__(self):
        # Ensures a single-time initialization
        super().__init__("DriveTrain")

        # Front Motor Controllers
        self.front_cont_right = ctre.WPI_TalonSRX(2)
        self.rear_cont_right = ctre.WPI_TalonSRX(3)
        self.right = wpilib.SpeedControllerGroup(self.front_cont_right, self.rear_cont_right)

        # Rear Motor Controllers
        self.front_cont_left = ctre.WPI_TalonSRright
        self.rear_cont_left = ctre.WPI_TalonSRX(1)
        self.left = wpilib.SpeedControllerGroup(self.front_cont_left, self.rear_cont_left)
        
        # Drive Type
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

    def engageDrive():
        