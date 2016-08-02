
"""
http://www.geeksforgeeks.org/print-all-interleavings-of-given-two-strings/\

str1 length = m
str2 length = n

count
base cases: 
count(m,0) = 1
count(0,m) = 1
return count(m-1, n)+count(m,n-1)

str1="ab" str2="cd"

abcd
acbd
cabd

acdb
cabd

cdab

Looks similar to bracket problem
"""

def print_valid_permutations(result, string1, string2, len_string1, len_string2, index_res):
	print "calling print_valid_permutations with", result, string1, string2, len_string1, len_string2, index_res
	if len_string1 == 0 and len_string2 == 0:
		print "".join(result)

	if len_string1 != 0:
		result[index_res] = string1[0]
		print_valid_permutations(result, string1[1:], string2, len_string1-1, len_string2, index_res+1)

	if len_string2 != 0:
		result[index_res] = string2[0]
		print_valid_permutations(result, string1, string2[1:], len_string1, len_string2-1, index_res+1)



if __name__ == "__main__":
	string1 = "p"#"abc"
	len_string1 = len(string1)
	string2 = "de"
	len_string2 = len(string2)
	result = [""]*(len_string1+len_string2)
	print_valid_permutations(result, string1, string2, len_string1, len_string2, 0)

# print print_combination_one(['a', 'b', 'c', 'd', 'e'], 3, len=2)
# print print_combination_one(['d', 'e', 'a', 'b', 'c'], 2, len=3)
# print print_combination_one(['a','b','c','d'], 2)
# print print_combination_one(['c','d','a','b'], 2)
"""

abcde y
abdce y
adbce y
dabce y

abdec 
adebc y
deabc y

daebc y
dabec
adbec

"""
