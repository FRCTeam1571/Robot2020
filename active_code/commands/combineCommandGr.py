from wpilib.command import GroupCommand
from commands import sampCommand, testCommand

class combineCommandGr(GroupCommand) :
    def __init__(self):
        CommandGroup.__init__(self)        
        
        self.addSequential(sampCommand())
        self.addParallel(testCommand())
        self.addSequential(sampCommand())
        