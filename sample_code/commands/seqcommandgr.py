from wpilib.command import CommandGroup
from commands.sampcommand import SampCommand
from commands.testcommand import TestCommand


class SeqCommandGr(CommandGroup):
    def __init__(self):
        CommandGroup.__init__(self, "SeqCommandGr")        
        self.setInterruptible(True)

        self.addSequential(SampCommand())
        self.addSequential(TestCommand())
        self.addSequential(SampCommand())
        