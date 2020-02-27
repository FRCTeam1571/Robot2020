from wpilib.command import Command

class SushiSpin(Command):
    def __init__(self):
        self.robot = self.getRobot()
        self.sushiWheel = self.getSushiWheel()

        self.requires(self.getRobot().SushiRotator)

        self.rpm = 0.5
        self.toggle = False
    
    def rotateSushi(self):
        print('placeholder')

    def execute(self):
        self.robot.sushiWheel.engageMotor(self.rpm)

    def isFinished(self):
        return False

    def end(self):
        self.robot.sushiWheel.engageMotor(0.0)
