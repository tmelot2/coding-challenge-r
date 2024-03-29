import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def testAddTwoPositive(self):
        c = Calculator('250,6')
        result = c.calculate()
        self.assertEqual(result, 256)

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

    def testNewLineDelimiters(self):
        c = Calculator('1\n2\n3')
        result = c.calculate()
        self.assertEqual(result, 6)

    def testMixedDelimiters(self):
        c = Calculator('1\n2,3')
        result = c.calculate()
        self.assertEqual(result, 6)

    def testMixedEmptyDelimetersWithTrailingValue(self):
        c = Calculator(',,\n\n,\n1')
        result = c.calculate()
        self.assertEqual(result, 1)

    def testErrorOnNegative(self):
        message = ''
        with self.assertRaises(Exception) as e:
            c = Calculator('1,-1,2,-2,3,-3')
        self.assertEqual('Cannot use negative numbers, found these: -1,-2,-3', str(e.exception))

    def testIgnoreInvalidLargeNumbers(self):
        c = Calculator('1,2,1001')
        result = c.calculate()
        self.assertEqual(result, 3)

    def test1000NotIgnored(self):
        c = Calculator('1,2,1000')
        result = c.calculate()
        self.assertEqual(result, 1003)

    def testValidMixedNonsense(self):
        c = Calculator('a,b,,\n\n1,9999\n2\n\na')
        result = c.calculate()
        self.assertEqual(result, 3)

    def testCustomDelimiter(self):
        c = Calculator('//#\n2#5')
        result = c.calculate()
        self.assertEqual(result, 7)

        c = Calculator('//,\n2,ff,100')
        result = c.calculate()
        self.assertEqual(result, 102)

    def testErrorOnTooLongCustomDelimiter(self):
        with self.assertRaises(Exception):
            c = Calculator('//##\n2#5')

    def testErrorOnNegativeWithCustomDelimiter(self):
        message = ''
        with self.assertRaises(Exception) as e:
            c = Calculator('//_\n1_-1,2_-2\n,3_-3')
        self.assertEqual('Cannot use negative numbers, found these: -1,-2,-3', str(e.exception))

    def testMultiCharCustomDelimiter(self):
        c = Calculator('//[***]\n11***22***33')
        result = c.calculate()
        self.assertEqual(result, 66)

    def testErrorOnInvalidMultiCharCustomDelimiter(self):
        message = ''
        with self.assertRaises(Exception) as e:
            c = Calculator('//[###\n2###5')
        self.assertEqual('Invalid custom delimiter pattern, see readme for format', str(e.exception))

    def testEmptyWithMultiCharDelimiter(self):
        c = Calculator('//[###]\n\n\n')
        result = c.calculate()
        self.assertEqual(result, 0)

    def testMultiDelimiters(self):
        c = Calculator('//[*][!!][r9r]\n11r9r22*hh*33!!44')
        result = c.calculate()
        self.assertEqual(result, 110)

    def testEmptyWithMultiDelimiters(self):
        c = Calculator('//[###][___]\n\n\n')
        result = c.calculate()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
