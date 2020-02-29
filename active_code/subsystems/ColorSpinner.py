import wpilib
import ctre

from wpilib.command import Subsystem
# from commands.mathRotate import SpinColorWheel

class ColorSpinner(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, "ColorSpinner")
        #def __init__(self, name = "ColorSpinner"):
        self.spinSpeed = 0
        self.motor = ctre.WPI_TalonSRX(6)# PMW and DIO pins
        self.motor.setExpiration(0.1)

    def engageMotor(self, spinSpeed = 0.35):
        self.motor.setSafetyEnabled(False)
        self.motor.set(spinSpeed)

    # def initDefaultCommand(self):
    #     self.setDefaultCommand(SpinColorWheel())