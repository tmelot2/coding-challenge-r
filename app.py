# Challenge Calculator
#
# Usage: 
# 	$ python3 app.py 1,2
# 	3

import sys
import traceback

from calculator import Calculator

DEBUG=False


# Utility functions
#
def validateInputArgs(args):
	# Requires 2nd input arg, ignores additional items
	return (True if len(args) >= 2 else False)

def printUsage():
	print('\nExample usage: $ python3 challenge-calculator.py 1,2')
	print('See readme.md for full format description')


## Main
#
try:
	# Validate app input args
	if not validateInputArgs(sys.argv):
		raise Exception(f'Missing input arg for number list.')

	c = Calculator(sys.argv[1])
	result = c.calculate()
	print(result)
except Exception as e:
	if DEBUG: 
		traceback.print_exc()
	print(f'Error: {e}')
	printUsage()
