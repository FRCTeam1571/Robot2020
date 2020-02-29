import wpilib

from wpilib.doublesolenoid import doublesolenoid

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.timer = wpilib.Timer()

    def teleopInit(self):
        self.compressor = wpilib.compressor
        # self.compressor.setClosedLoopControl(True)

        self.dsolenoid = wpilib.doublesolenoid(1, 2)

    def teleopPeriodic(self):
        print("placeholder")

