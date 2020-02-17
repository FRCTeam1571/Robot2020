from enum import Enum, auto
import wpilib

class XboxMap (Enum) :
    BUTTONA =  1
    BUTTONB = 2
    BUTTONX = 3
    BUTTONY = 4
    BUTTONLEFTBUMPER = 5
    BUTTONRIGHTBUMPER = 6
    BUTTONBACK = 7
    BUTTONSTART = 8
    BUTTONLEFTAXISPRESS = 9
    BUTTONRIGHTAXISPRESS = 10
    KLEFT = wpilib.Xboxcontroller.Hand.kLeftHand
    KRIGHT = wpilib.Xboxcontroller.Hand.kRightHand

class DrivePort (Enum):
    KLEFTMOTOR1PORT = 0
    KLEFTMOTOR2PORT= 1
    KRIGHTMOTOR1PORT = 2
    KRIGHTMOTOR2PORT = 3


class SubSystemPort (Enum):
    KMOTORPORT = 4
    KNIDECPORT = 0

class AutoTimes (Enum):
    KAUTOTIMEOUTSECONDS = 12
    KAUTOMOVESECONDS = 10

class OIPorts (Enum):
    KDRIVERCONTROLLERPORT = auto()

