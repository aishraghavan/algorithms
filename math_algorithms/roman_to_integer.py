"""
roman to integer
"""

def roman_to_number(str):
	if not str:
		return -1
	i = 0
	num = 0
	flag=True
	while i <len(str):
		j = i+1
		
		if j>= len(str):
			break
		#print "{0}: char : {1} j: {2}  char[j]: {3} num :{4}".format(i, str[i],j, str[j], num)
		#if get_number(str[i]) >= get_number(str[i+1]):
		if get_number(str[i]) >= get_number(str[j]):
			#print "if"
			num += get_number(str[i]) #+get_number(str[j])
		else:
			flag=False
			#print "else num : {0} get_number(str[i+1]) :{1} get_number(str[i]):{2}".format(num, get_number(str[i+1]), get_number(str[i]))
			#num += get_number(str[i+1]) - get_number(str[i])
			num += get_number(str[j]) - get_number(str[i])
			i = i+1
		i =i+ 1
	if flag:
		num += get_number(str[len(str)-1])
	return num	


def get_number(char):
	if char == 'I':
		return 1
	elif char == 'V':
		return 5
	elif char == 'X':
		return 10
	elif char == 'L':
		return 50
	elif char == 'C':
		return 100
	elif char == 'D':
		return 500
	elif char == 'M':
		return 1000
	else:
		return -1


if __name__ == "__main__":
	roman_strs=["XXIV", "XXVI", "LVIII", "MLIX"]
	for str1 in roman_strs:
		print "{0} : number = {1}".format(str1, roman_to_number(str1))
	
