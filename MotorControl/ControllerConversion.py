import math, Motor.py, Controller

class ControllerConversion:

	def convertFromControllerInputToMotors(controllerInput):
		lx = controllerInput.leftStickX
		ly = controllerInput.leftStickY

		lz = controllerInput.rightStickX #This is a rotation factor needed from the right stick, NOTE: needs to be scaled
		magnitude = math.sqrt(math.pow(lx, 2) + math.pow(ly,2))
		theta = math.acos(lx/magnitude)
		#arcSine = math.asin(ly/magnitude)
		piOverFour = math.pi/4.0
		
		#calculate the overall values where magnitude and lz are -1 to 1
		leftFrontValue = magnitude*sin(theta+piOverFour)+lz
		rightFrontValue = magnitude*cos(theta+piOverFour)-lz
		leftRearValue = magnitude*cos(theta+piOverFour)+lz
		rightRearValue = magnitude*sin(theta+piOverFour)-lz

		return {"leftFront":leftFrontValue, "rightFront":rightFrontValue, "leftRear":leftRearValue, "rightRear":rightRearValue}
		