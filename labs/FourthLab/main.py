import ctypes, os, argparse, random, time
from ctypes import *

def sort(values):
        pass
	# Converts the list of numbers to ctype array:
        arr = (ctypes.c_float * len(values))(*values)

	# Gets the library:
        dll = CDLL('bitonic.dll')
        
        start_time = time.time()
	# Call the library:
        dll.bitonic_sort(byref(arr),c_int(len(arr)))
        print("Битоническая сортировка (без преобразований): %s секунд" % (time.time() - start_time))
        
        return list(arr)

if __name__ == '__main__':
	# The preferences for the argument parser
	parser = argparse.ArgumentParser(description=
		'The simple program, that test two different sort algorithms')
	parser.add_argument('--power', dest='power',  type=int, help='the length = 2^power',  required=True)

	# Gets the arguments
	args = parser.parse_args()

	if args.power > 24:
                print("Сортировка может занять очень долгое время,нажмите Enter для продолжения...")
                input() 
		
	test = [random.uniform(0, 3) for x in range(2**args.power, 0, -1)]

	start_time = time.time()
	sort(test)
	print("Битоническая сортировка (с преобразованиями): %s секунд" % (time.time() - start_time))

	start_time = time.time()
	test.sort()
	print("Tim-Sort: %s секунд" % (time.time() - start_time))
