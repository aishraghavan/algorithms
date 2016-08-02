from copy import deepcopy

def segregrate_negative_followed_by_positive_numbers(array):
	#assuming no zeros given
	negative_index = 0
	for i in range(len(array)):
		if array[i] <0:
			array[negative_index], array[i] = array[i], array[negative_index]
			negative_index += 1
	return array

def segregrate_positive_followed_by_negative_numbers(array):
	#assuming no zeros given
	positive_index = 0
	for i in range(len(array)):
		if array[i] >0:
			array[positive_index], array[i] = array[i], array[positive_index]
			positive_index += 1
	return array

# if __name__ == "__main__":
# 	array = [1,-5,-1,3,23,-12]
# 	negative_followed_by_positive_numbers = [-5,-1,-12,1,3,23]
# 	print "Input"
# 	print array
# 	print "Calling segregrate_negative_followed_by_positive_numbers "
# 	print segregrate_negative_followed_by_positive_numbers(deepcopy(array))
# 	print "Calling segregrate_positive_followed_by_negative_numbers "
# 	print segregrate_positive_followed_by_negative_numbers(deepcopy(array))


def segregrate_negative_followed_by_positive_numbers(array):
	# fails in maintaining order
	#assuming no zeros given
	negative_index = 0
	for i in range(len(array)):
		array[negative_index], array[i] = array[i], array[negative_index]
		if array[i] <0:
			negative_index += 1
	return array


# def neel_sol(array):
# 	i = 0
# 	while i<len(array)-1:
# 		if array[i]> 0 and array[i+1]<0:
# 			array[i], array[i+1] = array[i+1], array[i]
# 		else:
# 			i+= 1
# 		while (i>0 and array[i]<0 and array[i-1]>0):
# 			array[i], array[i-1] = array[i-1], array[i]
# 			i -= 1
# 	return array


def neel_sol(array):
	i = 0
	curr_i = 0
	while i<len(array)-1:
		if array[i]> 0 and array[i+1]<0:
			array[i], array[i+1] = array[i+1], array[i]
			curr_i = i
		else:
			i+= 1
			curr_i = i
		while (i>0 and array[i]<0 and array[i-1]>0):
			array[i], array[i-1] = array[i-1], array[i]
			i -= 1
		i = curr_i
	return array

if __name__ == "__main__":
	 arrays = [[-1, 1, 2, 3, -2],
				[1,2,3, -1,-2,-3],
	 			[1,-1,2,-2,3,-3],
	 			[-1,1,2,3,-2],
    			[1,-5,-1,3,23,-12],
    			[1,2,3,4,5],
    			[-1,-2,-3,-4,-5],
			    [1,-1,2,-2,3,-3],
			    [-1,1,-2,2,-3,3],
			    [-1,-2,-3,1,2,3,-4,-5],
			    [1,2,3,-1,-2,4,5,-6,-7],
			    [8,4,-2,3,-5]]
	 for array in arrays:
		 print "input :"
		 print array
		 print neel_sol(array)