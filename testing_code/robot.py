import wpilib
from adis16470 import ADIS16470_IMU
from adis16470 import ADIS16470CalibrationTime

kYaw_default = "Z-Axis"

class Robot(wpilib.TimedRobot):
    ''' Statement of commands '''
    def robotInit(self):
        self.timer = wpilib.Timer() 

        #self.gyro = ADIS16470_IMU()
        self.m_yawSelected = kYaw_default
        self.m_runCal = False
        self.m_configCal = False
        self.m_reset = False

        # self.m_yawActiveAxis = self.gyro.IMUAxis.kz

        # Adds Options. Very Helpful. 
        self.m_autoChooser = wpilib.SendableChooser()
        self.m_autoChooser.AddOption(kautoname_custom, kautoname_custom)

        self.m_yawChooser = wpilib.SendableChooser()
        self.m_yawChooser.SetDefaultOption(self.kYawDefault, self.kYawDefault)
        self.m_yawchooser.AddOption(kYaw_xaxis, kYaw_xAxis)
        self.m_yawchooser.AddOption(kYaw_yAxis, kYaw_yAxis)

        wpilib.SmartDashboard.putBoolean("Config Calibration", False)
        wpilib.SmartDashboard.putBoolean("Run Calibration", False)
        wpilib.SmartDashboard.putBoolean("Reset Gyro", False)
        wpilib.SmartDashboard.putBoolean("Set Current Axis", False)


    def disabledInit(self):
        # add later
        print("Disabled Mode")

    def disabledPeriodic(self):
        # add later
        if self.timer.hasPeriodPassed(2) :
            print("Disabled Run")

    
    def teleopInit(self):
        if self.timer.get() == 0.0 :
            self.timer.start()
        elif self.timer.hasPeriodPassed(2) :
            print("Teleop Mode")
        elif self.timer.hasPeriodPassed(2.5) :
            self.timer.reset()
        

    def teleopPeriodic(self):
        # add later
        if self.timer.hasPeriodPassed(2) :
            print("Teleop method")
            
        #wpilib.SmartDashboard.putNumber("Yaw/Z Angle", self.m_imu.getAngle())



if __name__ == "__main__":
    wpilib.run(Robot)
    

