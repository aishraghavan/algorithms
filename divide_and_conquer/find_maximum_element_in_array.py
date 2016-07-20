"""
Find the maximum element in an array which is first increasing and then decreasing
http://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/

Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
Output: 50

Corner case (No decreasing part)
Input: arr[] = {10, 20, 30, 40, 50}
Output: 50

Corner case (No increasing part)
Input: arr[] = {120, 100, 80, 20, 0}
Output: 120
"""
def find_maximum_element_in_array_linear_search(array):
	if not array or len(array) == 0:
		return -1
	for i in range(len(array)-1):
		j = i+1
		if array[j]<array[i]:
			return array[i]
	return array[i+1]
	
def find_maximum_element_in_array_binary_search(array, start, end):
	if not array or len(array) == 0:
		return -1

	# if length is 1
	if start == end:
		return array[start]

	# if length is 2:
	if start+1 == end:
		if array[start]> array[end]:
			return array[start]
		elif array[start]< array[end]:
			return array[end]
	
	# rest fot the array
	mid = (start+end)/2
	if (array[mid]> array[mid-1] and array[mid]> array[mid+1]):
		return array[mid]

	if (array[mid]< array[mid-1] and array[mid]> array[mid+1]):
		return find_maximum_element_in_array_binary_search(array, start, mid-1)
	else:
		return find_maximum_element_in_array_binary_search(array, mid+1, end)


def print_and_format(array):
	print "Input array: {0}".format(array)
	print "Calling find_maximum_element_in_array_linear_search: {0}".format(find_maximum_element_in_array_linear_search(array))
	print "Calling find_maximum_element_in_array_binary_search: {0}".format(find_maximum_element_in_array_binary_search(array, 0, len(array)-1))
	print "----------------"



if __name__ == "__main__":
	array1 = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]
	print_and_format(array1)
	array2 = [1, 3, 50, 10, 9, 7, 6]
	print_and_format(array2)
	array3 = [10, 20, 30, 40, 50]
	print_and_format(array3)
	array4 = [120, 100, 80, 20, 0]
	print_and_format(array4)