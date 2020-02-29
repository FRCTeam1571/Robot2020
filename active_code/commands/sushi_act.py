from wpilib.command import Command

class Sushi_Act(Command):
    def __init__(self):
        Command.__init__(self, "Sushi_Act")
        self.robot = self.getRobot()
        #self.sushiWheel = self.getSushiWheel()

        self.requires(self.getRobot().sushiWheel)
        #self.requires(self.sushiWheel)

        self.rpm = 0.25
        self.toggle = False
    
    def rotateSushi(self):
        print('placeholder')

    def execute(self):
        self.robot.sushiWheel.engageMotor(self.rpm)

    def isFinished(self):
        return False

    def end(self):
        self.robot.sushiWheel.engageMotor(0.0)
