from _double_linked_list import _double_linked_list_Node
from _helper_generators import generate_double_linked_list
from _helper_printers import print_double_linked_list_contents

def reverse_double_linked_list(head):
    temp = _double_linked_list_Node()
    curr = head

    while(curr != None):
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
    if temp != None:
        head = temp.prev

    return head


head = generate_double_linked_list(6)
print_double_linked_list_contents(head)
print "---After reversing---"
new_head = reverse_double_linked_list(head)
print_double_linked_list_contents(new_head)
