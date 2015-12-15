from _tree import Tree
from _stacks import Stack
from _queue import Queue

def size_of_tree_recursively(node):
    if node == None:
        return 0;
    return size_of_tree_recursively(node.left) + \
            size_of_tree_recursively(node.right) + 1

def size_of_tree_stack(node):
    if node == None:
        return
    stack1 = Stack()
    stack1.push(node)
    size = 0
    while not stack1.is_empty():
        temp = stack1.pop()
        size += 1
        if temp.left:
            stack1.push(temp.left)
        if temp.right:
            stack1.push(temp.right)
    return size

def size_of_tree_queue(node):
    if node == None:
        return
    queue1 = Queue()
    queue1.insert(root)
    size = 0
    while not queue1.is_empty():
        temp = queue1.remove()
        size += 1
        if temp.left:
            queue1.insert(temp.left)
        if temp.right:
            queue1.insert(temp.right)
    return size

if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    print "Size of the tree recursively: {0}".format(size_of_tree_recursively(root))
    print "Size of the tree stack: {0}".format(size_of_tree_stack(root))
    print "Size of the tree queue: {0}".format(size_of_tree_queue(root))
