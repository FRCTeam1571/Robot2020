import wpilib 
#from wpilib.command import Command
from wpilib.command import Subsystem
from rev.color import ColorSensorV3

class Sensor(Subsystem):
    def __init__(self):
        Subsystem.__init__(self) , "Sensor"
        # Object for the color sensor
        self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)

    # Function to print value of various properties of the color sensor
    '''def toDash(self):
        wpilib.SmartDashboard.putNumber("Proximity", proximity)
        wpilib.SmartDashboard.putNumber("IR", ir)
        wpilib.SmartDashboard.putNumber("Red", getRed())
        wpilib.SmartDashboard.putNumber("Green", getGreen())
        wpilib.SmartDashboard.putNumber("Blue", getBlue())'''
        
    def getProx(self):
        return self.colorSensor.getProximity()

    def getIR(self):
        return self.colorSensor.getProximity()

    def getBlue(self):
        return self.getSensorColor().blue

    def getGreen(self):
        return self.getSensorColor().green

    def getRed(self):
        return self.getSensorColor().red

    def getYellow(self):
        return self.getSensorColor().yellow   

    def getSensorColor(self):
        self.detectedColor = self.colorSensor.getColor
        return self.detectedColor