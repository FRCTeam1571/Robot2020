import wpilib
from wpilib.command import Command
from commandbased import CommandBasedRobot
from subsystems.DriveTrain import DriveTrain
from subsystems.MasterController import MasterController
from commands import drive
from adis16470 import ADIS16470_IMU
from adis16470 import ADIS16470CalibrationTime

class Robot(CommandBasedRobot):
    ''' Statement of commands '''
    def robotInit(self):
        # self.controller = MasterController()
        # self.driveTrain = DriveTrain()

        # Command.getRobot = lambda x=0: self
        self.gyro = ADIS16470_IMU()
        self.m_imu.GetAngle()

    def autonomousInit(self):
        # add later
        print("Autonomous")


if __name__ == "__main__":
    wpilib.run(Robot)
    

