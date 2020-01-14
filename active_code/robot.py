import wpilib
from wpilib.command import Command
from commandbased import CommandBasedRobot

class Robot(CommandBasedRobot):
    ''' Statement of commands '''

if __name__ == "__main__":
    wpilib.run(Robot)
    