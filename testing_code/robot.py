import wpilib


class Robot(wpilib.TimedRobot):
    ''' Statement of commands '''
    def robotInit(self):
        self.timer = wpilib.Timer() 

    def disabledInit(self):
        # add later
        print("Disabled Mode")

    def disabledPeriodic(self):
        # add later
        if self.timer.hasPeriodPassed(2) :
            print("Disabled Run")

    
    def teleopInit(self):
        if self.timer.get() == 0.0 :
            self.timer.start()
        elif self.timer.hasPeriodPassed(2) :
            print("Teleop Mode")
        elif self.timer.hasPeriodPassed(2.5) :
            self.timer.reset()
        

    def teleopPeriodic(self):
        # add later
        if self.timer.hasPeriodPassed(2) :
            print("Teleop method")
            

if __name__ == "__main__":
    wpilib.run(Robot)
    

