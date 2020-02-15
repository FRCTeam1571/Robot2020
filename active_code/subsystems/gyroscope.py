import wpilib

#from wpilib.command import Command
from wpilib.command import Subsystem
from wpilib import GyroBase
from wpilib import AnalogGyro
from wpilib import SmartDashboard
from gyroscope import ADIS16470_IMU

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
        wpilib.SmartDashboard.putBoolean(False, "gyro status")
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