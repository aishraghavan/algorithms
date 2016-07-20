"""
linked_list_even_and_odd
http://www.geeksforgeeks.org/rearrange-a-linked-list-such-that-all-even-and-odd-positioned-nodes-are-together/

Input:   1->2->3->4
Output:  1->3->2->4

Input:   10->22->30->43->56->70
Output:  10->30->56->22->43->70
"""
from _linked_list import Node
from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents

def linked_list_even_and_odd(head):
	if not head:
		return None

	odd_even_head = None
	fast_ptr = head
	
	while(fast_ptr != None):
		odd_even_head = insert_node(odd_even_head, fast_ptr)
		if fast_ptr.next and fast_ptr.next.next:
			fast_ptr = fast_ptr.next.next
		else:
			#last node
			break

	fast_ptr = head.next
	while(fast_ptr != None):
		odd_even_head = insert_node(odd_even_head, fast_ptr)
		if fast_ptr.next and fast_ptr.next.next:
			fast_ptr = fast_ptr.next.next
		else:
			#last node
			break
	return odd_even_head

def insert_node(head, node):
	if head == None:
		temp = Node(node.contents)
		return temp
	else:
		prev = head
		while(prev.next!= None):
			prev = prev.next
		temp = Node(node.contents)
		prev.next = temp
		return head


def test_and_print(array):
	head1 = generate_linked_list_with_values(array)
	print "\n--------------"
	print "linked list before even_and_odd"
	print_linked_list_contents(head1)
	head1 = linked_list_even_and_odd(head1)
	print "\nlinked list after even_and_odd"
	print_linked_list_contents(head1)

if __name__ == "__main__":
	arrays = [[1, 2, 3, 4],
			  [10, 22, 30, 43, 56, 70],
			  #odd size
			  [10, 22, 30, 43, 56],
			  # two elements
			  [10,20],
			  #one element
			  [100]
			  ]
	for array in arrays:
		test_and_print(array)
	#None type
	print "linked list before even_and_odd"
	print_linked_list_contents(None)
	head1 = linked_list_even_and_odd(None)
	print "\nlinked list after even_and_odd"
	print_linked_list_contents(head1)
