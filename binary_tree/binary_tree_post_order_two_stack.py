from _tree import Tree
from _stacks import Stack

def post_order_iterative_two_stack(node):
    if node == None:
        return
    stack1 = Stack()
    stack2 = Stack()
    stack1.push(node)
    while not stack1.is_empty():
        curr = stack1.pop()
        stack2.push(curr)
        if curr.left:
            stack1.push(curr.left)
        if curr.right:
            stack1.push(curr.right)
    while not stack2.is_empty():
        temp = stack2.pop()
        print temp,

if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    print "post order traversal two stacks: 5, 7, 6, 9, 20, 10, 8"
    post_order_iterative_two_stack(root)
