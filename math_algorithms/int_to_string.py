def int_to_string(num):
	num_str = ''
	while num>0:
		num_str += str(num%10)
		#print num%10
		num = num/10
	return num_str[::-1]

if __name__ == "__main__":
	print int_to_string(123)

