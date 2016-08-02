"""
http://www.geeksforgeeks.org/find-smallest-range-containing-elements-from-k-lists/


Given k sorted lists of integers of size n each, find the smallest range that includes
at least element from each of the k lists. If more than one smallest ranges are found, print any one of them.

import heapq
h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
heapq.heappop(h)
(1, 'write spec')

import heapq
h = []
heapq.heappush(h, (6, 2))
heapq.heappush(h, (8,1))
heapq.heappush(h, (7,0))



"""
import heapq

def find_smallest_range_containing_k_lists(list_of_lists, k, n):
	heap = []
	# insert all zero index
	for i in range(k):
		heapq.heappush(heap, (list_of_lists[i][0], i))

	# same as above
	# heapq.heappush(heap, (list_of_lists[0][0], 0))
	# heapq.heappush(heap, (list_of_lists[1][0], 1))
	# heapq.heappush(heap, (list_of_lists[2][0], 2))		
	#import ipdb;ipdb.set_trace()
	curr_range = (min(heap), max(heap), max(heap)[0]-min(heap)[0])
	
	while(1):
		temp_range = (min(heap), max(heap), max(heap)[0]-min(heap)[0])
		if temp_range[2]< curr_range[2]:
			curr_range = temp_range
		
		temp = heapq.heappop(heap)
		list_in_consideration = temp[1]
		list_of_elements[list_in_consideration].remove(list_of_elements[list_in_consideration][0])
		if len(list_of_elements[list_in_consideration]) == 0:
			return curr_range

		heapq.heappush(heap, (list_of_elements[list_in_consideration][0], list_in_consideration))


def working_heap(list_of_lists, k, n):
	heap = []
	max_range = 0
	for lower_index in range(n):
		for top_index in range(k):
			#print heap
			#push element into heap
			heapq.heappush(heap, (list_of_lists[top_index][lower_index], 	top_index))		
			#pop element from heap

	print heap
	return heap

if __name__ == "__main__":
	list_of_elements = [
			[4, 7, 9, 12, 15],
			[0, 8, 10, 14, 20],
			[6, 12, 16, 30, 50]]
	#print len(list_of_elements)
	print find_smallest_range_containing_k_lists(list_of_elements, k=len(list_of_elements), n=len(list_of_elements[0]))
