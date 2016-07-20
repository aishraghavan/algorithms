"""
http://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
max_and_min_in_array
"""
# from collections import NamedTuple

# Pair = NamedTuple('Pair', (min,max))
class Pair(object):
	def __init__(self, min_val=-1, max_val=-1):
		self.min_val = min_val
		self.max_val = max_val

def max_and_min_in_array_normal(array):
	if not array or len(array)==0:
		return Pair(-1, -1)

	if len(array) == 1:
		return Pair(array[0], array[0])

	minmax = Pair()
	if array[0]>array[1]:
		minmax.max_val = array[0]
		minmax.min_val = array[1]
	else:
		minmax.max_val = array[1]
		minmax.min_val = array[0]


	for i in range(2, len(array)):
		if array[i]>minmax.max_val:
			minmax.max_val = array[i]
		elif array[i]<minmax.min_val:
			minmax.min_val = array[i]
	return minmax


def max_and_min_in_array_tournament(array, start, end):
	# Divide array into two parts
	if not array or len(array)==0:
		return Pair(-1, -1)

	if start==end:
		return Pair(array[start], array[end])

	minmax = Pair()
	if start+1 == end:
		if array[start]>array[end]:
			minmax.max_val = array[start]
			minmax.min_val = array[end]
		else:
			minmax.max_val = array[end]
			minmax.min_val = array[start]
		return minmax

	#mid = start + (end-start)/2
	mid = (end+start)/2
	minmax_left = max_and_min_in_array_tournament(array, start, mid-1)
	minmax_right = max_and_min_in_array_tournament(array,mid+1, end)

	if minmax_left.min_val<minmax_right.min_val:
		minmax.min_val = minmax_left.min_val
	else:
		minmax.min_val = minmax_right.min_val

	if minmax_left.max_val > minmax_right.max_val:
		minmax.max_val = minmax_left.max_val
	else:
		minmax.max_val = minmax_right.max_val

	return minmax

def max_and_min_in_array_pair(array):
	if not array or len(array)==0:
		return Pair(-1, -1)
	if len(array) == 1:
		return Pair(array[0], array[0])

	minmax = Pair()
	if len(array)%2 == 0:
		if array[0]>array[1]:
			minmax.max_val = array[0]
			minmax.min_val = array[1]
		else:
			minmax.max_val = array[1]
			minmax.min_val = array[0]
	else:
		minmax.max_val = array[0]
		minmax.min_val = array[0]

	for i in range(2, len(array), 2):
		if array[i]>array[i+1]:
			if minmax.max_val < array[i]:
				minmax.max_val = array[i]
			if minmax.min_val > array[i+1]:
				minmax.min_val = array[i+1]
		else:
			if minmax.max_val < array[i+1]:
				minmax.max_val = array[i+1]
			if minmax.min_val > array[i]:
				minmax.min_val = array[i]
	return minmax

	
def print_and_format(array):
	print "----------------"
	print "----------------"
	print "Input array: {0}".format(array)
	print "----------------"
	print "Method 1: max_and_min_in_array_normal"
	minmax = max_and_min_in_array_normal(array)
	print "Min: {0} and Max: {1}".format(minmax.min_val, minmax.max_val)
	print "----------------"
	print "Method 2: max_and_min_in_array_tournament"
	minmax = max_and_min_in_array_tournament(array, 0, len(array)-1)
	print "Min: {0} and Max: {1}".format(minmax.min_val, minmax.max_val)
	print "----------------"
	print "Method 3: max_and_min_in_array_pair"
	minmax = max_and_min_in_array_pair(array)
	print "Min: {0} and Max: {1}".format(minmax.min_val, minmax.max_val)


if __name__ == "__main__":
	array = [1000, 11, 445, 1,300, 3000]
	print_and_format(array)
	array = [34]
	print "----------------"
	print "One element array"
	print_and_format(array)
	array = [34,12]
	print "----------------"
	print "Two elements array"
	print_and_format(array)
