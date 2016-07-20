"""
https://leetcode.com/problems/happy-number/
19 is a happy number
"""
from sets import Set

class Solution(object):
	# def isHappyold(self, org_n):
	# 	if org_n == 0:
	# 		return False
	# 	if org_n == 1:
	# 		return True
	# 	n = org_n
	# 	past_array = Set()
	# 	while (1):
	# 		temp =  self.sum_of_squares(n)
	# 		#print temp
			
	# 		#import ipdb;ipdb.set_trace()
	# 		# if temp == 1:
	# 		# 	return True
			
	# 		if org_n == temp or temp in past_array:
	# 			return False
	# 		past_array.add(temp)
	# 		n = temp
	# 	return True

	def isHappy(self, org_n):
		if org_n == 0:
			return False
		if org_n == 1:
			return True
		n = org_n
		past_array = Set()
		while (n!=1):
			n = self.sum_of_squares(n)
			if n in past_array:
				return False
			past_array.add(n)
		return True

	def sum_of_squares(self, n):
		if n == 0:
			return 0
		sum = 0
		while (n>0):
			sum += pow(n%10, 2)
			n /= 10
		return sum

def print_output(input, output):
	sol = Solution()
	print "-----------"
	print "input :{0}".format(input)
	print "isHappy output: {0}".format(sol.isHappy(input))
	print "check output : {0}".format("Pass" if (sol.isHappy(input)==output) else "Fail")
	print "-----------"

if __name__ =="__main__":
	inputs = [19, 20, 0, 1, 1111111, 4, 2]
	outputs = [True, False, False, True, True, False, False]
	for input, output in zip(inputs,outputs):
		print_output(input, output)
	