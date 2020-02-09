import wpilib

from wpilib.command import TimedCommand

# from subsystems import MasterController
# from subsystems import ColorSpinner

class mathRotate(TimedCommand):
    def __init__(self, mathRotate = "mathRotate", timeInSeconds = 6.0):

        # self.requires(self.getRobot().ColorSpinner)
        """RPM = 475 so send 1 amp on the PWM
        Run for 6 seconds"""

    def execute(self):
        robot = self.getrobot()

        #move to new command
        run = self.getRobot().controller.getYbutton()

        self.Robot().ColorSpinner.engageMotor(0.5) #Give it the percent speed to run at, default = 0.5






        