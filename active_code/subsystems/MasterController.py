import wpilib
import ctre

from wpilib.command.subsystem import Subsystem
from networktables import NetworkTables
from wpilib.smartdashboard import SmartDashboard

class MasterController(Subsystem):
    def __init__(self):
        self.controller = wpilib.XboxController(0)

        # Sides
        self.kLeft = self.controller.Hand.kLeft
        self.kRight = self.controller.Hand.kRight

        # Triggers
        self.trigLeft = 0.0
        self.trigRight = 0.0
        self.speed = 0.0
        self.speedMultiplier = 0.9

        # Analog Sticks
        self.leftstick_x = 0.0
        self.leftstick_y = 0.0

        #Speed Multiplier Button
        self.speedUpButton = False
        self.speedDownButton = False
        self.speedArray = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        self.speedIndex = 4

    def readStick():
        #Get the values for the triggers and stick for basic driving
        self.trigLeft = self.controller.getTriggerAxis(self.kLeft)
        self.trigRight = self.controller.getTriggerAxis(self.kRight)
        self.speed = (self.trigRight - self.trigLeft) * self.speedMultiplier

        self.leftstick_x = self.controller.getX(self.kLeft) * self.speedMultiplier



    def readSpeedMultiplier():
        # Get speed up and down buttons to increase or decrease the speed for the drivetrain
        self.SpeedUpButton = self.controller.getAButtonPressed()
        self.SpeedDownButton = self.controller.getBButtonPressed()

        if (self.SpeedDownButton == True and self.speedIndex > 0):
            self.speedIndex -= 1
        
        if (self.SpeedUpButton == True and self.speedIndex < len(self.speedArray)):
            self.speedIndex += 1

        self.speedMultiplier = self.speedArray[self.speedIndex]

        SmartDashboard.putData("Speed Multiplier", self.speedMultiplier)

    def readController():
        #Call this method to get status of controller
        readSpeedMultiplier()
        readStick()

    def getLeftStick_x():
        return self.leftstick_x

    def getTrigLeft():
        return self.trigLeft

    def getTrigRight():
        return self.trigRight

    def getSpeed():
        return self.speed

    def getSpeedMultiplier():
        return self.speedMultiplier
    
