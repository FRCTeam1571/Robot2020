# import wpilib
# import ctre

# from wpilib.command import Subsystem
# from networktables import NetworkTables
# from wpilib import SmartDashboard
# import robotConstants
# from robotConstants import XboxMap
# from wpilib.command import JoystickButton


# from commands.mathRotate import mathRotate
# # from commands.drive import Drive

# #from commands import mathRotate

# class MasterController(Subsystem):
#     def __init__(self):
#         Subsystem.__init__(self, "MasterController")

#         # self.controller.Button()
#         # self.xButton = wpilib.Button()
#         # wpilib.JoystickButton()

#         # Sides

     

#         #Color rotate buttons
#         self.mathSpinButton = False
#         self.colorSpinButton = False

#         #Buttons for command calling
#         self.mathCommandButton = JoystickButton(self.controller, XboxMap.BUTTONX)

#         #run math rotate when X is pressed
#         self.mathCommandButton.whenPressed(mathRotate())

#         #for Cole's future command
#         # self.colorSpinButton.WhenPressed(Colecommand())

    
#     def checkDrive(self):
#         if (self.trigRight > 0) or (self.trigLeft > 0):
#             self.drive = drive.execute()
#         elif (self.trigRight == 0) and (self.trigLeft == 0):
#             pass
#         else:
#             print('uh oh stinky')

#     def readSpeedMultiplier(self):
#         # Get speed up and down buttons to increase or decrease the speed for the drivetrain
#         self.SpeedUpButton = self.controller.getAButtonPressed()
#         self.SpeedDownButton = self.controller.getBButtonPressed()

#         if (self.SpeedDownButton == True and self.speedIndex > 0):
#             print("Up one")
#             self.speedIndex -= 1

#         elif (self.SpeedUpButton == True and self.speedIndex < len(self.speedArray)):
#             print("Down one")
#             self.speedIndex += 1

#             if (self.SpeedUpButton == True and self.speedIndex >= 5):
#                 self.speedIndex = 5

#         self.speedMultiplier = self.speedArray[self.speedIndex]

#         wpilib.SmartDashboard.putNumber("Speed Multiplier", self.speedMultiplier)

#     def readColorButtons(self):
#         #read the values of the x and y buttons
#         self.mathSpinButton = self.controller.getXButtonPressed()
#         self.colorSpinButton = self.controller.getYButtonPressed()

#         # if (self.mathSpinButton):
#         #     rotateCom = mathRotate()
#         #     rotateCom.execute()
#         # if (self.colorSpinButton):
#         #     rotateCom = colecommand()
#         #     rotateCom.execute()

#     def readController(self):
#         #Call this method to get status of controller
#         self.readSpeedMultiplier()
#         self.readStick()
#         self.readColorButtons()
#         self.checkDrive()

#     def getLeftStick_x(self):
#         print(self.leftstick_x)
#         return self.leftstick_x

#     def getTrigLeft(self):
#         print("Left Trigger", self.trigLeft)
#         return self.trigLeft

#     def getTrigRight(self):
#         print("Right Trigger", self.trigRight)
#         return self.trigRight
#     def getSpeed(self):
#         previous = self.speed
#         if (self.speed != previous):
#             pass
#         else:
#             print("Speed", self.speed)
#         return self.speed
 


#         #yw
#     def getSpeedMultiplier(self):
#         print(self.speedMultiplier)
#         return self.speedMultiplier

#     def getYButton(self):
#         print(self.colorSpinButton)
#         return self.colorSpinButton

#     def getXButton(self):
#         print(self.mathSpinButton)
#         return self.mathSpinButton
