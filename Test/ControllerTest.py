from MotorControl import Controller

import unittest

class TestControllerClass(unittest.TestCase):
    
    def test_readControllerFromJson(self):
        file = File('../resources/controllerReadTest.json')
        
        
    def test_printControllerAsJson(self):
        myController = Controller()
        myJson = myController.printControllerAsJson()
#         assertFalse()
    
if __name__ == '__main__':
    unittest.main()