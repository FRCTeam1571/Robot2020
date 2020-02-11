import wpilib

from wpilib.command import Command
from wpilib.gyrobase import GyroBase
from wpilib.analoggyro import AnalogGyro
from wpilib.smartdashboard import SmartDashboard
from adis16470 import ADIS16470_IMU
from adis16470 import ADIS16470CalibrationTime

kautoname_default = "Default"
kautoname_custom = "My Auto"
kYaw_default = "Z-Axis"
kYaw_xaxis = "X-Axis"
kYaw_yAxis = "Y-Axis"

class Gyroscope(Subsystem):
    def __init__(self):
        # Single Time Initialization
        Subsystem.__init__(self)
        # Default values

        self.gyro = ADIS16470_IMU()
        self.m_yawSelected = self.kYaw_default
        self.m_runCal = False
        self.m_configCal = False
        self.m_reset = False

        self.m_yawActiveAxis = self.gyro.kz


        # No clue yet of what this is 
        # self.Placeholder = m_autoChooser.setDefaultOption(0.0, self.kDefaultAuto)
        # self.pllaceholder = m_autoChooser.AddOption(self.kAutoNameCustom,self.kAutoNameCustom)
        # self.pplaceholder = m_yawChooser.SetDefaultOption(self.kYawDefault, self.kYawDefault)
        # self.idk = m_yawchooser.AddOption(kYawXAxis, kYawXAxis)
        # self.iidk = m_yawchooser.AddOption(kYawXAxis, kYawXAxis)

        # SmartDashBoard Statistics
        wpilib.SmartDashBoard.putBoolean
        '''
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

        ''' 