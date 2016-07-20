from _stack import Stack
from collections import namedtuple

Pair = namedtuple('Pair', ['open', 'close'])

dict = {}
dict['('] = ')'
dict['{'] = '}'
dict['['] = ']'



def bracket_validation(string):
	stack = Stack()
	for ele in string:
		if ele in dict.keys():
			stack.push(ele)
		elif ele in dict.values():
			if not stack.is_empty():
				top = stack.top()
				if top == _get_key_from_value(ele):
					stack.pop()
				else:
					return False
			else:
				return False
	if not stack.is_empty():
		return False
	return True

def _get_key_from_value(string):
	for ele in dict:
		if dict[ele] == string:
			return ele
	return -1

better_dict = {}
better_dict[')'] = '('
better_dict['}'] = '{'
better_dict[']'] = '['


def bracket_validation_better_dict(string):
	stack = Stack()
	for ele in string:
		if ele in better_dict.values():
			stack.push(ele)
		elif ele in better_dict.keys():
			if not stack.is_empty():
				top = stack.top()
				if top == better_dict[ele]:
					stack.pop()
				else:
					return False
			else:
				return False
	if not stack.is_empty():
		return False
	return True




def print_format(input_string, output_string):
	print "------------------------"
	print "input: {0}".format(input_string)
	print "Calling bracket_validation:: output: {0} result:{1}".format(
		bracket_validation(input_string), 
		"Pass" if (bracket_validation(input_string)==output_string) else "Fail")
	print "Calling bracket_validation_better_dict:: output: {0} result:{1}".format(
		bracket_validation_better_dict(input_string), 
		"Pass" if (bracket_validation_better_dict(input_string)==output_string) else "Fail")
	print "------------------------"
	

if __name__ == "__main__":
	inputs = ["{[()]}", "{()[]}", "{[]", "()]"]
	ouputs = [True, True, False, False]
	for input,output in zip(inputs,ouputs):
		print_format(input, output)