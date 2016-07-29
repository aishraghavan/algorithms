"""
Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1

"""
def find_minimum_element_in_a_sorted_and_rotated_array_simple(array):
	if not array:
		return -1
	min_element = array[0]
	for i in range(1, len(array)):
		if array[i] < min_element:
			min_element = array[i]
	return min_element


def find_minimum_element_in_a_sorted_and_rotated_array_neel(array):
	if not array:
		return -1
	
	for i in range(len(array)):
		# if to the start 1<2<3
		# fails in this case
		# if i == 0 and array[i]<array[i+1]:
		if i == 0 and array[i]<array[-1]:
			return array[i]
		#elif to the end 2<3<4>1
		elif i == len(array)-1 and array[i]<array[i-1]:
			return array[i]
		#other cases 4>1<2
		elif array[i-1]> array[i] and array[i]<array[i+1]:
			return array[i]
	# if all elements are same
	return array[0]

def find_minimum_element_in_a_sorted_and_rotated_array_binary_search(array, start, end):
	if not array:
		return -1
	#print start, end
	if start == end:
		return array[start]
	elif start<end:
		mid = start+(end-start)/2
		#print "mid: ", mid, "array: ",array[mid]
		# 1, 2, 3
		if mid == start and array[mid]<array[mid+1]:
			return array[mid]
		# 5, 6, 1
		elif mid == end and array[mid]<array[mid-1]:
			return array[mid]
		elif array[mid]<array[mid+1] and array[mid]<array[mid-1]:
			return array[mid]
		elif  array[mid]<array[mid+1]:
			return find_minimum_element_in_a_sorted_and_rotated_array_binary_search(array, start, mid -1)
		else:
			return find_minimum_element_in_a_sorted_and_rotated_array_binary_search(array, mid +1, end)
	return -1	


def format_and_print(array):
    # print "Calling find_minimum_element_in_a_sorted_and_rotated_array"
    # print find_minimum_element_in_a_sorted_and_rotated_array_simple(array)
    # print "Calling find_minimum_element_in_a_sorted_and_rotated_array_neel"
    # print find_minimum_element_in_a_sorted_and_rotated_array_neel(array)
    print "Calling find_minimum_element_in_a_sorted_and_rotated_array_binary_search {0}".format(array)
    print find_minimum_element_in_a_sorted_and_rotated_array_binary_search(array, 0, len(array)-1)


if __name__ == "__main__":
    array1 = [5, 6, 1, 2, 3, 4]
    format_and_print(array1)
    array2 = [1, 2, 3, 4]
    format_and_print(array2)
    array3 = [2, 1]
    format_and_print(array3)
    array4 = [2, 2, 2]
    format_and_print(array4)