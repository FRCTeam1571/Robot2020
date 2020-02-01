from wpilib.command import Command
from subsystems import vision_sys

class ColorSensorV3(Command):
    def __init__(self):
        Command.__init__(self)
        
    def readcolor(self):
        