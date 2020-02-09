import wpilib
import ctre

from wpilib.command import Subsystem
from networktables import NetworkTables
from wpilib import SmartDashboard

#from commands import mathRotate

class MasterController(Subsystem):
    def __init__(self):
        self.previous = 0.0
        self.controller = wpilib.XboxController(0)

        # Sides
        self.kLeft = self.controller.Hand.kLeftHand
        self.kRight = self.controller.Hand.kRightHand

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

        # Half speed to max speed
        self.speedArray = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        self.speedIndex = 4

        #Color rotate buttons
        self.mathSpinButton = False
        self.colorSpinButton = False


    def readStick(self):
        #Get the values for the triggers and stick for basic driving
        self.trigLeft = self.controller.getTriggerAxis(self.kLeft)
        self.trigRight = self.controller.getTriggerAxis(self.kRight)
        self.speed = (self.trigRight - self.trigLeft) * self.speedMultiplier

        self.leftstick_x = self.controller.getX(self.kLeft) * self.speedMultiplier

    def readSpeedMultiplier(self):
        # Get speed up and down buttons to increase or decrease the speed for the drivetrain
        self.SpeedUpButton = self.controller.getAButtonPressed()
        self.SpeedDownButton = self.controller.getBButtonPressed()

        if (self.SpeedDownButton == True and self.speedIndex > 0):
            print("Up one")
            self.speedIndex -= 1

        elif (self.SpeedUpButton == True and self.speedIndex < len(self.speedArray)):
            print("Down one")
            self.speedIndex += 1

            if (self.SpeedUpButton == True and self.speedIndex >= 5):
                self.speedIndex = 5

        self.speedMultiplier = self.speedArray[self.speedIndex]

        wpilib.SmartDashboard.putNumber("Speed Multiplier", self.speedMultiplier)

    def readColorButtons(self):
        #read the values of the x and y buttons
        self.mathSpinButton = self.controller.getXButtonPressed()
        self.colorSpinButton = self.controller.getYButtonPressed()

        # if (self.mathSpinButton):
        #     rotateCom = mathRotate()
        #     rotateCom.execute()
        # if (self.colorSpinButton):
        #     rotateCom = colecommand()
        #     rotateCom.execute()

    def readController(self):
        #Call this method to get status of controller
        self.readSpeedMultiplier()
        self.readStick()
        self.readColorButtons()

    def getLeftStick_x(self):
        print(self.leftstick_x)
        return self.leftstick_x

    def getTrigLeft(self):
        print("Left Trigger", self.trigLeft)
        return self.trigLeft

    def getTrigRight(self):
        print("Right Trigger", self.trigRight)
        return self.trigRight

    def getSpeed(self):
        previous = self.speed
        if (self.speed != previous):
            pass
        else:
            print("Speed", self.speed)
        return self.speed
        # get smartdashboard working k thanks
        # big oof


        #yw
    def getSpeedMultiplier(self):
        print(self.speedMultiplier)
        return self.speedMultiplier

    def getYButton(self):
        print(self.colorSpinButton)
        return self.colorSpinButton

    def getXButton(self):
        print(self.mathSpinButton)
        return self.mathSpinButton
