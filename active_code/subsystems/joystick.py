import wpilib
import ctre

from wpilib.command.subsystem import Subsystem

class MasterController(Subsystem):
    def __init__(self):
        self.controller = wpilib.XboxController(0)

        # Sides
        self.kLeft = self.controller.Hand.kLeft()
        self.kRight = self.controller.Hand.kRight()

        # Triggers
        self.trigLeft = 0.0
        self.trigRight = 0.0
        self.speed = 0.0
        self.speedMultiplier = 0.9

        # Analog Sticks
        self.leftstick_x = 0.0
        self.leftstick_y = 0.0

    def readStick():
        self.trigLeft = self.controller.getTriggerAxis(self.kLeft)
        self.trigRight = self.controller.getTriggerAxis(self.kRight)
        self.speed = (self.trigRight - self.trigLeft) * self.speedMultiplier

        self.leftstick_x = self.controller.getX(self.kLeft) * self.speedMultiplier

        ## TO DO: Write function to change value of the "speedMultiplier" 