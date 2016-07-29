"""
http://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/
"""
string = [""]*20


string_list = [""]*20


def print_paranthesis_aish_iterative(size):
	position = 0
	open_count = 0
	close_count = 0
	done = False
	
	# how to generate the next values
	temp_str = ['']*100
	while close_count < size:
		if open_count> close_count:
			temp_str[position] = '}'
			close_count += 1
			position += 1
		if open_count<size:
			temp_str[position] = '{'
			open_count += 1
			position += 1
	if close_count == size:
		print "".join(temp_str)
	#reset counters
	open_count = 0
	close_count = 0
	position = 0
	


def print_paranthesis_aish(position ,size, open_count, close_count):
	if close_count == size:
		print "".join(string_list)
		#del string_list[:]
		#print string_list
		return
	else:
		if open_count>close_count:
			#start closing
			string_list[position] = '}'
			print_paranthesis_aish(position+1, size, open_count, close_count+1)
		if open_count<size:
			# can add more open brackets
			string_list[position] = '{'
			print_paranthesis_aish(position+1, size, open_count+1, close_count)


def print_paranthesis(position, size, open=0, close=0):
	
	print "Calling print_paranthesis(position={0}, size={1}, open={2}, close={3}), string={4}".format(position, size, open, close, string)
	
	if close == size:
		print ''.join(string)
		return
	else:
		if open>close:
			#open brackets are more than closing
			string[position] ='}'
			#already opened in above line. So close it.
			print_paranthesis(position+1, size, open, close+1)
		if open<size:
			#Has the capability to add more open brackets
			string[position] ='{'
			#already closed in above line. So open it.
			print_paranthesis(position+1, size, open+1, close)

if __name__ == "__main__":
	print_paranthesis(0, 3, 0, 0)
	#print_paranthesis_aish_iterative(3)
	#print_paranthesis_aish(0, 3, 0, 0)