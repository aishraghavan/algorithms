
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

def count_permutations(m,n):
	#print m, n
	if (m<=0 and n==1) or (n<=0 and m==1):
		return 1
	return count_permutations(m-1, n)+count_permutations(m, n-1)
	

def print_combination_one(string1, start, len):
	"""
	input:
	abcde

	abdce
	adbce
	dabce

	input: abcd
	['acbd', 'cabd']

	input:cdab
	['cadb', 'acdb']
	"""
	#string1 = "abcde"
	#start = 3
	list_strings =[]
	list_strings.append(''.join(string1))
	delta = 1
	while delta<len:
		while start>0:
			#string1[start], string1[start-1] = string1[start-1], string1[start]
			swap_values(string1, start, delta)
			list_strings.append(''.join(string1))
			start -= 1
		delta += 1
	return list_strings

def print_all_interleavings_of_given_two_strings(str1, str2):
	temp_str = str1 +str2
	index_str2 = len(str1)

	pass

def swap_values(string1, current_index, delta):
	string1[current_index], string1[current_index-delta] = string1[current_index-delta], string1[current_index]

print print_combination_one(['a', 'b', 'c', 'd', 'e'], 3, len=2)
print print_combination_one(['d', 'e', 'a', 'b', 'c'], 2, len=3)
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

""""
