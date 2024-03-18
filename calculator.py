class Calculator:
	'''
	Calculates the sum of the given list of integers. See 'Input Format' in
	readme for full description.

	Design notes

	Goal was to keep the calculation logic very simple. To do this, the class
	validates & preprocesses the input str on init, turning it into a simple
	list internally.

	This works well for simplicity, but will likely be too slow if the input str
	scales too large. In that case, a design I would explore is to replace the
	preprocessing with as few loops over the data as possible, doing as much work
	as possible each iteration.
	'''

	def __init__(self, numListStr):
		self._validateCustomDelimiter(numListStr)
		self.numList = self._parseNumListStr(numListStr)
		self._validateNoNegativeNumbers()


	def _validateCustomDelimiter(self, numListStr):
		'''
		Validates that input optional custom delimiter is 1 character only,
		raises error if > 1.

		NOTE-1: Format is: //{delimiter}\n{numbers}
		'''
		if numListStr[0:2] == '//':
			if numListStr[2] != '\n' and numListStr[3] == '\n':
				pass
			else:
				raise Exception('Custom delimiter cannot be > 1 character')


	def _parseNumListStr(self, numListStr):
		'''
		Returns the input str as a list of ints.

		It replaces all valid delimiters with commas, then splits the str into
		a list & returns that.

		NOTE: Assumes a valid input str, call _validateCustomDelimiter() first!
		'''
		# Do this so we aren't editing the input arg
		newListStr = numListStr

		# Parse optional custom delimiter, see NOTE-1 above for format
		newDelim = ''
		if newListStr[0:2] == '//' and newListStr[3] == '\n':
			newDelim = newListStr[2]
			# Trim out custom delimiter syntax
			newListStr = newListStr[4:]

		# Replace newline & optional custom delims with commas
		newListStr = newListStr.replace('\n', ',')
		if newDelim != '':
			newListStr = newListStr.replace(newDelim, ',')

		# Split on commas
		return newListStr.split(',')


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
		Returns value of num as int. Returns 0 if num is > 1000 or it cannot be 
		casted to an int.
		'''
		try:
			val = int(num)
			if val > 1000:
				val = 0
		except Exception as e:
			val = 0
		return val


	def calculate(self):
		'''
		Loops over the number list, accumulates each one into a sum, & returns
		result.
		'''
		sum = 0
		for i,num in enumerate(self.numList):
			numVal = self._getNumVal(num)
			sum += numVal
		return sum
