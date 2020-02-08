import wpilib

from wpilib.command import TimedCommand

from Subsystems import MasterController
from Subsystems import ColorSpinner

class mathRotate(TimedCommand):
    def __init__(self, "mathRotate", 6.0):

        # self.requires(self.getRobot().ColorSpinner)
        """RPM = 475 so send 1 amp on the PWM
        Run for 6 seconds"""

    def execute(self):
        robot = self.getrobot()

        #move to new command
        run = self.getRobot().controller.getYbutton()

        value = self.getRobot().colorSpinner.function()






        