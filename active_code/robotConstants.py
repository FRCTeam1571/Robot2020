from enum import IntEnum, auto
import wpilib

class XboxMap (IntEnum) :
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
    KLEFT = wpilib.XboxController.Hand.kLeftHand
    KRIGHT = wpilib.XboxController.Hand.kRightHand

class DrivePort (IntEnum):
    KLEFTMOTOR1PORT = 0
    KLEFTMOTOR2PORT= 1
    KRIGHTMOTOR1PORT = 2
    KRIGHTMOTOR2PORT = 3


class SubSystemPort (IntEnum):
    KMOTORPORT = 4
    KNIDECPORT = 0

class AutoTimes (IntEnum):
    KAUTOTIMEOUTSECONDS = 12
    KAUTOMOVESECONDS = 10

class OIPorts (IntEnum):
    KDRIVERCONTROLLERPORT = auto()

