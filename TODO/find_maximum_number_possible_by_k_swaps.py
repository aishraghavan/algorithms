"""
http://www.geeksforgeeks.org/find-maximum-number-possible-by-doing-at-most-k-swaps/

Input: M = 254, K = 1
Output: 524

Input: M = 254, K = 2
Output: 542

Input: M = 68543, K = 1
Output: 86543

Input: M = 7599, K = 2
Output: 9975

Input: M = 76543, K = 1
Output: 76543

Input: M = 129814999, K = 4
Output: 999984211


"""
import copy

def find_maximum_number_possible_by_k_swaps(array,k, max_value):
	if(k == 0):
		return array

	array_len = len(array)
	for i in range(array_len-1):
		j = i+1
		while j<array_len and k>0:
			#swap only if curr<next
			if array[i]<array[j]:
				array[i], array[j] = array[j], array[i]

				#find if the current max value is greater than max_value, then replace.
				temp_max = int(''.join(array))
				if temp_max > max_value:
					max_value =  temp_max
				k=k-1
				find_maximum_number_possible_by_k_swaps(array,k, max_value)
			j += 1

def find_maximum_number_possible_by_k_swaps_iterative(array,k, max_value):
	#NOTE: There exits a bug. does not stop at the right k
	if(k == 0):
		return array

	flag = False
	array_len = len(array)
	while (k>0):
		for i in range(array_len-1):
			j = i+1
			while j<array_len:
				#swap only if curr<next
				if array[i]<array[j]:
					flag = True

					#when to stop

					array[i], array[j] = array[j], array[i]
					#find if the current max value is greater than max_value, then replace.
					temp_max = int(''.join(array))
					if temp_max > max_value:
						max_value =  temp_max
					k=k-1
					#print array, k


				j += 1
		if not flag and int(''.join(array)) == max_value:
			k=k-1

def format_and_print(number, k):
	array = list(str(number))
	print "input : ", array
	input1 = copy.deepcopy(array)
	input2 = copy.deepcopy(array)
	find_maximum_number_possible_by_k_swaps(input1, k, copy.deepcopy(number))
	find_maximum_number_possible_by_k_swaps_iterative(input2, k, copy.deepcopy(number))
	print "output find_maximum_number_possible_by_k_swaps: ", ''.join(input1)
	print "output find_maximum_number_possible_by_k_swaps_iterative: ", ''.join(input2)

if __name__ == "__main__":
	format_and_print(532, k=1) #input 254 output 542
	format_and_print(254, k=1) #input 254 output 542
	format_and_print(254, k=2) #input 254 output 542
	format_and_print(68543, k=1) #input 68543 output 86543
	format_and_print(7599, k=2) #input 7599, output: 9957
	format_and_print(7599, k=3) #input 7599, output: 9975
	format_and_print(76543, k=1) #input 76543, output: 76543
	format_and_print(129814999, k=4) #input 129814999, output 999984211
