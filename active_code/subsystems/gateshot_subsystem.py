# Gate object with which to open a crevice for the balls to move from the bed in and out from
import wpilib
from wpilib.command import Subsystem

# # Motor controller for the snow blower motor
from ctre import WPI_TalonSRX

class GateShot_Subsystem(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, "GateShot")
        self.gate_shot = WPI_TalonSRX(0)

        # Open
        self.switchOpen = wpilib.DigitalInput(1)
         # Close
        self.switchClose = wpilib.DigitalInput(0)

    def engageMotor(self, spinSpeed):
        self.gate_shot.set(spinSpeed)
        print('Gate open')
    
    def disengageMotor(self):
        self.gate_shot.set(0)

    def readCloseSwitch(self):
        return self.switchClose.get()

    def readOpenSwitch(self):
        return self.switchOpen.get()