import hal
import wpilib
from wpilib.command import Subsystem
import ctre
from commands.defcommand import DefCommand

class SampSubsystem(Subsystem):
    def __init__(self):
      Subsystem.__init__(self, "SampSubsystem")
        
      self.spinSpeed = 0
      self.motor = wpilib.NidecBrushless(0, 0)
      #self.motor = ctre.WPI_TalonSRX(0)

      self.motor.setExpiration(2.5)
      self.motor.setSafetyEnabled(False)

      #Show Motor status in NT
      self.addChild("Motor", self.motor)   
      self.endSwitch = True

      self.limitSwitch = wpilib.DigitalInput(1)
      self.limitSwitchLow = wpilib.DigitalInput(2)
      #m_simDevice = hal.SimDevice("LimitSwitch", 1)
      #RobotBase.isReal()
      #if m_simDevice :
      #  self.limitSwitch.setSimDevice(1)

      self.counter = wpilib.Counter(self.limitSwitch)

      self.onLED = wpilib.DigitalOutput(3)


    #set a default command for the Subsystem
    def initDefaultCommand(self) :
      print("Default Command for SampSubsystem")
      self.setDefaultCommand(DefCommand())

    def isSwitchSet(self):
      return counter.Get() > 0

    def initializeCounter(self):
      counter.Reset()


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
