from _linked_list import Node, get_linked_list
from linked_list_count_elements import count_no_of_elements

def naive_middle_element_in_linked_list(head):
    count = count_no_of_elements(head)
    mid = count/2
    while mid > 0 and head:
        head = head.next
        mid -= 1
    return head


def middle_element_of_linked_list(head):
    slow_p = fast_p = head
    #NOTE:  wrong watch out
    #while slow_p != None and fast_p.next != None:
    while (fast_p  and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        #print "slow_p : {0}, fast_p : {1}".format(slow_p, fast_p)
    return slow_p


def middle_element_with_head_and_one_fast_pointer(head):
    count = 0
    mid_ptr = head

    while(head):
        #print "head: {0}, mid:{1}".format(head, mid_ptr)
        # increment mid only for odd count value.
        # concept same as fast_pointer.
        if (count & 1):
            mid_ptr = mid_ptr.next
        count += 1
        head = head.next
    return mid_ptr



if __name__ == '__main__':
    #odd naive
    print "odd: middle element {0}".format(naive_middle_element_in_linked_list(get_linked_list(5)))
    # even naive
    print "even: middle element {0}".format(naive_middle_element_in_linked_list(get_linked_list(6)))
    #empty naive
    print "empty: middle element {0}".format(naive_middle_element_in_linked_list(None))

    #odd
    print "odd: middle element {0}".format(middle_element_of_linked_list(get_linked_list(5)))
    # even
    print "even: middle element {0}".format(middle_element_of_linked_list(get_linked_list(6)))
    # empty
    print "empty: middle element {0}".format(middle_element_of_linked_list(None))

    #odd
    print "odd: middle element {0}".format(middle_element_with_head_and_one_fast_pointer(get_linked_list(5)))
    # even
    print "even: middle element {0}".format(middle_element_with_head_and_one_fast_pointer(get_linked_list(6)))
    #empty
    print "empty: middle element {0}".format(middle_element_with_head_and_one_fast_pointer(None))
