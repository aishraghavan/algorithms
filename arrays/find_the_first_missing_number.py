"""
http://www.geeksforgeeks.org/find-the-first-missing-number/

Given a sorted array of n integers where each integer is 
in the range from 0 to m-1 and m > n. Find the smallest number that is missing from the array.

n-> size of array
m-> range ending index

Input: {0, 1, 2, 6, 9}, n = 5, m = 10
Output: 3

Input: {4, 5, 10, 11}, n = 4, m = 12
Output: 0

Input: {0, 1, 2, 3}, n = 4, m = 5
Output: 4

Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11
Output: 8

Solution:
1. Linear search

"""

def find_the_first_missing_number_linear_search(array, m):
	length_of_array = len(array)
	ele = 0
	i = 0
	while ele < m and i<length_of_array:
		#print ele, i, array[i], m
		if ele != array[i]:
			return ele
		ele += 1
		i += 1
	# if array size is less than m
	if ele <m:
		return ele
	return None


def find_the_first_missing_number_binary_search_new(array, start, end):
	if start>end:
		end +1
	if start!=array[start]:
		return start

	mid = (start + end) / 2;
 
    if (array[mid] > mid):
    	return find_the_first_missing_number_binary_search_new(array, start, mid)
    else
    	return find_the_first_missing_number_binary_search_new(array, mid + 1, end)



def find_the_first_missing_number_binary_search(array, m):
	# Not working
	length_of_array = len(array)
	ele = 0
	while ele <m:
		#print "calling with array:{0}, start:{1}, end:{2}, search_item:{3}".format(array, 0, len(array)-1, ele)
		index = binary_search_helper(array, 0, len(array)-1, ele)
		if index == -1:
			return ele
		ele += 1
	return None


def binary_search_helper(array, start, end, search_item):
	# Not working
	#print "calling with array:{0}, start:{1}, end:{2}, search_item:{3}".format(array, start, end, search_item)
	if start<end:
		mid  = start +(end-start)/2
		#print "mid: ",mid
		if array[mid] == search_item:
			return mid
		if array[mid] > search_item:
			return binary_search_helper(array, start, mid, search_item)
		else:
			return binary_search_helper(array, mid+1, end, search_item)
	return -1


def format_and_print(array, m, expected_output):
	print "Input: {0} and m: {1} Expected output: {2}".format(array, m, expected_output)
	print "find_the_first_missing_number_linear_search(array, m): ", find_the_first_missing_number_linear_search(array, m)
	# Not working
	#print "find_the_first_missing_number_binary_search(array, m): ", find_the_first_missing_number_binary_search(array, m)
	print "find_the_first_missing_number_binary_search_new: ", find_the_first_missing_number_binary_search_new(array, m)
	

if __name__ == "__main__":
	format_and_print([0, 1, 2, 6, 9], m=10, expected_output=3)
	format_and_print([4, 5, 10, 11], m = 12, expected_output=0)
	format_and_print([0, 1, 2, 3], m=5, expected_output=4)
	format_and_print([0, 1, 2, 3, 4, 5, 6, 7, 10], m=11, expected_output=8)