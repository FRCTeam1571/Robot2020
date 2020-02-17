import wpilib
from wpilib.command import Subsystem
import ctre 
from robotConstants import SubSystemPort

class testSubsystem(Subsystem):
    def __init__(self):
      Subsystem.__init__(self, "testSubsystem")
        
      self.spinSpeed = 0
      self.motor = ctre.WPI_TalonSRX(SubSystemPort.KMOTORPORT)

      self.motor.setExpiration(0.1)
      self.motor.setSafetyEnabled(True)

      #Show Motor status in NT
      self.addChild("Motor", self.motor)   
      self.endSwitch = True

    #set a default command for the Subsystem
    def initDefaultCommand(self) :
      print("Default Command for testSubsystem")
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
