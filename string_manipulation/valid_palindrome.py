"""
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

"""

def valid_palindrome(string):
	if not string :
		return True
	filtered_string = step_1_filter_input(string)
	for i in range(len(filtered_string)/2):
		if filtered_string[i] != filtered_string[len(filtered_string)-1-i]:
			return False
	return True

	#return check_palindrome(filtered_string)

def check_palindrome(string1):
    if string1 == string1[::-1]:
        return True
    return False


def step_1_filter_input(string):
	filtered_string = ""
	for s in string.lower():
		if s.isalpha() or s.isdigit():
			filtered_string += s
	return filtered_string

def another_way_to_check_palindrome(string):
	if not string :
		return True
	string = string.lower()
	start_index = 0
	end_index = len(string)-1

	while (start_index< len(string) and end_index>0):
		while not string[start_index].isalnum():
			start_index += 1
		while not string[end_index].isalnum():
			end_index -= 1
		if string[start_index] != string[end_index]:
			return False
		start_index += 1
		end_index -= 1
	return True



class Solution(object):
    def isPalindrome(self, string):
	   if not string:
	       return True

	   filtered_string = self.step_1_filter_input(string)
	   if (filtered_string == filtered_string[::-1]):
	       return True
	   return False

    def step_1_filter_input(self, string):
	   filtered_string = ""
	   for s in string.lower():
	       if s.isalpha() or s.isdigit():
	           filtered_string += s
	   return filtered_string



def print_output(input_string, output_string):
	sol = Solution()
	print "-----------"
	print "input :{0}".format(input_string)
	print "valid_palindrome output: {0}".format(valid_palindrome(input_string))
	print "filtered_string: {0}".format(step_1_filter_input(input_string))
	print "From leetcode: {0}".format(sol.isPalindrome(input_string))
	print "check output 1: {0}".format("Pass" if (valid_palindrome(input_string)==output_string) else "Fail")
	print "check output 2: {0}".format("Pass" if (another_way_to_check_palindrome(input_string)==output_string) else "Fail")
	print "-----------"


if __name__ == "__main__":
	inputs = ["A man, a plan, a canal: Panama",
			  "race a car",
			  "",
			  "0P",
			  "a."]
	outputs = [True, False, True, False, True]
	for input, output in zip(inputs,outputs):
		print_output(input, output)
