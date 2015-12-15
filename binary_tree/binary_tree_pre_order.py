from _tree import Tree
from _stacks import Stack

def pre_order_iterative(node):
    if node == None:
        return
    stack1 = Stack()
    stack1.push(node)
    while not stack1.is_empty():
        temp = stack1.pop()
        print temp,
        if temp.right:
            stack1.push(temp.right)
        if temp.left:
            stack1.push(temp.left)

if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    print "pre order traversal : 8, 6, 5, 7, 10, 9, 20"
    pre_order_iterative(root)
