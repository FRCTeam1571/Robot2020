from wpilib.command import CommandGroup
from commands.sampcommand import SampCommand
from commands.testcommand import TestCommand

class CombineCommandGr(CommandGroup) :
    def __init__(self):
        CommandGroup.__init__(self, "CombineCommandGr") 
        self.setInterruptible(True)
               
        self.addSequential(SampCommand())
        self.addParallel(TestCommand())
        self.addSequential(SampCommand())
        