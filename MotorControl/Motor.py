import json

class Motor:
	motorMax = 1
	motorMin = 0 
	motorValue = 0.0 #should be a value form -1 to 1
	reverseDirection = False

	def __init__(self):
		self.motorMax = 1
		self.motorMin = 0
		self.motorValue = 0.0 #should be a value form -1 to 1
		self.reverseDirection = False

	def __init__(self, mValue, mMin, mMax):
		self.motorValue = mValue
		self.motorMin = mMin
		self.motorMax = mMax
		self.reverseDirection = False

	def getMotorOutput():
		return motorValue*(motorMax - motorMin) + math.copysign(motorMin, motorValue)

	# def setMotorMax(value):
	# 	direction = getDirectionValue()
	# 	self.motorMax = direction*value

	# def setMotorMin(value):
	# 	direction = getDirectionValue()
	# 	self.motorMin = direction*value

	def setMotorValue(value):
		direction = getDirectionValue()
		self.motorValue = direction*value

	def getDirectionValue():
		if(self.reverseDirection):
			return -1
		else:
			return 1
		
	def printAsJsonm(self):
		return json.dumps(self)

	@staticmethod
	def readFromJson(jsonData):
		data = json.loads(jsonData)
		self.motorMax = data['motorMax']
		self.motorMin = data['motorMin']
		self.motorValue = data ['motorValue']
		self.reverseDirection = data['reverseDirection']

