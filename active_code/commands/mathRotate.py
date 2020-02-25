import wpilib

from wpilib.command import TimedCommand

# from subsystems import MasterController
from subsystems import ColorSpinner

class mathRotate(TimedCommand):
    def __init__(self, mathRotate = "mathRotate", timeInSeconds = 6.0):

        TimedCommand.__init__(self, mathRotate, timeInSeconds)

        # self.requires(self.getRobot().ColorSpinner)
        """RPM = 475 so send 1 amp on the PWM
        Run for 6 seconds"""

    def initialize(self):
        #move to new command
        
        # self.getRobot().controller.readController()
        # run = self.getRobot().controller.getXbutton()

        # if (run):
        self.getRobot().colorSpinner.engageMotor(0.5) #Give it the percent speed to run at, default = 0.5

    def engage(self):
        print("Rotating Motor")

        self.getRobot().colorSpinner.engageMotor(0.5) #Give it the percent speed to run at, default = 0.5


    # def isFinished(self):


    #stop the motor when the command ends
    def end(self):
        self.getRobot().colorSpinner.engageMotor(0)



        