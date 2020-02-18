from wpilib.command import Command

# Three main ways commands are scheduled:
#   Manually, by calling the start() method on the command (used for autonomous)
#   Automatically by the scheduler based on button/trigger actions specified in the code 
#       (typically defined in the OI class but checked by the Scheduler).
#   Automatically when a previous command completes (default commands and command groups).
# The scheduler proceeds through the list of active commands and calls the execute() and isFinished() methods on each command, ~every 20 ms.
# Command - A basic command that operates on a subsystem
# Instant Command - A command that runs and completes instantly
# Timed Command

class SampCommand(Command):
    def __init__(self):
        Command.__init__(self, "SampCommand")        
        self.requires(self.getRobot().sampSubsystem)
        self.setInterruptible(True)
        self.runCount = 0

    # This method sets up the command and is called immediately before the command is executed for the first time and 
    # every subsequent time it is started . Any initialization code should be here.
    def initialize(self):
        print("Initialize sampCommand")
        self.runCount = 0


    # This method is called periodically (about every 20ms) and does the work of the command. Sometimes, if there is a position a subsystem 
    # is moving to, the command might set the target position for the subsystem in initialize() and have an empty execute() method.
    def execute(self):
        robot = self.getRobot()
        robot.sampSubsystem.forward()
        self.runCount += 1

    # The execute() method does some work and the isFinished() method that tells if it is done. 
    # Happens on every update from the driver station or about every 20ms
    # Make this return true when this Command no longer needs to run execute()
    def isFinished(self) :
        if (runCount > 10) : 
            return True 
        else :
            return False

    # Called once after isFinished returns true
    def end(self) :
        robot = self.getRobot()
        robot.sampSubsystem.stop()
        runCount = 0

    # Called when another command which requires one or more of the same subsystems is scheduled to run
    def interrupted(self) :
        end() 