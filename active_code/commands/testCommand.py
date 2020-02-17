from wpilib.command import timedCommand


class testCommand(timedCommand):
    def __init__(self):
        timeInSec = 5
        timedCommand.__init__(self, "testCommand", timeInSec)        
        self.requires(self.getRobot().testSubsystem)
        
    # This method sets up the command and is called immediately before the command is executed for the first time and 
    # every subsequent time it is started . Any initialization code should be here.
    # Called just before the Command runs 
    def initialize(self):
        print("Initialize testCommand")

    # This method is called periodically (about every 20ms) and does the work of the command. Sometimes, if there is a position a subsystem 
    # is moving to, the command might set the target position for the subsystem in initialize() and have an empty execute() method.
    # Called repeatedly when this Command is scheduled to run
    def execute(self):
        robot = self.getRobot()
        robot.testSubsystem.forward()

    # The execute() method does some work and the isFinished() method that tells if it is done. 
    # Happens on every update from the driver station or about every 20ms    
    # Make this return true when this Command no longer needs to run execute()
    def isFinished(self) :
        return True 

    # Called once after isFinished returns true
    def end(self):
        robot = self.getRobot()
        robot.testSubsystem.stop()

    # Called when another command which requires one or more of the same subsystems is scheduled to run
    def interrupted(self) :
        return True 