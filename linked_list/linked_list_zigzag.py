"""
http://www.geeksforgeeks.org/linked-list-in-zig-zag-fashion/
"""
from _linked_list import Node
from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents

#not implemented completely
def sort_linked_list_zig_zag(head):
	if not head:
		return
	flag = True
	curr = head
	prev = None
	while(curr.next!= None):
		if flag:
			if curr.contents> curr.next.contents:
				helper_swap_nodes(prev, curr, curr.next)
		else:
			if curr.contents< curr.next.contents:
				helper_swap_nodes(prev, curr, curr.next)
		flag = not flag
		prev = curr
		curr = curr.next
	return head


def helper_swap_nodes(prev, node1, node2):
    if not node1 or not node2:
        return
    if prev:
        prev.next = node2
    temp = node2.next
    node2.next = node1
    node1.next = temp
    return

def test_and_print(array):
    head1 = generate_linked_list_with_values(array)
    print "\n--------------"
    print "linked list before sorting"
    print_linked_list_contents(head1)
    head1 = sort_linked_list_zig_zag(head1)
    print "\nlinked list after sorting"
    print_linked_list_contents(head1)

if __name__ == "__main__":
    arrays = [[1,2,3,4],
    		  [11,15,20,5,10],
    		  [4,3,7,8,2,6,1]]
              
    for array in arrays:
        test_and_print(array)