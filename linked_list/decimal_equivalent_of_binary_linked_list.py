"""
http://www.geeksforgeeks.org/decimal-equivalent-of-binary-linked-list/
"""
from linked_list_count_elements import count_no_of_elements
from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents


def decimal_equivalent_based_on_length(head, count):
	result  = 0 
	for i in range(count-1,-1,-1):
		result = result + head.contents *(pow(2,i))
		head = head.next
	return result


def decimal_equivalent(head):
	result = 0
	while head!=None:
		result = (result<<1)+head.contents
		head = head.next
	return result


if __name__ == "__main__":
	array1=[0,0,0,1,1,0,0, 1,0]
	header1 = generate_linked_list_with_values(array1)
	print "print_linked_list_contents: "
	print_linked_list_contents(header1)
	print "count_no_of_elements : {0}".format(count_no_of_elements(header1))
	print "decimal_equivalent_based_on_length : {0}".format(decimal_equivalent_based_on_length(header1, count_no_of_elements(header1)))
	print "decimal_equivalent : {0}".format(decimal_equivalent(header1))

	array2 = [1, 0, 0]
	header2 = generate_linked_list_with_values(array2)
	print "print_linked_list_contents: "
	print_linked_list_contents(header2)
	print "count_no_of_elements : {0}".format(count_no_of_elements(header2))
	print "decimal_equivalent_based_on_length : {0}".format(decimal_equivalent_based_on_length(header2, count_no_of_elements(header2)))
	print "decimal_equivalent : {0}".format(decimal_equivalent(header2))