"""
missing_number_in_ap
"""
def missing_number_in_ap_simple(array):
	if not array or len(array) == 0:
		return None
	num = len(array)
	start = array[0]
	end = array[num-1]
	diff = (end-start)/num
	expected_sum = (num+1)*(start+end)/2
	sum = 0
	for ele in array:
		sum += ele
	return expected_sum-sum

def missing_number_in_ap_binary_search(array):
	if not array or len(array) == 0:
		return None
	num = len(array)
	start = array[0]
	end = array[num-1]
	diff = (end-start)/num
	return find_missing_utility(array, 0, num-1, diff)

def find_missing_utility(array, start, end, diff):
	if end<=start:
		return -1
	mid = start + (end-start)/2

	if array[mid+1]-array[mid] != diff:
		return array[mid]+ diff

	if mid>0 and array[mid]-array[mid-1] != diff:
		return array[mid-1]+ diff	

	if array[mid] == array[0]+mid*diff:
		return find_missing_utility(array, mid+1, end, diff)
	else:
		return find_missing_utility(array, start, mid-1, diff)

if __name__ == "__main__":
	array1 = [2, 4, 8, 10, 12, 14]
	print "Missing number Linear Search: {0}".format(missing_number_in_ap_simple(array1))
	print "Missing number Binary Search: {0}".format(missing_number_in_ap_binary_search(array1))


