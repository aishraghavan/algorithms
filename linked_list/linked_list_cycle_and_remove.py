"""
http://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
"""
from _helper_generators import generate_linked_list
from _helper_printers import print_linked_list_contents

def linked_list_cycle_and_remove_1(head, loop_ptr):
    if not head or not loop_ptr:
        return None
    ptr1 = head
    while(1):
        ptr2 = loop_ptr

        while (ptr2.next != loop_ptr and
               ptr2.next != ptr1):
            ptr2 = ptr2.next

        # checking if the second condition in the while loop was satisfied.
        if ptr2.next == ptr1:
            break
        ptr1 = ptr1.next
    ptr2.next = None

def linked_list_cycle_and_remove_with_cycle_count(head, loop_ptr):
    if not head or not loop_ptr:
        return None
    ptr1 = head
    ptr2 = head
    #step1: count the elements in cycle
    loop_count = helper_count_nodes(loop_ptr)
    
    #step2: ptr2 is now k nodes ahead of ptr1
    for i in range(loop_count):
        ptr2 = ptr2.next

    
    #step3: determine the start of loop
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    #step4: Follow this to get to the end of the loop
    # for i in range(1, loop_count):
    #   ptr2 = ptr2.next

    while ptr2.next != ptr1:
        ptr2 = ptr2.next

    ptr2.next = None

def linked_list_efficient_detect_and_remove(head):
    if not head :
        return None

    slow_p = head
    # Note fast_p starts at head.next
    fast_p = head.next
    while(fast_p != None):
        if fast_p.next == None:
            break
        if (slow_p == fast_p):
            break
        slow_p = slow_p.next
        fast_p = fast_p.next.next

    # makes sure that the break happened at that condition
    if (slow_p == fast_p):
        slow_p = head
        # moves at the same phase. fast_p is already in the loop. Hence, it will reach the 
        while(slow_p != fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next

        fast_p.next = None



def helper_cycle_or_not(node):
    slow_p = node
    fast_p = node
    #print "slow_p : ", slow_p, "fast_p : ",fast_p
    while(slow_p != None and fast_p != None and fast_p.next != None):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        #print "slow_p : ", slow_p, "fast_p : ",fast_p#, fast_p.next.next
        if (slow_p == fast_p):
            return True, slow_p
    #print "No cycle found"
    return False, None

def helper_count_nodes(loop_ptr):
    ptr1 = loop_ptr
    ptr2 = loop_ptr
    k = 1
    while(ptr2.next != ptr1):
        ptr2 = ptr2.next
        k += 1
    return k

def helper_generate_cycle_list():
    head_cycle = generate_linked_list(5)
    head_cycle.next.next.next.next.next = head_cycle.next.next
    return head_cycle

def test_and_print_helper():
    head_cycle = helper_generate_cycle_list()
    result, loop_ptr = helper_cycle_or_not(head_cycle)
    print "result : {0}, loop_ptr: {1}".format(result, loop_ptr)
    print "--------------"
    print "helper_count_nodes : {0}".format(helper_count_nodes(loop_ptr))
    print "--------------"

def test_linked_list_cycle_and_remove_1():
    head_cycle = helper_generate_cycle_list()
    result, loop_ptr = helper_cycle_or_not(head_cycle)
    print "--------------"
    print "Calling linked_list_cycle_and_remove_1:"
    linked_list_cycle_and_remove_1(head_cycle, loop_ptr)
    print_linked_list_contents(head_cycle)
    print "\n--------------"

def test_linked_list_cycle_and_remove_with_cycle_count():
    head_cycle = helper_generate_cycle_list()
    result, loop_ptr = helper_cycle_or_not(head_cycle)
    print "Calling linked_list_cycle_and_remove_with_cycle_count"
    linked_list_cycle_and_remove_with_cycle_count(head_cycle, loop_ptr)
    print_linked_list_contents(head_cycle)
    print "\n--------------"

def test_linked_list_efficient_detect_and_remove():
    head_cycle = helper_generate_cycle_list()
    print "Calling linked_list_efficient_detect_and_remove"
    linked_list_efficient_detect_and_remove(head_cycle)
    print_linked_list_contents(head_cycle)
    print "\n--------------"



if __name__ == "__main__":
    test_linked_list_cycle_and_remove_1()
    test_linked_list_cycle_and_remove_with_cycle_count()
    test_linked_list_efficient_detect_and_remove()
    
    #print "ptr2.contents : {0}, ptr1.contents : {1}".format(ptr2.contents, ptr1.contents)

