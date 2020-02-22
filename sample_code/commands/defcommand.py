from wpilib.command import Command

class DefCommand(Command):
    def __init__(self):
        Command.__init__(self, "DefCommand")        
        self.requires(self.getRobot().sampSubsystem)
        
    # This method sets up the command and is called immediately before the command is executed for the first time and 
    # every subsequent time it is started . Any initialization code should be here.
    def initialize(self):
        print("Initialize DefCommand")

    # This method is called periodically (about every 20ms) and does the work of the command. Sometimes, if there is a position a subsystem 
    # is moving to, the command might set the target position for the subsystem in initialize() and have an empty execute() method.
    def execute(self):
        robot = self.getRobot()
        robot.sampSubsystem.forward()

    # Always returns false meaning this command never completes on it's own. 
    # This command will be set as the default command for the subsystem. 
    # Whenever the subsystem is not running another command, it will run this command. 
    # If any other command is scheduled it will interrupt this command, then return to this command when the other command completes.
    # Make this return true when this Command no longer needs to run execute()
    def isFinished(self) :
        return False 

    # Called once after isFinished returns true
    def end(self):
        robot = self.getRobot()
        robot.sampSubsystem.stop()

    # Called when another command which requires one or more of the same subsystems is scheduled to run
    def interrupted(self) :
        end()
        return True 