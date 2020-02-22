import wpilib
from wpilib.command import Command
from subsystems import vision_sys as vs

class ColorSensorV3(Command):
    def __init__(self):
        Command.__init__(self)
        self.totalRad = 0
        self.totalRot = 0

        self.vals = {"Proximity" : vs.Sensor.getProx, "Red" : vs.Sensor.getRed, "Green" : vs.Sensor.getGreen, "Blue" : vs.Sensor.getBlue}
        self.dash = wpilib.SmartDashboard
        
    # Function to read the starting color of the color panel
    def readcolor(self):
        for val in self.vals:
            self.dash.putNumber(val, self.vals[val])
        
        self.dash.updateValues()