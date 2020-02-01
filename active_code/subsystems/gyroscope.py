import wpilib

from wpilib.command import Command
from wpilib.gyrobase import GyroBase
from wpilib.analoggyro import AnalogGyro
from adi.ADIS16470_IMU import ADIS16470_IMU

class Gyroscope(Subsystem):
    def __init__(self):
        Subsystem.__init__(self)
        self.imu = ADIS16470_IMU()
        
