"""
http://www.geeksforgeeks.org/merge-k-sorted-linked-lists/

Assumptions: No duplicates
"""

from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents


if __name__ == "__main__":
	array1=[1,3,5,7]
	header1 = generate_linked_list_with_values(array1)
	print "print_linked_list_contents header1: "
	print_linked_list_contents(header1)

	array2=[2,4,6,8]
	header2 = generate_linked_list_with_values(array2)
	print "\nprint_linked_list_contents header2: "
	print_linked_list_contents(header2)

	array3=[0,9,10,11]
	header3 = generate_linked_list_with_values(array3)
	print "\nprint_linked_list_contents header3: "
	print_linked_list_contents(header3)
