from pyfrc.tests import *
from subsystems import masterController

def Sample_Test():
    masterController.readController()
    assert True