from _linked_list import Node
from _helper_generators import generate_empty_stack
from reverse_linked_list import reverse_linked_list
from _helper_printers import print_linked_list_contents, print_stack_contents


def convert_array_to_linked_list(array):
    head = None
    for val in array:
        if head == None:
            head = Node(val)
        else:
            temp = head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)
    return head

def convert_linked_list_to_stack(head):
    s = generate_empty_stack()
    #print_linked_list_contents(head)
    while head:
        #print head.contents
        s.push(head.contents)
        head = head.next
    return s

def test_convert_array_to_linked_list():
    print "# convert array to a linked list"
    head1 = convert_array_to_linked_list(['f', 'g', 'e', 'g', 'f'])
    print_linked_list_contents(head1)

    print "\n# reversed linked list"
    # does not work
    # reversed_head = head1
    reversed_head = reverse_linked_list(convert_array_to_linked_list(['f', 'g', 'e', 'g', 'f']))
    print_linked_list_contents(reversed_head)

def test_convert_linked_list_to_stack():
    head1 = convert_array_to_linked_list(['f', 'g', 'e', 'g', 'f'])
    # convert linked list to stack
    stack = convert_linked_list_to_stack(head1)
    print_stack_contents(stack)

if __name__ == "__main__":
    test_convert_array_to_linked_list()
    test_convert_linked_list_to_stack()
