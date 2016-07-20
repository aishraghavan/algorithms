"""
linked_list_abosolute_value_sorting
http://www.geeksforgeeks.org/sort-linked-list-already-sorted-absolute-values/
Input :  1 -> -10 
output: -10 -> 1
[1, -10]

Input : 1 -> -2 -> -3 -> 4 -> -5 
output: -5 -> -3 -> -2 -> 1 -> 4 
[1,-2, -3, 4, -5]

Input : -5 -> -10 
Output: -10 -> -5
[-5,-10]

Input : 5 -> 10 
output: 5 -> 10
[5, 10]
"""
from _linked_list import Node
from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents

def sort_linked_list_efficiently(head):
	if not head:
		return None
	ptr1 = head
	prev = None
	while(ptr1!= None):
		
		if prev != None and ptr1.contents<prev.contents:
			head = helper_insert_in_front_and_modify(ptr1, head, prev)
		prev= ptr1
		ptr1 = ptr1.next

	return head

def helper_insert_in_front_and_modify(node, head, prev):
	if not node:
		return 
	node_next = node.next 

	#insert in front
	temp = Node(node.contents)
	temp.next = head

	#make connection
	prev.next = node_next
	# delete node
	del node

	return temp



def test_and_print(array):
	head1 = generate_linked_list_with_values(array)
	print "\n--------------"
	print "linked list before sorting"
	print_linked_list_contents(head1)
	head1 = sort_linked_list_efficiently(head1)
	print "\nlinked list after sorting"
	print_linked_list_contents(head1)

if __name__ == "__main__":
	arrays = [[1, -10],
			  [1,-2, -3, 4, -5],
			  [-5,-10],
			  [5, 10]]
	for array in arrays:
		test_and_print(array)