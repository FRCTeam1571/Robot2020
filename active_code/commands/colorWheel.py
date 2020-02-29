# import wpilib
# import ctre

# from wpilib.command import Command
# # from subsystems.MasterController import MasterController
# # from commands import mathRotate
# # from commands import readColor
# # from subsystems.ColorSpinner import ColorSpinner

# class ColorWheel(Command):
#     def __init__(self):
#         Command.__init__(self, "ColorWheel")

#         self.robot = self.getRobot()
#         self.oi = self.getOi()
#         # self.motor = ColorSpinner().motor
#         self.motor = ctre.WPI_TalonSRX(6)

#     def execute(self):
#         self.motor.engageMotor()

#     def isFinished(self):
#         return False
    
#     def end(self):
#         self.motor.engageMotor(0.0)