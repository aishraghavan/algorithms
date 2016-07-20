def bubble_sort(array):
	if not array or len(array)== 0:
		return -1
	n = len(array)
	for i in range(n):
		for j in range(n-1-i):
			#Descending
			#if array[j+1]>array[j]:
			
			#Ascending
			if array[j+1]<array[j]:
				array[j+1], array[j] = array[j], array[j+1]
	return array

def print_format(array):
	print "------------------------"
	print "input: {0}".format(array)
	print "bubble sort: {0}".format(bubble_sort(array))
	print "------------------------"

if __name__ == "__main__":
	array = [1,9,5,7,2]
	print_format(array)