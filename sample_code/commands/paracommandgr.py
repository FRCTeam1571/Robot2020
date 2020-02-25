from wpilib.command import CommandGroup
#from commands import SampCommand, TestCommand, InstaCommand
from commands.sampcommand import SampCommand
from commands.testcommand import TestCommand
from commands.instacommand import InstaCommand

class ParaCommandGr(CommandGroup) :
    def __init__(self):
        CommandGroup.__init__(self, "paraCommandGr")        
        self.setInterruptible(False)

        self.addParallel(SampCommand())
        self.addParallel(TestCommand())
        self.addParallel(InstaCommand())
        