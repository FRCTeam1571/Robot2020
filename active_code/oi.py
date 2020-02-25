
# Commands can run when the associated button is pressed by using whenPressed().
# Commands can run when a button is released by using whenReleased() instead of whenPressed().
# Commands can run continuously while the button is depressed by calling whileHeld().
# Commands can be toggled when a button is pressed using toggleWhenPressed().
# A command can be canceled when a button is pressed using cancelWhenPressed().
# Arbitrary conditions use the Trigger class to run a command.
# Triggers and Buttons are usually polled every 20ms or whenever the scheduler is called.

import wpilib
from wpilib.command import Command
from wpilib.command import JoystickButton
# from active_code.commands import (sampcommand, testcommand, instacommand, defcommand)
# from active_code.commands import (seqcommandgr, paracommandgr, combinecommandgr)
#from commands import (SampCommand, TestCommand, InstaCommand, DefCommand)
#from commands import (SeqCommandGr, ParaCommandGr, CombineCommandGr)

from robotConstants import XboxMap
from commands import drive
from commands.mathRotate import mathRotate



class OI():
    def __init__(self):
        self.controller = wpilib.XboxController(0)
        #joystick = wpilib.joystick(0)
        self.speedMultiplier = 0.9

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

        buttonA = JoystickButton(self.controller, XboxMap.BUTTONA)
        buttonB = JoystickButton(self.controller, XboxMap.BUTTONB)
        buttonX = JoystickButton(self.controller, XboxMap.BUTTONX)
        buttonY = JoystickButton(self.controller, XboxMap.BUTTONY)
        buttonStart = JoystickButton(self.controller, XboxMap.BUTTONSTART)

        buttonX.whenPressed(mathRotate())

        # buttonA.whenPressed(SampCommand())
        # buttonB.whenPressed(TestCommand())
        # buttonX.whenPressed(SeqCommandGr())
        # buttonY.whenPressed(ParaCommandGr())
        # buttonStart.whenPressed(CombineCommandGr())

        
    def getLeftX(self) :
        self.leftstick_x = self.controller.getX(XboxMap.KLEFT) * self.speedMultiplier
        return self.leftstick_x

    def getLeftY(self) :
        self.leftstick_y = self.controller.getY(XboxMap.KLEFT) * self.speedMultiplier
        return self.leftstick_y

    def getRightX(self) :
        self.rightstick_x = self.controller.getX(XboxMap.KRIGHT) 
        return self.rightstick_x

    def getRightY(self) :
        self.rightstick_y = self.controller.getY(XboxMap.KRIGHT) 
        return self.rightstick_y

    '''--------------------------------------------------------'''

    def readLeftTrig(self):
        self.trigLeft = self.controller.getTriggerAxis(self.kLeft)
        return self.trigLeft

    def readRightTrig(self):
        self.trigRight = self.controller.getTriggerAxis(self.kRight)
        return self.trigRight

    def getSpeed(self):
        self.speed = (self.trigRight - self.trigLeft) * self.speedMultiplier
        return self.speed

    def readLeftStickX(self):
        self.leftstick_x = self.controller.getX(self.kLeft) * self.speedMultiplier
        return self.leftstick_x

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