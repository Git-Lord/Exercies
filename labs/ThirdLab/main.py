import ctypes, os, argparse, syslog
from ctypes import *


def calculate(numbers):
	# Converts the list of numbers to ctype array:
	arr = (ctypes.c_int * len(numbers))(*numbers)

	# Gets the library:
	dll = CDLL('lib.so')

	# Call the library:
	return dll.calculateMinimum(c_int(len(arr)),byref(arr))
	

if __name__ == '__main__':
	# The prefernces for the argument parser
	parser = argparse.ArgumentParser(description=
		'The simple program, that calculates the sum of integers that has the minimum absolute value')

	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('--numbers', metavar='n', type=int, nargs='+', help='set of integers')
	group.add_argument('--file', metavar='f', help='path to file with numbers')
	parser.add_argument('--debug', dest='debug', action='store_true', help='enable the log to syslog')

	# Gets the arguments
	args = parser.parse_args()
	print(args)

	try:
		# Load the numbers from file:
		if (args.file is not None):
			f = open(args.file)
			numbers = list(map(int,f.read().split()))
		# Get the inputted numbers
		else:
			numbers = args.numbers
		# Calculates the sum
		s = calculate(numbers)
		print('Минимальная по модулю сумма элементов: {0}'.format(s))
	except Exception as e:
		if args.debug == True:
			syslog.syslog(str(e))
		print('Произошла ошибка: выполнение программы остановлено')