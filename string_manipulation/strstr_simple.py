# Haystack and needle problem - returns only first occurence
"""
strstr("hello there", "hello") returns 0
strstr("hello there", "llo") returns 2
strstr("hello there", "afafaf") returns -1

Proposals:
-----------
1. 	haystack and permutation of needles
2. 	split the haystick with the size of length_of_needle
	
   	The algorithms:
   	strstr("hello there", "llo") returns 2
   	"hel"
   	"ell"
   	"llo"
   	"lo "
   	"o t"
   	" th"
   	"the"
   	"her"
   	"ere"
"""

def strstr(haystack, needle):
	if haystack == None or needle == None:
		return None
	length_of_needle = len(needle)
	for i in range(len(haystack)-length_of_needle):
		temp = haystack[i:i+length_of_needle]
		if temp == needle:
			return i
	return -1


if __name__ == "__main__":
	print strstr("hello there", "hello") # 0
	print strstr("hello there", "llo")	# 2
	print strstr("hello there", "afafaf") # -1
