def print_double_linked_list_contents(node):
    """
    print linked list contents
    """
    if not node:
        print "Empty linked list"
    while (node and node.contents != None) :
        print "prev:{0}, Node: {1}, next:{2}".format(node.prev, node.getContents(), node.next)
        node = node.next

def print_linked_list_contents(node):
    """
    print linked list contents
    """
    if not node:
        print "Empty linked list"
    while node:
        print node.getContents(),
        node = node.next

def print_stack_contents(stack):
    """
    print stack contents
    """
    if not stack.is_empty():
        print stack.items
    else:
        print "Stack is empty: {0}".format(stack)


def print_tree_node(node):
    print "Node data :{0}, left:{1}, right:{2}".format(node.data, node.left, node.right)
