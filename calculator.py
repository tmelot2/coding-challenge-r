import re

class Calculator:
	'''
	Calculates the sum of the given list of integers. See 'Input Format' in
	readme for full description.

	Formats:
		- No custom delim:             {numbers}
		- Custom 1-character delim:    //{delim}\n{numbers}
		- Custom many-character delim: //[{delim}]\n{numbers}
		- Many custom delims: 		   //[{delim1}][{delim2}]\n{numbers}

	{numbers} is comma-separated list of ints. Newline & custom delimiters are
	also valid.

	Design Notes

	Goal was to keep the calculation logic very simple. To do this, the class
	validates & preprocesses the input str on init, turning it into a simple
	list internally.

	This works well for simplicity, but will likely be too slow if the input str
	scales too large. In that case, a design I would explore is to replace the
	preprocessing with as few loops over the data as possible, doing as much work
	as possible each iteration.
	'''
	CUSTOM_DELIM_PATTERN = r'^//(.*?)\n(.*?)'

	def __init__(self, numListStr):
		self.numList = self._parseNumListStr(numListStr)
		self._validateNoNegativeNumbers()


	def _validateCustomDelimiter(self, numListStr):
		'''
		Validates format for custom delimiters, raises error on invalid.
		'''
		if numListStr[0:2] == '//':
			match = re.findall(self.CUSTOM_DELIM_PATTERN, numListStr)
			customDelim = match[0][0] # 1st match in list, 1st item in tuple

			# Multi-delim & multi-character delim
			if customDelim[0] == '[' and customDelim[-1] == ']':
				# All good, nothing else to validate
				pass
			# 1-character delim
			elif customDelim[0] != '[' and customDelim[-1] != ']':
				if len(customDelim) > 1:
					raise Exception('The format used only supports 1-character delimiters. Wrap in [] for multi-character delimiters.')
			else:
				raise Exception('Invalid custom delimiter pattern, see readme for format')


	def _parseNumListStr(self, numListStr):
		'''
		Returns the input str as a list of ints.

		It replaces all valid delimiters with commas, then splits the str into
		a list & returns that.
		'''

		# Local copy so we aren't editing the input arg
		newListStr = str(numListStr)

		# Validate custom delimiter format
		self._validateCustomDelimiter(newListStr)

		# Parse & replace optional custom delimiters
		if newListStr[0:2] == '//':
			# Get delimiter section
			delimiterSection = re.findall(self.CUSTOM_DELIM_PATTERN, newListStr)
			delim = delimiterSection[0][0] # 1st match in list, 1st item in tuple

			# Replace single or multi delimiters
			multiDelimPattern = r'\[.*?\]+'
			multiDelims = re.findall(multiDelimPattern, delim)
			# Multi
			if len(multiDelims):
				for d in multiDelims:
					newListStr = newListStr.replace(d[1:-1], ',')
			# Single
			else:
				newListStr = newListStr.replace(delim, ',')

		# Replace newlines with commas
		newListStr = newListStr.replace('\n', ',')

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


	def calculate(self, displayFormula=False):
		'''
		Loops over the number list, accumulates each one into a sum, & returns
		result.
		'''
		result = 0
		vals = []
		for i,num in enumerate(self.numList):
			numVal = self._getNumVal(num)
			vals.append(str(numVal))
			result += numVal

		if displayFormula:
			formulaStr = '+'.join(vals)
			print(f'{formulaStr} = {result}')

		return result
