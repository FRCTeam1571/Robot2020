from wpilib.command import InstantCommand

class InstaCommand(InstantCommand):
    def __init__(self):
        InstantCommand.__init__(self, "InstaCommand")        
        self.requires(self.getRobot().sampSubsystem)
        self.setInterruptible(False)

        
    # This method sets up the command and is called immediately before the command is executed for the first time and 
    # every subsequent time it is started . Any initialization code should be here.
    def initialize(self):
        print("Initialize instaCommand")

    # This method is called periodically (about every 20ms) and does the work of the command. Sometimes, if there is a position a subsystem 
    # is moving to, the command might set the target position for the subsystem in initialize() and have an empty execute() method.
    def execute(self):
        robot = self.getRobot()
        robot.sampSubsystem.forward()

    # Always returns True meaning this command completes after first execution. 
    #def isFinished(self) :
    #    return True 

    def end(self):
        robot = self.getRobot()
        robot.sampSubsystem.stop()

    # Called when another command which requires one or more of the same subsystems is scheduled to run
    # Make this return true when this Command no longer needs to run execute()
    def interrupted(self) :
        end()
