class Calculator:
	'''
	Calculates the sum of the given list of integers. See readme for input format.
	'''
	def __init__(self, numListStr):
		self.numList = self._parseNumListStr(numListStr)
		self._validateNoNegativeNumbers()


	def _parseNumListStr(self, numListStr):
		# Replace newline chars with commas
		newStr = numListStr.replace('\n', ',')
		# Split on commas
		return newStr.split(',')


	def _validateNoNegativeNumbers(self):
		negatives = []
		for num in self.numList:
			val = self._getNumVal(num)
			if val < 0:
				negatives.append(num)
		if len(negatives):
			negListStr = ','.join(negatives)
			raise Exception(f'Cannot use negative numbers, found these: {negListStr}')


	def _getNumVal(self, num):
		'''
		Returns value of num as int, or 0 if num cannot be casted to an int.
		'''
		try:
			val = int(num)
		except Exception as e:
			val = 0
		return val


	def calculate(self):
		sum = 0
		for i,num in enumerate(self.numList):
			numVal = self._getNumVal(num)
			sum += numVal
		return sum
