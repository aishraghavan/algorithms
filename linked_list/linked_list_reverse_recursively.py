from _helper_printers import print_linked_list_contents
from _helper_generators import generate_linked_list

def reverse_linked_list_recursively(node):
    if node == None:
        return ;

    first_node = node
    rest_node = first_node.next

    print "reverse called with :", node
    if (rest_node == None):
        return ;
    #print rest_node
    reverse_linked_list_recursively(rest_node)
    print "returning back reverse called with : rest node :{0}, first_node:{1}".format(rest_node, first_node)
    first_node.next.next = first_node
    first_node.next = None
    node = rest_node
    print "printing node :", node, "rest_node :", rest_node
    print_linked_list_contents(node)
    #return rest_node


head = generate_linked_list(3)
#print_linked_list_contents(head)
rev = reverse_linked_list_recursively(head)
print "reverse: "
print_linked_list_contents(head)
