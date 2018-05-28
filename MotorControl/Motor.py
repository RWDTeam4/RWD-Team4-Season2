class Motor:
	motorMax = 1
	motorMin = 0 
	motorValue = 0.0 #should be a value form -1 to 1
	reverseDirection = False

	def __init__(self, mValue, mMin, mMax):
		self.motorValue = mValue
		self.motorMin = mMin
		self.motorMax = mMax

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