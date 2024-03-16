class Calculator:
	'''
	Calculates the sum of the given list of integers. See readme for input format.
	'''
	def __init__(self, numListStr):
		self.numList = self._parseNumListStr(numListStr)
		self._validateNumList()


	def _parseNumListStr(self, numListStr):
		# Replace newline chars with commas
		newStr = numListStr.replace('\n', ',')
		# Split on commas
		return newStr.split(',')


	def _validateNumList(self):
		# There was previously a validation for a max of 2 numbers. That's no
		# longer the case. Leaving this here because we'll probably need it in
		# the future. 
		pass


	def calculate(self):
		sum = 0
		for i,n in enumerate(self.numList):
			try:
				numVal = int(n)
			except Exception as e:
				numVal = 0

			sum += numVal
		return sum
