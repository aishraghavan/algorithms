# Haystack and needle problem - returns only first occurence
"""
strstrp("hello there", "hello") returns 0
strstrp("hello there", "elloh") returns 0
strstrp("hello there", "llohe") returns 0
strstrp("hello there", "llo") returns 2
strstrp("hello there", "afafaf") returns -1



Proposals:
-----------
1. haystack and permutation of needles - not efficient
2. haystack and recursion - not efficient

"""

def strstrp(haystack, needle):
	if haystack == None or needle == None:
		return None
	length_of_needle = len(needle)
	sorted_needle = sorted(needle)
	for i in range(len(haystack)-length_of_needle):
		temp = haystack[i:i+length_of_needle]
		sorted_temp = sorted(temp)
		if sorted_temp == sorted_needle:
			return i
	return -1


if __name__ == "__main__":
	print strstrp("hello there", "hello") #returns 0
	print strstrp("hello there", "elloh") #returns 0
	print strstrp("hello there", "llohe") #returns 0
	print strstrp("hello there", "llo") #returns 2
	print strstrp("hello there", "afafaf") #returns -1

