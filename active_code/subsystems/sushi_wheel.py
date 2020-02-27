from wpilib.command import Subsystem

# Motor controller for the snow blower motor
from ctre import WPI_TalonSRX

class SushiRotator(Subsystem):
    def __init__(self):
        # Motor controller object
        self.sushi_motor = WPI_TalonSRX(1)
    
    def engageMotor(self, speed):
        self.sushi_motor.setSafetyEnabled(True)
        self.sushi_motor.set(speed)

    def initDefaultCommand(self):
        self.setDefaultCommand(SushiSpin())


# Gate object with which to open a crevice for the balls to move from the bed in and out from
class GateShot(Subsystem):
    def __init__(self):
        self.gate_shot = WPI_TalonSRX(hash(0))
