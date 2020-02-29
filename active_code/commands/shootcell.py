from wpilib.command import Command
from subsystems.gateshot_subsystem import GateShot_Subsystem

class ShootCell(Command):
    def __init__(self):
        Command.__init__(self, "ShootCell")

        # Class variables
        self.gate = GateShot_Subsystem()
        self.orientation = 0

    def masterGateControl(self):
        if (self.gate.readSushiSwitch() == True) and (self.gate.readCloseSwitch() == True):
            self.openGate()
        elif (self.gate.readOpenSwitch() == True):
            self.closeGate()
        else:
            print('error')
    
    def openGate(self):
        self.gate.engageMotor(.35)
        self.orientation = 1


    def closeGate(self):
        self.gate.engageMotor(-.35)
        self.orientation = 0
    
    def execute(self):
        self.masterGateControl()

    def isFinished(self):
        return False
    
    def end(self):
        self.gate.disengageMotor()