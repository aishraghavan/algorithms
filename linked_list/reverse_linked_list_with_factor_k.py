from reverse_linked_list import reverse_linked_list
from linked_list_count_elements import count_no_of_elements
from _helper_generators import generate_linked_list
from _helper_printers import print_linked_list_contents


def method_1_reverse_linked_list_after_k(head, k):
    temp_head = head
    length = count_no_of_elements(head)
    if k> length:
        print "Wrong input: k value greater than length"
        return
    if not head:
        print "list is empty"
        return
    count = 0
    prev_head = None
    while temp_head and count < k:
        prev_head = temp_head
        temp_head = temp_head.next
        count +=1
    print "\n head.contents:{0}".format(head)
    print "\n prev head contents:{0}".format(prev_head)
    print "\noriginal list: "
    print_linked_list_contents(head)

    reversed_k_head =reverse_linked_list(temp_head)
    print "\n reversed_k_head list:"
    print_linked_list_contents(reversed_k_head)

    prev_head.next = reverse_linked_list
    print "new::"
    #print_linked_list_contents(prev_head)


if __name__ == "__main__":
    head =  generate_linked_list(6)
    print_linked_list_contents(head)
    method_1_reverse_linked_list_after_k(head, 3)
