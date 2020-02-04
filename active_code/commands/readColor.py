import wpilib
from wpilib.command import Command
from subsystems import vision_sys as vs

class ColorSensorV3(Command):
    def __init__(self):
        Command.__init__(self)
        self.totalRad = 0
        self.totalRot = 0
        
    # Function to read the starting color of the color panel
    def readcolor(self):
        wpilib.SmartDashboard.putNumber("Proximity", vs.getProx)
        