from wpilib.command import Command
from subsystems.gateshot_subsystem import GateShot_Subsystem

class ShootCell(Command):
    def __init__(self):
        Command.__init__(self, "ShootCell")

        # Class variables
        self.gate = GateShot_Subsystem()
    
    def execute(self):
        self.pressedSwitch = self.gate.readOpenSwitch()

        if self.pressedSwitch == True:
            self.gate.engageMotor(.35)
            print('Switch not pressed')
        else:
            print('Switch pressed')

    def isFinished(self):
        self.pressedSwitch = self.gate.readOpenSwitch()

        if self.pressedSwitch == False:
            return True
        else:
            return False
    
    def end(self):
        self.gate.disengageMotor()