from _stacks import Stack
from _linked_list import Node
from _double_linked_list import _double_linked_list_Node
from _helper_printers import print_linked_list_contents, print_stack_contents

def generate_empty_stack():
    s = Stack()
    return s

def generate_stack(length):
    s = generate_empty_stack()
    # Pushing in process
    for i in range(length):
        num = 10*(i+1)
        s.push(num)
    return s

def generate_stack_with_values(array):
    s = generate_empty_stack()
    for val in array:
        s.push(val)
    return s

def generate_linked_list(length, start=1):
    head = Node()
    temp_node = head
    for i in xrange(start, length+start):
        node = Node(i)
        temp_node.next = node
        temp_node = temp_node.next
    head = head.next
    #print_linked_list_contents(head)
    return head

def generate_linked_list_with_values(array):
    head = Node()
    temp_node = head
    for element in array:
        node = Node(element)
        temp_node.next = node
        temp_node = temp_node.next
    head = head.next
    return head


def generate_double_linked_list(length, start=1):
    head = _double_linked_list_Node()
    temp_node = head
    prev_node = _double_linked_list_Node()

    for i in xrange(start, length+start):
        node = _double_linked_list_Node(i)
        temp_node.next = node
        prev_node = temp_node
        temp_node = temp_node.next
        temp_node.prev = prev_node
    head =  head.next
    #print__double_linked_list_contents(head)
    return head

if __name__ == "__main__":
    print_stack_contents(generate_empty_stack())
    print_stack_contents(generate_stack(6))
    print_linked_list_contents(generate_linked_list(4))
