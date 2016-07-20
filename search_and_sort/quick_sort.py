"""
quick_sort
"""
import random

def quick_sort(array):
	# yet to be implemented
	if len(array) == 0 :
		return -1

	random_index = random.randrange(len(array))	

	#swap
	array[i], array[j]= array[j], array[i]
	return array


def print_format(array):
	print "------------------------"
	print "input: {0}".format(array)
	print "bubble sort: {0}".format(quick_sort(array))
	print "------------------------"


if __name__ == "__main__":
	array = [1, 4, 45, 6, 10, 8]