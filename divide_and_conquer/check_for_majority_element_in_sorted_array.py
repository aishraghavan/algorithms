"""
http://www.geeksforgeeks.org/check-for-majority-element-in-a-sorted-array/
"""
def check_for_majority_element_linear_search(array, element):
	if not array or len(array) == 0 or not element:
		return -1
	n = len(array)
	for i in range(n/2):
		if array[i] == element and array[i+n/2] == element:
			return True
	return False

def check_for_majority_element_binary_search(array, element):
	if not array or len(array) == 0 or not element:
		return -1
	index = binary_search(array, 0, len(array)-1, element)
	if index == -1:
		return False
	n = len(array)
	if ((index+n/2)<=n-1) and (array[index+n/2]==element):
		return True
	return False

def binary_search(array, start, end, element):
	if end>=start:
		mid =(start+end)/2
		if ((mid ==0 or element> array[mid-1]) and (array[mid] == element)):
			return mid
		elif array[mid]< element:
			return binary_search(array, mid+1, end, element)
		else:
			return binary_search(array, start, mid-1, element)
	return -1

def format_and_print_output(array, element):
	print "Input array: {0} and Element: {1}".format(array, element)
	print "Calling check_for_majority_element_linear_search : {0}".format(check_for_majority_element_linear_search(array, element))
	print "Calling check_for_majority_element_binary_search : {0}".format(check_for_majority_element_binary_search(array, element))


if __name__ == "__main__":
	array1 = [1,2,3,3,3,3,10] 
	format_and_print_output(array1, 3)
	array2 = [1,1,2,4,4,4,6,6]
	format_and_print_output(array2, 4)
	array3 = [1,1,1,2,2]
	format_and_print_output(array3, 1)

