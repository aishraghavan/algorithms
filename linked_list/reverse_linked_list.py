from _linked_list import Node
from _helper_generators import generate_linked_list
from _helper_printers import print_linked_list_contents
from copy import deepcopy

def reverse_linked_list(head):
    temp = deepcopy(head)
    if not temp:
        return temp
    prev_ptr = None
    curr_ptr = temp
    next_ptr = curr_ptr.next
    #while curr_ptr and next_ptr:
    #while next_ptr.next: wrong
    #while next_ptr:
    while curr_ptr:
        #print " prev_ptr : {0}, curr_ptr: {1}, next_ptr: {2}".format(prev_ptr, curr_ptr, next_ptr)
        next_ptr = curr_ptr.next
        curr_ptr.next = prev_ptr
        prev_ptr = curr_ptr
        curr_ptr = next_ptr

    return prev_ptr


def reverse_linked_list_recursively(head):
    print "yet to be implemented."
    pass


if __name__ == "__main__":
    head =  generate_linked_list(6)
    print "Orginal list"
    print_linked_list_contents(head)
    print "\nReversed list"
    print_linked_list_contents(reverse_linked_list(head))

    empty_head = generate_linked_list(0)
    print_linked_list_contents(reverse_linked_list(empty_head))

    #reverse_linked_list_recursively(head)
