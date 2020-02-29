import wpilib


class Robot(wpilib.TimedRobot):
    ''' Statement of commands '''
    def robotInit(self):
        self.timer = wpilib.Timer()

    def teleopInit(self):
        self.compressor = wpilib.compressor
        # self.compressor.setClosedLoopControl(True)

        self.dsolenoid = wpilib.doublesolenoid(1, 2)

        
        self.limitSwitch = wpilib.DigitalInput(0)
        self.limitSwitch2 = wpilib.DigitalInput(1)

    def teleopPeriodic(self):
        self.limitSwitch.get()
        self.limitSwitch2.get()
        wpilib.SmartDashboard.putNumber("Switch Value", self.limitSwitch)
        wpilib.SmartDashboard.putNumber("Switch Value", self.limitSwitch2)


if __name__ == "__main__":
    wpilib.run(Robot)
