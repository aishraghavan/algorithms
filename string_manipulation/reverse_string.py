"""
344 
https://leetcode.com/problems/reverse-string/
"""

def reverse_string(s):
	if not s or len(s)== 0:
		return s

	s = list(s)
	for i in range(len(s)/2):
		s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
	return ''.join(s)


def print_format(s):
	print "reverse_string({0}) : {1}".format(s, reverse_string(s))

if __name__ == "__main__":
	print_format("abcde")
	print_format("abcd")