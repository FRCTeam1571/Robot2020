import wpilib

from wpilib.command import Subsystem



class ColorSpinner(Subsystem):
    def __init__(self):
        #self.spinSpeed = 0

        self.motor = wpilib.NidecBrushless(0, 0)# PMW and DIO pins

    def engageMotor(self, spinSpeed = 0.5):


        self.motor.set(spinSpeeed)


