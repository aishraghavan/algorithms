"""
http://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/
"""

def pair_of_given_sum_sorted(array, sum):
	if not sum or len(array)<=1:
		return False
	l = 0 
	r = len(array)- 1
	while (l<r):
		if array[l] + array[r] == sum:
			return True
		elif array[l] + array[r] < sum:
			l += 1
		else:
			r -= 1
	return False

SIZE = 100

def pair_of_given_sum_hashmap(array, sum):
	binary_map = [0]*SIZE
	if not sum or len(array)<=1:
		return False
	for i in range(len(array)):
		temp = sum - array[i]
		if temp >=0 and binary_map[temp] == 1:
			return True
		binary_map[array[i]] = 1
	return False

def pair_unsorted(array, sum):
	for i in range(len(array)-1):
		j = i+1
		temp = sum - array[i]
		while j<=len(array)-1:
			if temp == array[j]:
				return True
			j += 1
	return False

if __name__ == "__main__":
	array = [8, 10, 12, 15, 16, 20, 25] 
	sum1 = 35
	sum2= 10
	print "-------------------------"
	print "calling pair_of_given_sum_sorted({0}, {1}) : {2}".format(array, sum1, pair_of_given_sum_sorted(array, sum1))
	print "calling pair_of_given_sum_sorted({0}, {1}) : {2}".format(array, sum2, pair_of_given_sum_sorted(array, sum2))
	print "calling pair_of_given_sum_sorted({0}, {1}) : {2}".format(array, 28, pair_of_given_sum_sorted(array, 28))

	array2 = [-8, 1, 4,6, 10, 45]
	print "-------------------------"
	print "calling pair_of_given_sum_sorted({0}, {1}) : {2}".format(array2, 28, pair_of_given_sum_sorted(array2, 28))
	print "calling pair_of_given_sum_sorted({0}, {1}) : {2}".format(array2, 8, pair_of_given_sum_sorted(array2, 8))
	print "calling pair_of_given_sum_sorted({0}, {1}) : {2}".format(array2, 2, pair_of_given_sum_sorted(array2, 2))

	print "-------------------------"
	print "Testing pair_of_given_sum_hashmap"
	array  = [1,4,45,6,10,-8]
	print "calling pair_of_given_sum_hashmap({0}, {1}) : {2}".format(array, 28, pair_of_given_sum_hashmap(array, 28))
	print "calling pair_of_given_sum_hashmap({0}, {1}) : {2}".format(array, 16, pair_of_given_sum_hashmap(array, 16))
	
	print "-------------------------"
	print "Testing pair_unsorted"
	print "calling pair_unsorted({0}, {1}) : {2}".format(array, 16, pair_unsorted(array, 16))
	print "calling pair_unsorted({0}, {1}) : {2}".format(array, 28, pair_unsorted(array, 28))

