#http://www.programcreek.com/2014/02/leetcode-intersection-of-two-linked-lists-java/
from _helper_generators import generate_linked_list_with_values
from linked_list_count_elements import count_no_of_elements

# find the starting point of the linked list where it is merged
def intersection_of_two_linked_list(node1, node2):
	if not node1 or not node2:
		print "Empty linked list"
		return None

	len1 = count_no_of_elements(node1)
	len2 = count_no_of_elements(node2)
	print "len1 :", len1
	print "len2 :", len2

	# move the pointers
	diff = abs(len1 - len2)
	if (len1>len2):
		i = 0
		while (i<diff):
			node1 = node1.next
			i += 1
	else:
		i = 0
		while (i<diff):
			node2 = node2.next
			i += 1

	while (node1 != None and node2 != None):
		print "node1: {0}, node2:{1}".format(node1.contents, node2.contents)
		if node1.contents == node2.contents:
			return node1
		node1 = node1.next
		node2 = node2.next

	return None

if __name__ == "__main__":
	node1 = generate_linked_list_with_values([1, 2, 4, 3])
	node2 = generate_linked_list_with_values([10, 6, 1, 4, 3]) 
	print intersection_of_two_linked_list(node1, node2)
