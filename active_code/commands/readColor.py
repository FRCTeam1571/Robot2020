import wpilib
from wpilib.command import Command
from wpilib.command import Scheduler
from subsystems import vision_sys as vs

class ColorSensorV3(Command):
    def __init__(self):
        Command.__init__(self)
        self.requires(rev.color.ColorSensorV3)

        self.totalRad = 0
        self.totalRot = 0

        self.vals = {"Proximity" : vs.Sensor.getProx, "Red" : vs.Sensor.getRed, "Green" : vs.Sensor.getGreen, "Blue" : vs.Sensor.getBlue}
        self.dash = wpilib.SmartDashboard

        '''self.color = [red, green, blue]'''
        self.rgbRed = [.42, .37, .25]
        self.rgbGreen = [.19, .52, .25]
        self.rgbBlue = [.15, .45, .34]
        self.rgbYellow = [.32, .52, .12]

        # Tolerance that values can comfortably fall within
        self.offset = .05
        self.isColor = False
        self.bal = 0
        
    # Function to read the starting color of the color panel
    def readcolor(self):
        for val in self.vals:
            self.dash.putNumber(val, self.vals[val])
        
        self.dash.updateValues()

    # def execute(self):
        