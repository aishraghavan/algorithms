from _linked_list import Node
from _helper_generators import generate_linked_list
from _helper_printers import print_linked_list_contents
from copy import deepcopy

def reverse_linked_list(head):
    currp = head
    prevp = None
    nextp = None
    while currp != None:
        nextp = currp.next
        currp.next = prevp
        prevp = currp
        currp = nextp

    print "prevp"
    print_linked_list_contents(prevp)

if __name__ == "__main__":
    head =  generate_linked_list(6)
    print "Orginal list"
    print_linked_list_contents(head)
    reverse_linked_list(head)
