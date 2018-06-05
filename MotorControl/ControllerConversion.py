import math, Motor, json
from Controller import Controller

class ControllerConversion:

	@staticmethod
	def convertFromControllerInputToMotors(controllerInput):
		lx = controllerInput.leftStickX
		ly = controllerInput.leftStickY

		lz = controllerInput.rightStickX #This is a rotation factor needed from the right stick, NOTE: needs to be scaled
		magnitude = math.sqrt(math.pow(lx, 2) + math.pow(ly,2))
		ratio = 0
		try:
			ratio = lx/magnitude
		except ZeroDivisionError:
			ratio = 0
		theta = math.acos(ratio)
		#arcSine = math.asin(ly/magnitude)
		piOverFour = math.pi/4.0
		
		#calculate the overall values where magnitude and lz are -1 to 1
		leftFrontValue = magnitude*math.sin(theta+piOverFour)+lz
		rightFrontValue = magnitude*math.cos(theta+piOverFour)-lz
		leftRearValue = magnitude*math.cos(theta+piOverFour)+lz
		rightRearValue = magnitude*math.sin(theta+piOverFour)-lz

		return {"leftFront":leftFrontValue, "rightFront":rightFrontValue, "leftRear":leftRearValue, "rightRear":rightRearValue}
		
	@staticmethod
	def printAsJson(object):
		return json.dumps(object.__dict__)

	@staticmethod
	def readControllerFromJson(jsonData):
		data = json.loads(jsonData)
		newController = Controller()
		newController.xButton = data["xButton"]		
		newController.yButton = data["yButton"]
		newController.aButton = data["aButton"]
		newController.bButton = data["bButton"]
		newController.lButton = data["lButton"]
		newController.rButton = data["rButton"]
		newController.l2Button = data["l2Button"]
		newController.r2Button = data["r2Button"]
		newController.l3Button = data["l3Button"]
		newController.r3Button = data["r3Button"]
		newController.startButton = data["startButton"]
		newController.selectButton = data["selectButton"]
		newController.leftStickX = data["leftStickX"]
		newController.leftStickY = data["leftStickY"]
		newController.rightStickX = data["rightStickX"]
		newController.rightStickY = data["rightStickY"]
		return newController