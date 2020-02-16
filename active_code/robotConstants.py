from enum import Enum, auto

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