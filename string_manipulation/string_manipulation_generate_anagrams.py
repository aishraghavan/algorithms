"""
string_manipulation_generate_anagrams

http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
"""


permutation_array = []
def permutations_of_string_recursive(string_array, k , n):
	if k == n:
		#temp_str = ''.join(string_array)
		permutation_array.append(''.join(string_array))
		#print permutation_array#string_array
	else:
		for i in range(k,n):
			string_array[k], string_array[i] = string_array[i], string_array[k]
			permutations_of_string_recursive(string_array, k+1, n)
			string_array[k], string_array[i] = string_array[i], string_array[k]
	return permutation_array

if __name__ == "__main__":
	permutation_array = permutations_of_string_recursive(list("abcd"), 0, 4)
	print permutation_array