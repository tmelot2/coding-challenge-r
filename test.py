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

	def testOneNumber(self):
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

	def testManyNumbers(self):
		c = Calculator('1,2,3,4,5,6,7,8,9,10,11,12')
		result = c.calculate()
		self.assertEqual(result, 78)

	def testManyNumbersWithInvalids(self):
		c = Calculator('1,2,3,tttttttttttttt,4,5,zzzzzzzzzz')
		result = c.calculate()
		self.assertEqual(result, 15)

	def testNoNumbers(self):
		# NOTE: This shouldn't happen in the app, because the app validates
		# there is a non-blank input arg. But lets test sane behavior from
		# the class anyways.
		c = Calculator('')
		result = c.calculate()
		self.assertEqual(result, 0)


if __name__ == '__main__':
	unittest.main()
