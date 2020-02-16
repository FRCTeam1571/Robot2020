
# Commands can run when the associated button is pressed by using whenPressed().
# Commands can run when a button is released by using whenReleased() instead of whenPressed().
# Commands can run continuously while the button is depressed by calling whileHeld().
# Commands can be toggled when a button is pressed using toggleWhenPressed().
# A command can be canceled when a button is pressed using cancelWhenPressed().
# Arbitrary conditions use the Trigger class to run a command.
# Triggers and Buttons are usually polled every 20ms or whenever the scheduler is called.

import wpilib
from wpilib.command import Command
from commands import sampCommand
from commands import testCommand

class oi():
    def __init__(self):
        joy = wpilib.joystick(0)

        button1 = wpilib.joystickButton(joy, 1)
        button2 = wpilib.joystickButton(joy, 2)

        button1.whenPressed(sampCommand())
        button2.whenPressed(testCommand())

