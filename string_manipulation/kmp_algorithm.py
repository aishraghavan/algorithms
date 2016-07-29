"""
EXAMPLE
0000001

ABCABY
000120

ABCBCXA
0000001

ABCABCA
0001234

ABCDABCY
00001230

1.alawys first is 0
2. j ,i
3. when j != 0 look at a[j-1] and go to the location until you reach 
"""

def serach_by_kmp_multiple(string, pattern):
	output = []
	prefix_arr = prefix_array(pattern)
	i = 0
	j = 0
	while i < len(string) and j<len(pattern):
		if string[i] == pattern[j]:
			i+=1 
			j+=1
		else:
			# does not match
			if j == 0:
				i += 1
			else:
				j = prefix_arr[j-1]
		if j+1 == len(pattern) and i< len(string):
			output.append(i-j)
			j=0
	
	#wrong
	# if i == len(string) and j == len(pattern):
	#if j == len(pattern):
	if len(output) >0:
		return True, output
	return False, -1


def serach_by_kmp(string, pattern):
	prefix_arr = prefix_array(pattern)
	i = 0
	j = 0
	while i < len(string) and j<len(pattern):
		if string[i] == pattern[j]:
			i+=1 
			j+=1
		else:
			# does not match
			if j == 0:
				i += 1
			else:
				j = prefix_arr[j-1]
	
	#wrong
	# if i == len(string) and j == len(pattern):
	if j == len(pattern):
		return True, i -j
	return False, -1


def prefix_array(string):
	if not string:
		-1

	# step1: initialize array to 0
	prefix_array = [0]*len(string)
	#return prefix_array
	
	#initalize j=0 and i=1
	j = 0
	i = 1

	# run until i reaches the end
	while (i<len(string)):
		# if it is equal, prefix_array[i] should be j+1
		if string[i] == string[j]:
			prefix_array[i] = j+1
			j += 1
			i += 1
		else:
			# if j is 0, then prefix_array[i] is zero
			if j == 0:
				prefix_array[i] = 0
				i += 1
			else:
				#else: j becomes as prefix_array[j-1]
				j = prefix_array[j-1]
		
	return prefix_array


if __name__ == "__main__":
	# str1 = "ABCDABCY"
	# print prefix_array(str1)
	# str2 = "ABCABCA"
	# print prefix_array(str2)
	
	sub_string = "abcdabcy"
	# string1= "abcxabcdabcdabcy"
	
	# print "inputs str: {0} sub_string: {1}".format(string1, sub_string)
	# result, location = serach_by_kmp(string1, sub_string)
	# print "result: {0}, location: {1}".format(result, location)
	# string2 = "dfgdgjabcdabcyasdassd"
	# print "inputs str: {0} sub_string: {1}".format(string2, sub_string)
	# result, location = serach_by_kmp(string2, sub_string)
	# print "result: {0}, location: {1}".format(result, location)

	string2 = "abcdabcysddabcdabcy"
	print "inputs str: {0} sub_string: {1}".format(string2, sub_string)
	# result, location = serach_by_kmp(string2, sub_string)
	result, location = serach_by_kmp_multiple(string2, sub_string)
	print "result: {0}, location: {1}".format(result, location)



