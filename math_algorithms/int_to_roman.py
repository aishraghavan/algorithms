"""
int to roman

1 - 3999
"""

def int_to_roman(str1):
	if not str1:
		return -1
	num = int(str1)
	count = 0
	reminder = 0
	reconstruct = 0
	while num>0:
		#print "reminder: {0}, num: {1}, count: {2}".format(reminder, num, count)
		reminder = num%10
		num = num/10
		temp = reminder*(pow(10, count))
		reconstruct += temp
		print "reconstruction: {0} roman: {1}".format(temp, get_roman(str(temp)))
		count +=1
	print "final reminder :	{0}".format(reminder)
	print "reconstructed num : {0}".format(reconstruct)
		

def get_int_to_roman(str1):
	if not str1:
		return -1
	num = int(str1)
	output = ""
	while (num>0):
		if num/1000>0:
			output+= ("M" *int(num/1000)) 
			num = num%1000
		if num/500>0:
		 	output+= ("D" *int(num/500)) if int(num/500)<4 else ("C" *int(num/500)+"M")
			num = num%500
		if num/100>0:
			output+= ("C" *int(num/100)) if int(num/100)<4 else ("C" *int(num/100)+"D")
			num = num%100
		if num/50>0:
			output+= ("L" *int(num/50)) if int(num/50)<4 else ("X" *int(num/50)+"C")
			num = num%50
		if num/10>0:
			temp = int(num/10)
			print " temp: {0}, % :{1}, val:{2}".format(temp,  num%10,  num%10<4)
			output+= ("X" *temp) if num%10<4 else (("I"*temp)+"V")
			#num = num%10
			num = num%10 if num%10<4 else 0
		if num/5>0:
			temp = int(num/5)
			output+= ("V" *temp) if num%5<4 else ("I" *temp+"X")
			num = num%5 if num%5<4 else 0
		if num>0:
			output+= ("I" *num) if num<4 else ("IV")
	return output


# def get_int_to_roman(str1):
# 	if not str1:
# 		return -1
# 	num = int(str1)
# 	output = ""
# 	if num/1000>0:
# 		output+= ("M" *int(num/1000)) 
# 		num = num%1000
# 	if num/500>0:
# 	 	output+= ("D" *int(num/500)) if int(num/500)<4 else ("C" *int(num/500)+"M")
# 		num = num%500
# 	if num/100>0:
# 		output+= ("C" *int(num/100)) if int(num/100)<4 else ("C" *int(num/100)+"D")
# 		num = num%100
# 	if num/50>0:
# 		output+= ("L" *int(num/50)) if int(num/50)<4 else ("X" *int(num/50)+"C")
# 		num = num%50
# 	if num/10>0:
# 		#temp = int(num/10)
# 		#print " temp: {0}, % :{1}, val:{2}".format(temp,  num%10,  num%10<4)
# 		output+= ("X" *temp) if num%10<4 else ("I" *temp+"V")
# 		#num = num%10
# 		num = num%10 if num%10<4 else 0
# 	if num/5>0:
# 		temp = int(num/5)
# 		output+= ("V" *temp) if num%5<4 else ("I" *temp+"X")
# 		num = num%5 if num%5<4 else 0
# 	if num>0:
# 		output+= ("I" *num) if num<4 else ("IV")
# 	return output

if __name__ == "__main__":
	# int_strs=["123", "1005", "567", "978", "4", "8", "9"]
	# for str1 in int_strs:
	# 	print "num {0} : roman : {1}".format(str1, get_int_to_roman(str1))
	# print "num {0} : roman : {1}".format("9", get_int_to_roman("9"))
	# print "num {0} : roman : {1}".format("8", get_int_to_roman("8"))
	# print "num {0} : roman : {1}".format("4", get_int_to_roman("4"))
	for i in range(15,50):
		print "num {0} : roman : {1}".format(str(i), get_int_to_roman(str(i)))

