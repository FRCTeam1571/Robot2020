import wpilib

from wpilib.drive import DifferentialDrive
from wpilib.command.subsystem import Subsystem
import ctre
from commands.drive import Drive

class DriveTrain(Subsystem):
    def __init__(self):
        # Ensures a single-time initialization
        super().__init__("DriveTrain")

        # Front Motor Controllers
        self.front_cont_right = ctre.WPI_TalonSRX(7)
        self.rear_cont_right = ctre.WPI_TalonSRX(6)
        self.right = wpilib.SpeedControllerGroup(self.front_cont_right, self.rear_cont_right)

        # Rear Motor Controllers
        self.front_cont_left = ctre.WPI_TalonSRX(5)
        self.rear_cont_left = ctre.WPI_TalonSRX(4)
        self.left = wpilib.SpeedControllerGroup(self.front_cont_left, self.rear_cont_left)
        
        # Drive Type
        self.drive = DifferentialDrive(self.left, self.right)

    def initDefaultCommand(self):
        # self.driveCommand = Drive.Drive()
        self.setDefaultCommand(Drive())

    def engageDrive(self, speed, rotation):
        self.drive.arcadeDrive(speed, rotation)
        
