import json

class Controller:
	xButton 		= False
	yButton 		= False
	aButton 		= False
	bButton 		= False
	lButton 		= False
	rButton 		= False
	l2Button 		= False
	r2Button 		= False
	l3Button 		= False
	r3Button 		= False
	startButton 	= False
	selectButton 	= False
	leftStickX 		= 0
	leftStickY 		= 0
	rightStickX 	= 0
	rightStickY 	= 0
	
	def __init__(self):
		self = self
		#Do Nothing
	
	@classmethod
	def printControllerAsJson():
		return json.dumps(self)

	@classmethod
	def readControllerFromJson(jsonData):
		data = json.load(jsonData)
		self.xButton = data["xButton"]		
		self.yButton = data["yButton"]
		self.aButton = data["aButton"]
		self.bButton = data["bButton"]
		self.lButton = data["lButton"]
		self.rButton = data["rButton"]
		self.l2Button = data["l2Button"]
		self.r2Button = data["r2Button"]
		self.l3Button = data["l3Button"]
		self.r3Button = data["r3Button"]
		self.startButton = data["startButton"]
		self.selectButton = data["selectButton"]
		self.leftStickX = data["leftStickX"]
		self.leftStickY = data["leftStickY"]
		self.rightStickX = data["rightStickX"]
		self.rightStickY = data["rightStickY"]