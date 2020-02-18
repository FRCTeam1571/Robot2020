
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
from commands.sampcommand import SampCommand
from commands.testcommand import TestCommand
from commands.instacommand import InstaCommand
from commands.defcommand import DefCommand
from commands.seqcommandgr import SeqCommandGr
from commands.paracommandgr import ParaCommandGr
from commands.combinecommandgr import CombineCommandGr
from robotconstants import XboxMap


class OI():
    def __init__(self):
        self.controller = wpilib.XboxController(0)
        #joystick = wpilib.joystick(0)
        self.speedMultiplier = 0.9


        buttonA = JoystickButton(self.controller, XboxMap.BUTTONA)
        buttonB = JoystickButton(self.controller, XboxMap.BUTTONB)
        buttonX = JoystickButton(self.controller, XboxMap.BUTTONX)
        buttonY = JoystickButton(self.controller, XboxMap.BUTTONY)
        buttonStart = JoystickButton(self.controller, XboxMap.BUTTONSTART)

        buttonA.whenPressed(SampCommand())
        buttonB.whenPressed(TestCommand())
        buttonX.whenPressed(SeqCommandGr())
        buttonY.whenPressed(ParaCommandGr())
        buttonStart.whenPressed(CombineCommandGr())

        
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