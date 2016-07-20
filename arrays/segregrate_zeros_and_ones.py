"""
http://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/
"""

def segregrate_zeros_and_ones_count_zeros(array):
	zero_count = 0
	for i in range(len(array)):
		if array[i] == 0:
			zero_count += 1

	for i in range(len(array)):
		if i<zero_count:
			array[i] = 0
		else:
			array[i] = 1
	return array


def segregrate_zeros_and_ones_two_indicies(array):
	if not array or len(array)==0:
		return -1
	left = 0
	right = len(array)-1
	while(left<right):
		while array[left]==0 and left<right:
			left += 1
		while array[right]==1 and left<right:
			right -= 1
		if (left<right):
			array[left] = 0
			array[right] = 1
			left +=1
			right -=1
	return array

def segregrate_zeros_and_ones_temp_arrays(array):
	temp_zeros = []
	temp_ones = []
	for i in range(len(array) 	):
		if array[i] == 0:
			temp_zeros.append(0)
		elif array[i] == 1:
			temp_ones.append(1)
	temp_zeros.extend(temp_ones)
	return temp_zeros


def format_and_print(array):
	print "Input arrary :"
	print array
	print "Calling segregrate_zeros_and_ones_two_indicies"
	print segregrate_zeros_and_ones_two_indicies(array)
	print "Calling segregrate_zeros_and_ones_count_zeros"
	print segregrate_zeros_and_ones_count_zeros(array)
	print "Calling segregrate_zeros_and_ones_temp_arrays"
	print segregrate_zeros_and_ones_temp_arrays(array)


if __name__ == "__main__":
	array1 = [0,1,0,1,0,0,1,1,1,0]
	format_and_print(array1)