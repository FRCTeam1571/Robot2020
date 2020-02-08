import wpilib

from wpilib.command import Command
from wpilib.gyrobase import GyroBase
from wpilib.analoggyro import AnalogGyro
from adi.ADIS16470_IMU import ADIS16470_IMU

class Gyroscope(Subsystem):
    def __init__(self):
        # Single Time Initialization
        Subsystem.__init__(self)
        #
        self.imu = ADIS16470_IMU()
        # Axis Values
        self.kYawDefault = 0.0 # Z-Axis
        self.kYawXAxis = 0.0
        self.kYawYAxis = 0.0

        self.runCal =

