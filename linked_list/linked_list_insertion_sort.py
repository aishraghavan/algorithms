"""
push(&a, 5);
    push(&a, 20);
    push(&a, 4);
    push(&a, 3);
    push(&a, 30);

    Linked List before sorting
30  3  4  20  5
Linked List after sorting
3  4  5  20  30
"""
from _linked_list import Node
from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents


def insertion_sort_linked_list(head):
    if not head:
        return
    ptr1 = head
    prev = None
    done = False
    while not done:
        if ptr1 == None:
            ptr1 = head
            # when to stop
            if helper_is_sorted(ptr1):
                done = True
        if ptr1 and ptr1.next:
            if ptr1.contents >ptr1.next.contents:
                helper_swap_nodes(prev, ptr1, ptr1.next)
        prev = ptr1
        ptr1 = ptr1.next

    return head


def helper_is_sorted(head):
    ptr1 = head
    while ptr1 and ptr1.next != None:
        if ptr1.contents >ptr1.next.contents:
            return False
        ptr1 = ptr1. next
    return True


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
    head1 = insertion_sort_linked_list(head1)
    #print "\n is_sorted(head1):{0}".format(is_sorted(head1))
    print "\nlinked list after sorting"
    print_linked_list_contents(head1)

if __name__ == "__main__":
    arrays = [[1,12, 3, 14, 5],
                [1,2,3,4,5]]
              
    for array in arrays:
        test_and_print(array)