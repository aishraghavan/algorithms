"""
http://www.geeksforgeeks.org/count-number-of-occurrences-in-a-sorted-array/
count_occurences_in_sorted_array
"""
# Not completely implemented
def count_occurences_in_sorted_array(array, element):
	if not array or len(array) == 0  or not element:
		return -1
	import ipdb;ipdb.set_trace()
	first = find_first(array, 0, len(array)-1, element)
	print "first: {0}".format(first)

	if first == -1:
		return -1
	last = find_first(array, first, len(array)-1, element)

	return last-first+1


def find_first(array, start, end, element):
	if (end>=start):
		mid = start + (end-start)/2
		#import ipdb;ipdb.set_trace()
		if (mid == 0 or element>= array[mid-1]) and array[mid] == element:
			return mid
		elif array[mid]< element:
			find_first(array, mid+1, end, element)
		else:
			find_first(array, start, mid-1, element)
	return -1

def find_last(array, start, end, element):
	if (end>=start):
		mid = start + (end-start)/2
		if (mid == len(array)-1 or element< array[mid-1]) and array[mid] == element:
			return mid
		elif element< array[mid]:
			find_last(array, start, mid-1, element)
		else:
			find_last(array, mid+1, end, element)
	return -1

def print_output(array, x):
	print "Given array : {0}".format(array)
	print "Calling count_occurences_in_sorted_array with x: {0} and output: {1}".format(x, count_occurences_in_sorted_array(array, x))

if __name__ == "__main__":
	array = [1,1,2,2,2,2,3]
	# elements = [2,3,1,4]
	# for element in elements:
	# 	print_output(array, element)
	print_output(array, 2)