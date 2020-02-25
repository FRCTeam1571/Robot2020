import wpilib

from wpilib.command import Subsystem
from wpilib import GyroBase
from wpilib import AnalogGyro
from wpilib import SmartDashboard
from wpilib import SendableChooser
#from adis16470 import ADIS16470_IMU
from wpilib import ADXRS450_Gyro
from wpilib import ADXL345_SPI

kautoname_default = "Default"
kautoname_custom = "My Auto"
kYaw_default = "Z-Axis"
kYaw_xaxis = "X-Axis"
kYaw_yAxis = "Y-Axis"

class Gyroscope(Subsystem):
    def __init__(self):
        # Single Time Initialization
        Subsystem.__init__(self, "Gyroscope")
        # Default values

        # self.gyro = ADIS16470_IMU()
        self.gyro = ADXRS450_Gyro
        self.accel = ADXL345_SPI
        # self.m_yawSelected = kYaw_default
        self.m_runCal = False
        self.m_configCal = False
        self.m_reset = False

        # self.m_yawActiveAxis = self.gyro.IMUAxis.kz

        # Adds Options. Very Helpful. 
        self.m_autoChooser = wpilib.SendableChooser()
        self.m_autoChooser.addOption(kautoname_custom, kautoname_custom)
        
        self.m_yawChooser = wpilib.SendableChooser()
        self.m_yawChooser.setDefaultOption(self.kYawDefault, self.kYawDefault)
        self.m_yawchooser.addOption(kYaw_xaxis, kYaw_xAxis)
        self.m_yawchooser.addOption(kYaw_yAxis, kYaw_yAxis)

        # SmartDashBoard Statistics
        wpilib.SmartDashboard.putBoolean("Config Calibration", False)
        wpilib.SmartDashboard.putBoolean("Run Calibration", False)
        wpilib.SmartDashboard.putBoolean("Reset Gyro", False)
        wpilib.SmartDashboard.putBoolean("Set Current Axis", False)

        def gyroControls(self):
            # wpilib.SmartDashboard.putNumber("Yaw/Z Angle", self.m_imu.getAngle())
            # wpilib.SmartDashboard.putNumber("X Comp Angle", self.m_imu.getXComplimentaryAngle())
            # wpilib.SmartDashboard.putNumber("Y Comp Angle", self.m_imu.getYComplimentaryAngle())
            wpilib.SmartDashboard.putNumber("Angle", self.gyro.GetAngle())

            self.m_yawSelected = kYawDefault
            wpilib.SmartDashboard.putNumber("Yaw/Z Angle", self.m_imu.getAngle())
            wpilib.SmartDashboard.putNumber("X Comp Angle", self.m_imu.getXComplimentaryAngle())
            wpilib.SmartDashboard.putNumber("Y Comp Angle", self.m_imu.getYComplimentaryAngle())
            
            self.m_yawSelected = kYaw_default

            # Set IMU Settings

            if (self.m_configCal):
                # self.configCalTime(self.imu._8s)
                self.m_configCal = wpilib.SmartDashboard.putBoolean("Config Calibration", False)
            
            if (self.m_reset):
                # self.m_imu.reset()
                self.m_reset = wpilib.SmartDashboard.putBoolean("Reset Gyro", False)

            if (self.m_runCal):
                # self.m_imu.Calibrate()
                self.m_runCal = wpilib.Smartdashboard.putBoolean("Run Calibration", False)

            # Read the Axis you want to read
            # Sendable Chooser allows you to change the value, hence changing what is displayed.

            if (self.m_yawSelected == "X-Axis"):
                self.m_yawActiveAxis = self.m_imu.IMUAxis.kX
            
            elif (self.m_yawSelected == "Y-Axis"):
                self.m_yawActiveAxis = self.m_imu.IMUAxis.kY
                
            else: 
                # self.m_yawActiveAxis = self.m_imu.IMUAxis.kZ
                pass
            # Set the Axis you want to read
            if (self.m_setYawAxis):
                self.m_setYawAxis = wpilib.SmartDashboard.putBoolean("setYawAxis", False)
                
        """
        plan:
        [] 1. Get the x-axis reading. it's ok to look up what you need!
        [] 2. Get it into smartdashboard/console print
        [] 3. trial and error. not working? debug?
        [] 4. Get the rest of the axis working
            [] Y axis
            [] Z axis
        [] 5. What should i do w/ this information?
            [] say what angle the robot is facing
            [] show how fast the robot is going.

        """