"""
http://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
"""

def segregrate_zeros_ones_twos_count(array):
	if not array or len(array) == 0:
		return -1
	zero_count = 0
	two_count = 0
	one_count = 0
	for i in range(len(array)):
		if array[i] == 0:
			zero_count += 1
		elif array[i] == 2:
			two_count += 1
		else:
			one_count += 1

	for i in range(zero_count):
		array[i] = 0
	for j in range(i+1,i+1+one_count):
		array[j] = 1
	for i in range(j+1, j+1+two_count):
		array[i] = 2
	return array

def segregrate_zeros_ones_twos_dutch(array):
	if not array or len(array) == 0:
		return -1

	low = 0
	mid = 0
	high = len(array)-1
	while(mid<=high):
		temp = array[mid]
		if temp == 0:
			array[low],array[mid] = array[mid], array[low]
			low += 1
			mid += 1
		elif temp == 1:
			mid += 1
		else:
			array[mid],array[high] = array[high], array[mid]
			high -= 1
	return array

def segregrate_zeros_ones_twos_temp_arrays(array):
	if not array or len(array) == 0:
		return -1
	temp_zeros = []
	temp_ones = []
	temp_twos = []
	for i in range(len(array)):
		if array[i] == 0:
			temp_zeros.append(0)
		elif array[i] == 1:
			temp_ones.append(1)
		else:
			temp_twos.append(2)
	temp_zeros.extend(temp_ones)
	temp_zeros.extend(temp_twos)
	return temp_zeros

def format_and_print(array):
	print "Input array :"
	print array
	print "Calling segregrate_zeros_ones_twos_count"
	print segregrate_zeros_ones_twos_count(array)
	print "Calling segregrate_zeros_ones_twos_dutch"
	print segregrate_zeros_ones_twos_dutch(array)
	print "Calling segregrate_zeros_ones_twos_temp_arrays"
	print segregrate_zeros_ones_twos_temp_arrays(array)
	

if __name__ == "__main__":
	#array1 = [0,1,0,1,0,0,1,1,1,0]
	array1 = [0,1,1,0,1,2,1,2,0,0,0,1]
	format_and_print(array1)