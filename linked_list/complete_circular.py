from _linked_list import Node
from _helper_printers import print_linked_list_contents


def complete_circular(head):
	if head == None:
		return True
	node = head.next
	while node!= None and node!=head:
		node = node.next
	return (node==head)
	

def _complete_circular_eg():
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n1
	head = n1
	return head


def _not_complete_circular_eg():
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n2
	head = n1
	return head

def _simple_list_eg():
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	head = n1
	return head



if __name__ == "__main__":
	complete_circular_head = _complete_circular_eg()
	print "is it complete_circular? {0}".format(complete_circular(complete_circular_head))
	# fails for this input
	# not_complete_circular_head = _not_complete_circular_eg()
	# print "is it complete_circular? {0}".format(complete_circular(not_complete_circular_head))
	simple_head = _simple_list_eg()
	print "is it complete_circular? {0}".format(complete_circular(simple_head))





