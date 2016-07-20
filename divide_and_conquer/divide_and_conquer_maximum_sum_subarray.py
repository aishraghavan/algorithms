"""
http://www.geeksforgeeks.org/divide-and-conquer-maximum-sum-subarray/
"""
def divide_and_conquer_maximum_sum_subarray(array, low, high):
	if low == high:
		return array[low]

	mid = (low+high)/2
	return max(	divide_and_conquer_maximum_sum_subarray(array, low, mid),
				divide_and_conquer_maximum_sum_subarray(array, mid+1, high),
				divide_and_conquer_maximum_crossover_sum_subarray(array, low, mid, high))

def divide_and_conquer_maximum_crossover_sum_subarray(array, low, mid, high):
	# one small issue exists
	sum = 0 
	left_sum = -2048
	for i in range(high, mid-1, -1):
		sum = sum + array[i]
		if sum> left_sum:
			left_sum = sum
	sum = 0
	right_sum = -2048
	for i in range(mid+1, high):
		sum = sum + array[i]
		if sum> right_sum:
			right_sum = sum

	return left_sum + right_sum


"""
http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""
def largest_sum_contiguous_subarray(array):
	# Does not work for ngeative numbers array
	max_sum_so_far = 0
	max_sum_ending_here = 0
	for i in range(len(array)):
		max_sum_ending_here += array[i]
		if max_sum_ending_here <0:
			max_sum_ending_here = 0
		#if max_sum_ending_here> max_sum_so_far:
		# Make it efficient by adding the elif case.
		elif max_sum_ending_here> max_sum_so_far:
			max_sum_so_far = max_sum_ending_here
	return max_sum_so_far

def dynamic_programing_solution(array):
	# work for ngeative numbers array
	curr_max = array[0]
	max_so_far = array[0]
	for i in range(len(array)):
		curr_max = max(array[i], curr_max+array[i])
		max_so_far = max(curr_max, max_so_far)
	return max_so_far



def print_and_format(array):
	print "--------------"
	print "--------------"
	print "Input: {0}".format(array)
	print "Calling divide_and_conquer_maximum_sum_subarray"
	print "Maximum subsum: {0}".format(divide_and_conquer_maximum_sum_subarray(array, 0 , len(array)-1))
	print "--------------"
	print "Calling largest_sum_contiguous_subarray"
	print "Maximum subsum: {0}".format(largest_sum_contiguous_subarray(array))
	print "--------------"
	print "Calling dynamic_programing_solution"
	print "Maximum subsum: {0}".format(dynamic_programing_solution(array))
	print "--------------"

if __name__ == "__main__":
	array = [-2,-5,6,-2,-3,1,5,-6]
	print_and_format(array)
	array = [2, 3, 4, 5, 7]
	print_and_format(array)
	array = [-2, -3, -4, -5, -7]
	print_and_format(array)

