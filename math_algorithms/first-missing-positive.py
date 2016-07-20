"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

def first_missing_positive_native(list):
	if not list:
		return 
	sorted_list = sorted(list)
	print sorted_list
	postive_index = 0
	for index in range(len(sorted_list)):
	#for ele in sorted_list:
		if sorted_list[index]>0:
			postive_index = index
			break
		index += 1
	prev = sorted_list[postive_index]
	print "postive_index : {0} prev : {1}".format(postive_index, prev)
	
	for i in range(postive_index+1, len(sorted_list)):
		if sorted_list[i]-prev == 1:
			i += 1
			prev= sorted_list[i]
		else:
			return prev+1

		print sorted_list[i],


if __name__ == "__main__":
	list1 = [1,2,0]
	first_missing_positive_native(list1)
	list2 = [3,4,-1,1]
	first_missing_positive_native(list2)