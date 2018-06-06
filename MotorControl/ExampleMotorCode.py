#This is an example file demonstrating the use of the controller code
#

from Controller import Controller
from ConvrollerConversion import ControllerConversion as CV

controllerA = Controller()

#Set Controller values as a state read for entire controller object
controllerA.xButton = True
controllerA.l2Button = True
controllerA.leftStickX = 127
controllerA.rightStickX = 40

jsonData = CV.printAsJson(ControllerA)

#Transfer this string over to the other Pi

controllerB = CV.readControllerFromJson(jsonData)

print CV.convertFromControllerInputToMotors(controllerB)