from wpilib.command import CommandGroup
from commands import sampCommand, testCommand


class seqCommandGr(CommandGroup):
    def __init__(self):
        CommandGroup.__init__(self)        
        
        self.addSequential(sampCommand())
        self.addSequential(testCommand())
        self.addSequential(sampCommand())
        