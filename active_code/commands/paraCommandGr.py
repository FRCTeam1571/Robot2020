from wpilib.command import GroupCommand
from commands import sampCommand, testCommand, instaCommand

class paraCommandGr(GroupCommand) :
    def __init__(self):
        CommandGroup.__init__(self)        
        
        self.addParallel(sampCommand())
        self.addParallel(testCommand())
        self.addParallel(instaCommand())
        