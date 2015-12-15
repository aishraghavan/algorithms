from _linked_list import Node
from _helper_generators import generate_linked_list
from _helper_printers import print_linked_list_contents

# def reverse_linked_list_recursively(head):
#     first = head
#     rest = None
#     if first == None:
#         return
#     rest = first.next
#     if rest == None:
#         return
#     first.next.next = first
#     first.next = None
#     head = rest
#     return reverse_linked_list_recursively(rest)

def reverse(node):
    def reverse_helper(old_head, new_head):
        if old_head is None:
            return new_head
        next_old_head = old_head.next
        old_head.next = new_head
        return reverse_helper(next_old_head, old_head)

    return reverse_helper(node, None)

if __name__ == "__main__":
    print "hello"
    head =  generate_linked_list(6)
    print "Orginal list"
    print_linked_list_contents(head)
    print "reversed linked list python"
    no_python_way = reverse(head)
    print_linked_list_contents(no_python_way)
    # print "reversed linked list"
    # no = reverse_linked_list_recursively(head)
    # print_linked_list_contents(no)
