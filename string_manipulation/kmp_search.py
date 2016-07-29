"""
kmp_search
"""
from kmp_compute_prefix_array import compute_prefix_array_for_kmp

def kmp_search(string, pattern):
	if not string or not pattern:
		return

	lsp_array = compute_prefix_array_for_kmp(pattern)
	string_index = 0
	pattern_index = 0
	while string_index< len(string) and pattern_index < len(pattern):
		if string[string_index] != pattern[pattern_index]:
			string_index += 1
			pattern_index += 1
		else:
			if pattern_index == 0:
				string_index += 1
			else:
				pattern_index = lsp_array[pattern_index-1]
	if pattern_index == len(pattern):
		return True, string_index-pattern_index
	return False, -1



string = "abcdabcysddabcdabcy"
sub_string = "abcdabcy"
print "inputs str: {0} sub_string: {1}".format(string, sub_string)
result, location = kmp_search(string, sub_string)
# result, location = serach_by_kmp_multiple(string, sub_string)
print "result: {0}, location: {1}".format(string, location)