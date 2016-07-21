"""
zig_zag_printing_alternation_one_direction("GEEKSFORGEEKS", 3)
GKOES
ESRE
EFGK

zig_zag_printing_alternation_one_direction("HAPPYBIRTHDAY", 4)
HYTY
ABH
PID
PRA

"""

def zig_zag_printing_alternation_one_direction(string, size):
	org_index = 0
	index = 0
	output  = ""

	while index < len(string):
		#print string[index]
		output += string[index]
		index = index+ size
		if index >= len(string):
			#reset
			org_index +=1
			if org_index <size:
				index = org_index

	return output


exepected_output ="GKOESESREEFGK"
output = zig_zag_printing_alternation_one_direction("GEEKSFORGEEKS", 3)
print "exepected_output : {0}".format(exepected_output)
print output , (output == exepected_output)

input_string = "HAPPYBIRTHDAY"
expected_string = "HYTYABHPIDPRA"
output = zig_zag_printing_alternation_one_direction(input_string, 4)
print "expected_string : {0}".format(expected_string)
print output , (output == expected_string)


