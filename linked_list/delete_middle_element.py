"""
http://www.geeksforgeeks.org/delete-middle-of-linked-list/
"""
from middle_element_in_linked_list import middle_element_of_linked_list
from _linked_list import get_linked_list
from _helper_printers import print_linked_list_contents

def delete_middle_element(head):
	if not head:
		return None
	slowp = fastp= head
	prev = None
	while fastp!= None and fastp.next!= None:
		fastp = fastp.next.next
		prev = slowp
		slowp = slowp.next

	prev.next = slowp.next
	del slowp
	return head

if __name__ == '__main__':
	head = get_linked_list(5)
	print "middle element : "
	print "new linked list"
	new_head = delete_middle_element(head)
	print_linked_list_contents(new_head)

