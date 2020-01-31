import wpilib 
from rev.color import ColorSensorV3

class Sensor(self):
    def __init__(self):
        # Object for the color sensor
        self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)

    # Function to print value of various properties of the color sensor
    def toDash(self):
        wpilib.SmartDashboard.putNumber("Proximity", proximity)
        wpilib.SmartDashboard.putNumber("IR", ir)
        wpilib.SmartDashboard.putNumber("Red", getRed())
        wpilib.SmartDashboard.putNumber("Green", getGreen())
        wpilib.SmartDashboard.putNumber("Blue", getBlue())
        

    def getProx(self):
        self.proximity = self.colorSensor.getProximity()
        return self.proximity

    def getIR(self):
        self.ir = self.colorSensor.getProximity()
        return self.ir

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