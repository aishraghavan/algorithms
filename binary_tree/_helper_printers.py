def print_stack_contents(stack):
    """
    print stack contents
    """
    if not stack.is_empty():
        print stack.items
    else:
        print "Stack is empty: {0}".format(stack)
