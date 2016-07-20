"""
https://leetcode.com/articles/move-zeroes/
"""
from copy import deepcopy

def move_zeros_with_temp_array(array):
	if not array or len(array) == 0:
		return -1
	
	print "Input array :"
	print array
	temp_non_zeros = []
	for ele in array:
		if ele != 0:
			temp_non_zeros.append(ele)
	add_zeros = len(array) - len(temp_non_zeros)
	temp_non_zeros.extend([0]*add_zeros)
	return temp_non_zeros

def move_zeros_with_count_zeros(array):
	if not array or len(array) == 0:
		return -1

	print "Input array :"
	print array
	non_zero_index = 0
	for i in range(len(array)):
		if array[i] != 0:
			array[non_zero_index] = array[i]
			non_zero_index += 1
	
	for i in range(non_zero_index, len(array)):
		array[i] = 0
	return array

def move_zeros_optimized(array):
	if not array or len(array) == 0:
		return -1

	print "Input array :"
	print array
	non_zero_index= 0
	for curr in range(len(array)):
		if array[curr] != 0:
			array[non_zero_index],array[curr] = array[curr], array[non_zero_index]
			non_zero_index += 1
	return array


def format_and_print(array):
	print "Calling move_zeros_with_temp_array"
	print move_zeros_with_temp_array(deepcopy(array))
	print "Calling move_zeros_with_count_zeros"
	print move_zeros_with_count_zeros(deepcopy(array))
	print "Calling move_zeros_optimized"
	print move_zeros_optimized(deepcopy(array))


if __name__ == "__main__":
	# array1 = [0,1,0,1,0,0,1,1,1,0]
	# format_and_print(array1)
	array2 = [0, 1, 0, 3, 12]
	format_and_print(array2)