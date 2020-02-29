# import wpilib

# from wpilib.command import TimedCommand
# from wpilib.command import Command
# from subsystems.DriveTrain import DriveTrain

# class AutonomousCommand(Command):
#     def __init__(self):
#         # TimedCommand.__init__(self, "AutonomousCommand", 5.0)
#         Command.__init__(self, "AutonomousCommand")
#         self.timer = wpilib.Timer()
#         self.robot = self.getRobot()

#         # Class variables for systems pushed to the scheduler
#         self.drive_train = DriveTrain()

#         self.requires(self.drive_train)
#         self.setInterruptible(True)

#         self.timer.start()

#     def execute(self):
#         self.drive_train.engageDrive(.4, 0)
#         print('Auto hits execute')
    
#     def isFinished(self):
#         if self.timer.hasPeriodPassed(5):
#             print('Hit')
#             return True
#         else:
#             return False

#     def end(self):
#         self.drive_train.engageDrive(0, 0)