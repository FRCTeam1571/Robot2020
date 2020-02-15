import wpilib

from wpilib.drive import DifferentialDrive
from wpilib.command import Subsystem
from commands import drive
import ctre

class DriveTrain(Subsystem):
    def __init__(self):
        # Ensures a single-time initialization
        Subsystem.__init__(self, "DriveTrain")

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
        self.drive.setExpiration(0.1) 

        # 
        self.drive.setSafetyEnabled(False)

    def initDefaultCommand(self):
        # self.driveCommand = Drive.Drive()
        try:        
            self.setDefaultCommand(drive.Drive)
        except TypeError:
            print("Error for drive")

    def engageDrive(self, speed, rotation):
        self.drive.arcadeDrive(speed, rotation)
        
