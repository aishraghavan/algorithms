"""
http://www.geeksforgeeks.org/print-all-interleavings-of-given-two-strings/
"""

Fbrackets
def print_all_interleavings_of_given_two_strings(result_string, string1, string2, len_string1, len_string2, res_index):

	if len_string1 == 0 and len_string2 == 0:
		print ''.join(result_string)

	if len_string1!= 0:
		result_string[res_index] = string1[0]
		print_all_interleavings_of_given_two_strings(result_string, string1[1:], string2, len_string1-1, len_string2, res_index+1)

	if len_string2!= 0:
		result_string[res_index] = string2[0]
		print_all_interleavings_of_given_two_strings(result_string, string1, string2[1:], len_string1, len_string2-1, res_index+1)


if __name__ == "__main__":
	string1 = "de"
	string2 = "p"
	len_string1 = len(string1)
	len_string2 = len(string2)
	result_string = ['']*(len_string1+len_string2)
	print_all_interleavings_of_given_two_strings(result_string, string1, string2, len_string1, len_string2, 0)