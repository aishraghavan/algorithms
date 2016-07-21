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

if __name__ == "__main__":
	array = [1,-5,-1,3,23,-12]
	negative_followed_by_positive_numbers = [-5,-1,-12,1,3,23]
	print "Input"
	print array
	print "Calling segregrate_negative_followed_by_positive_numbers "
	print segregrate_negative_followed_by_positive_numbers(deepcopy(array))
	print "Calling segregrate_positive_followed_by_negative_numbers "
	print segregrate_positive_followed_by_negative_numbers(deepcopy(array))
