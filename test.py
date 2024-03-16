import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):
	def testAddTwoPositive(self):
		c = Calculator('250,6')
		result = c.calculate()
		self.assertEqual(result, 256)

	def testAddTwoNegative(self):
		c = Calculator('-2,-1')
		result = c.calculate()
		self.assertEqual(result, -3)

	def testAddOnePositiveOneNegative(self):
		c = Calculator('4,-3')
		result = c.calculate()
		self.assertEqual(result, 1)

	def testErrorOnTooManyNumbers(self):
		with self.assertRaises(Exception):
			c = Calculator('1,2,3')
	
	def testIgnoreMissingNumber(self):
		c = Calculator('2')
		result = c.calculate()
		self.assertEqual(result, 2)

	def testIgnoreInvalidNumber(self):
		c = Calculator('2,abcd')
		result = c.calculate()
		self.assertEqual(result, 2)

	def testAllInvalidNumbers(self):
		c = Calculator('abc,xyz')
		result = c.calculate()
		self.assertEqual(result, 0)


if __name__ == '__main__':
	unittest.main()
