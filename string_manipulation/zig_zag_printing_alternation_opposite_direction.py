"""
zig_zag_printing_alternation_opposite_direction("GEEKSFORGEEKS", 3)
GFOKS
ESRE
EKGE

zig_zag_printing_alternation_opposite_direction("HAPPYBIRTHDAY", 4)
HRT
AIH
PBD
PYAY

"""

def zig_zag_printing_alternation_opposite_direction(string, size):
	direction = 1
	output = ['']*size
	row_index = -1
	for i in range(len(string)):
		row_index += direction
		
		if row_index == size:
			#ending row
			direction =  -1
			row_index -= 1
			
		elif row_index == -1:	
			# starting row
			direction =  1
			row_index += 1
			
		output[row_index] += string[i]
	return "".join(output)


if __name__ =="__main__":
	exepected_output ="GFOKSESREEKGE"
	output = zig_zag_printing_alternation_opposite_direction("GEEKSFORGEEKS", 3)
	print "exepected_output : {0}".format(exepected_output)
	print output , (output == exepected_output)

	input_string = "HAPPYBIRTHDAY"
	expected_string = "HRTAIHPBDPYAY"
	output = zig_zag_printing_alternation_opposite_direction(input_string, 4)
	print "expected_string : {0}".format(expected_string)
	print output , (output == expected_string)


