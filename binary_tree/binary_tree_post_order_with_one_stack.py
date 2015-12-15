from _tree import Tree
from _stacks import Stack

def post_order_iterative_one_stack(node):
    if node == None:
        return
    stack1 = Stack()
    stack1.push(node)
    prev = None
    while not stack1.is_empty():
        curr = stack1.top()
        if (prev == None or prev.right == curr or prev.left ==curr):
            # go down the Tree
            if curr.left != None:
                stack1.push(curr.left)
            elif curr.right != None:
                stack1.push(curr.right)
            else:
                print stack1.pop()
        elif curr.left == prev:
            if curr.right != None:
                stack1.push(curr.right)
            else:
                print stack1.pop()

        elif curr.right == prev:
            print stack1.pop()
        prev = curr

if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    print "post order traversal one stack: 5, 7, 6, 9, 20, 10, 8"
    post_order_iterative_one_stack(root)
