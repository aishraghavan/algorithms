"""
linked_list_merge_inplace()
http://www.geeksforgeeks.org/in-place-merge-two-linked-list-without-changing-links-of-first-list/
"""
from _linked_list import Node
from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents

def linked_list_merge_inplace(head1, head2):
	if not head1 or not head2:
		return None

	ptr1 = head1
	ptr2 = head2
	prev = None
	#print "head1 :{0}, head2: {1}".format(head1, head2)
	while ptr1 != None and ptr2 != None:
		#import ipdb;ipdb.set_trace()
		if ptr1.contents > ptr2.contents:
			#insert ptr2 in ptr1
			ptr1 = insert_node(ptr1, prev, ptr2)
			if prev == None:
				head1 = ptr1
			ptr2 = ptr2.next
		else:
			prev = ptr1
			ptr1 = ptr1.next

	#print "ptr1: {0}, ptr2: {1}".format(ptr1, ptr2)
	while ptr2!= None:
		insert_node(head=None, prev=prev, node= ptr2)
		ptr2 = ptr2.next
	return head1

def insert_node(head, prev, node):
	if prev == None:
		temp = Node(node.contents)
		temp.next = head
	else:
		temp = Node(node.contents)
		prev.next = temp
		temp.next = head
	return temp


def test_and_print(array1, array2):
	head1 = generate_linked_list_with_values(array1)
	head2 = generate_linked_list_with_values(array2)
	print "\n--------------"
	print "linked list 1"
	print_linked_list_contents(head1)
	print "\nlinked list 2"
	#print "--------------"
	print_linked_list_contents(head2)
	head1= linked_list_merge_inplace(head1, head2)
	print "\nOutput of merging linked list 1 and 2:"
	print_linked_list_contents(head1)


if __name__ == "__main__":
	array1 = [2,4,7,8,10]
	array2 = [1,3,12]
	test_and_print(array1, array2)
	array3 = [1,3,5,7,9,12]
	array4 = [2,4,6,8,11]
	test_and_print(array3, array4)