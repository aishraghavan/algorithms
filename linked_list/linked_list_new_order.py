from _helper_generators import generate_linked_list, generate_linked_list_with_values
from _helper_printers import print_linked_list_contents
from middle_element_in_linked_list import middle_element_of_linked_list
from reverse_linked_list import reverse_linked_list
from copy import deepcopy
from _linked_list import Node


def _check_parameters(head, reversed_head, middle):
    if not head or not reversed_head or not middle:
        return False
    return True

def first_last_ordering_without_stack(head, reversed_head, middle):
    if not _check_parameters(head, reversed_head, middle):
        return
    t_head = head
    t_reversed_head = reversed_head
    count = 1
    new_head = Node()
    new_head_pointer = new_head
    while t_head != middle:
        if count%2:
            new_head.next = Node(t_head.contents)
            new_head = new_head.next
            # if not new_head:
            #     new_head = Node(t_head.contents)
            # else:
            #     new_head.next = Node(t_head.contents)
            #     new_head = new_head.next
            t_head = t_head.next
        else:
            # if not new_head:
            #     new_head = Node(t_reversed_head.contents)
            # else:
            #     new_head.next = Node(t_reversed_head.contents)
            #     new_head =  new_head.next
            new_head.next = Node(t_reversed_head.contents)
            new_head =  new_head.next
            t_reversed_head = t_reversed_head.next
        count = count + 1
    new_head.next = Node(t_head.contents)
    return  new_head_pointer

def first_last_ordering_with_stack(head, reversed_head, middle):
    if not _check_parameters(head, reversed_head, middle):
        return
    t_head = head
    t_reversed_head = reversed_head
    count = 1
    lista = []
    while t_head != middle:
        if count%2:
            lista.append(t_head.contents)
            t_head =  t_head.next
        else:
            lista.append(t_reversed_head.contents)
            t_reversed_head = t_reversed_head.next
        count = count + 1
    lista.append(t_head.contents)
    new_head = generate_linked_list_with_values(lista)
    return new_head

if __name__ == "__main__":
    head = generate_linked_list(6)
    print "actual order :"
    print_linked_list_contents(head)
    print "\nexpected output: 1->6->2->5->3->4"
    middle = middle_element_of_linked_list(head)

    rest_reversed = reverse_linked_list(middle)

    print "\nreversed :"
    print_linked_list_contents(rest_reversed)

    new_order = first_last_ordering_with_stack(head, rest_reversed, middle)
    print "\nnew linked list order :"
    print_linked_list_contents(new_order)

    print "\nnew linked list order without stack:"
    new_call = first_last_ordering_without_stack(head, rest_reversed, middle)
    print_linked_list_contents(new_call)


    # Empty case
    print_linked_list_contents(first_last_ordering_with_stack(None, None, None))
    print_linked_list_contents(first_last_ordering_without_stack(None, None, None))
