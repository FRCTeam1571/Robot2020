from wpilib.command import Subsystem

# Motor controller for the snow blower motor
from ctre import WPI_TalonSRX

from commands.sushi_act import Sushi_Act

class SushiRotator(Subsystem):
    def __init__(self):
        Subsystem.__init__(self, 'SushiRotator')
        # Motor controller object
        self.sushi_motor = WPI_TalonSRX(1)
        
    
    def engageMotor(self, speed):
        self.sushi_motor.setSafetyEnabled(False)
        self.sushi_motor.set(speed)

    def initDefaultCommand(self):
        self.setDefaultCommand(Sushi_Act())
