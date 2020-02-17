
# Commands can run when the associated button is pressed by using whenPressed().
# Commands can run when a button is released by using whenReleased() instead of whenPressed().
# Commands can run continuously while the button is depressed by calling whileHeld().
# Commands can be toggled when a button is pressed using toggleWhenPressed().
# A command can be canceled when a button is pressed using cancelWhenPressed().
# Arbitrary conditions use the Trigger class to run a command.
# Triggers and Buttons are usually polled every 20ms or whenever the scheduler is called.

import wpilib
from wpilib.command import Command
from commands import sampCommand, testCommand, instaCommand, defCommand
from commands import seqCommandGr, paraCommandGr, combineCommandGr
from active_code.robotConstants import XboxMap


class oi():
    def __init__(self):
        self.controller = wpilib.XboxController(0)
        #joystick = wpilib.joystick(0)
        self.speedMultiplier = 0.9


        buttonA = wpilib.joystickButton(self.controller, XboxMap.BUTTONA)
        buttonB = wpilib.joystickButton(self.controller, XboxMap.BUTTONB)
        buttonX = wpilib.joystickButton(self.controller, XboxMap.BUTTONX)
        buttonY = wpilib.joystickButton(self.controller, XboxMap.BUTTONY)
        buttonStart = wpilib.joystickButton(self.controller, XboxMap.BUTTONSTART)

        buttonA.whenPressed(sampCommand())
        buttonB.whenPressed(testCommand())
        buttonX.whenPressed(seqCommandGr())
        buttonY.whenPressed(paraCommandGr())
        buttonStart.whenPressed(combineCommandGr())

        
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