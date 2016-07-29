"""
http://www.geeksforgeeks.org/check-if-array-elements-are-consecutive/

Examples:
a) If array is {5, 2, 3, 1, 4}, then the function should return true because the array has consecutive numbers from 1 to 5.

b) If array is {83, 78, 80, 81, 79, 82}, then the function should return true because the array has consecutive numbers from 78 to 83.

c) If the array is {34, 23, 52, 12, 3 }, then the function should return false because the elements are not consecutive.

d) If the array is {7, 6, 5, 5, 3, 4}, then the function should return false because 5 and 5 are not consecutive


Solution:
-----------
1. sorting - O(nlogn)
2. maintian an auxilary boolean array and mark it as visited.
3. maintian an auxilary array and mark it as negative.

For method 2 and 3, we need a way to find the max and min value in array to determine length.
"""
def check_if_array_elements_are_consecutive(array):
	min_value, max_value = find_max_value_and_min_value(array)
	length = max_value - min_value + 1

	#print "#step 1: check for length", length, len(array)
	#step 1: check for length
	if length == len(array):
		#step 2: create a boolean value 
		boolean_visited_array = [False]*length

		for i in range(len(array)):
			temp = array[i] - min_value
			# print temp, array[i],i, boolean_visited_array, boolean_visited_array[temp]
			# if temp is outside the range, break it.
			if boolean_visited_array[temp] == True:
				#break;
				return False
			else:
				boolean_visited_array[temp] = True
			#print temp, array[i],i, boolean_visited_array, boolean_visited_array[temp]
		# if all elements are True
		if i+1 == len(array):
			return True
	return False

def find_max_value_and_min_value(array):
	max_value = -100 #assuming to set it as MIN_INT
	min_value = 100 #assuming to set it as MAX_INT
	for i in range(len(array)):
		if array[i]>max_value:
			max_value = array[i]
		if array[i]<min_value:
			min_value = array[i]
	return min_value, max_value

def format_and_print(array):
	min_value, max_value = find_max_value_and_min_value(array)
	print "Array: {0}, min_value: {1} and max_value: {2}".format(array, min_value, max_value)
	print "Checking check_if_array_elements_are_consecutive: {0}".format(check_if_array_elements_are_consecutive(array))


if __name__ == "__main__":
	arrays = [[5, 2, 3, 1, 4],
			  [83, 78, 80, 81, 79, 82],
			  [34, 23, 52, 12, 3],
			  [7, 6, 5, 5, 3, 4]]
	for array in arrays:
		format_and_print(array)