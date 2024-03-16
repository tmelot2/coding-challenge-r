class Calculator:
	'''
	Calculates the sum of the given list of integers. See readme for input format.
	'''
	def __init__(self, numListStr):
		self.numList = numListStr.split(',')
		self._validateNumList()


	def _validateNumList(self):
		if len(self.numList) > 2:
			raise Exception('Too many numbers in list (max of 2).')


	def calculate(self):
		sum = 0
		for i,n in enumerate(self.numList):
			try:
				numVal = int(n)
			except Exception as e:
				numVal = 0

			sum += numVal
		return sum
