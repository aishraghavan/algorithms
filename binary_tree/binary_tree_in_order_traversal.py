from _tree import Tree
from _stacks import Stack

def in_order_iterative(node):
    if node == None:
        return
    stack1 = Stack()
    #stack1.push(node)
    curr = node
    done = False
    while not done:
        if curr != None:
            stack1.push(curr)
            curr = curr.left
        else:
            if not stack1.is_empty():
                curr = stack1.pop()
                print curr,
                curr = curr.right
            else:
                done = True

if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    print "in order traversal : 5, 6, 7, 8, 9, 10, 20"
    in_order_iterative(root)
