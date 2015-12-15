from _helper_generators import generate_linked_list
from _helper_printers import print_linked_list_contents

def cycle_or_not(node):
    slow_p = node
    fast_p = node
    while(slow_p != None and fast_p != None and fast_p.next != None):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        print "slow_p : ", slow_p, "fast_p : ",fast_p#, fast_p.next.next
        if (slow_p == fast_p):
            print "cycle found"
            return True
    print "No cycle found"
    return False

head_cycle = generate_linked_list(5)
head_cycle.next.next.next.next = head_cycle.next.next
cycle_or_not(head_cycle)

head = generate_linked_list(5)
cycle_or_not(head)
