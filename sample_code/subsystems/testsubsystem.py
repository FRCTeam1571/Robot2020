import wpilib
from wpilib.command import Subsystem
import ctre 
from robotconstants import SubSystemPort


class TestSubsystem(Subsystem):
    def __init__(self):
      Subsystem.__init__(self, "TestSubsystem")
        
      self.spinSpeed = 0
      self.motor = ctre.WPI_TalonSRX(SubSystemPort.KMOTORPORT)

      self.motor.setExpiration(2.5)
      self.motor.setSafetyEnabled(False)

      #Show Motor status in NT
      self.addChild("Motor", self.motor)   
      self.endSwitch = True

    #set a default command for the Subsystem
    def initDefaultCommand(self) :
      print("Default Command for TestSubsystem")
      # self.setDefaultCommand(defCommand)

    # spin motor Forward
    def forward(self) :
      speed = 1.0
      self.motor.set(speed)

    # spin motor in Reverse
    def reverse(self) : 
      speed = -1.0
      self.motor.set(speed)

    # spin motor in Reverse
    def stop(self) : 
      speed = 0.0
      self.motor.set(speed)

    # signal endpoint
    def isEndPoint(self) : 
      return endSwitch 
