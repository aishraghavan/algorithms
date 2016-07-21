"""
http://www.geeksforgeeks.org/remove-duplicates-from-an-array-of-small-primes/
only remove_duplicates_from_array_of_small_primes

1. o(n^2)
2. hash map
3. sets
4. sort
5. prod of primes

"""

def remove_duplicates_from_array_of_small_primes(array):
	if not array:
		return None
	unique_array = []
	unique_array.append(array[0])
	prod = array[0]
	for i in range(1, len(array)):
		#import ipdb;ipdb.set_trace()
		if prod%array[i] != 0:
			unique_array.append(array[i])
			prod *= array[i]
	return unique_array

def format_and_print(array):
	print "Input array :"
	print array
	print "Calling remove_duplicates_from_array_of_small_primes"
	print remove_duplicates_from_array_of_small_primes(array)
	print "---------------------"


if __name__ == "__main__":
	array1 = [3,5,7,2,2,5,7,7]
	array2 = [3,5,7,3,3,13,5,13,29,13]
	format_and_print(array1)
	format_and_print(array2)
