from _tree import Tree
from _stacks import Stack

def bst_or_not(node):
    if node == None:
        return
    stack1 = Stack()
    stack1.push(node)
    #import ipdb; ipdb.set_trace()
    while not stack1.is_empty():
        temp = stack1.pop()
        if not temp.left is None:
            if temp.left.data < temp.data :
                stack1.push(temp.left)
            else:
                return False
        if not temp.right is None:
            if temp.right.data > temp.data :
                stack1.push(temp.right)
            else:
                return False
    return True

def make_sample_bst():
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    return root

def make_sample_non_bst():
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(19)
    l4 = Tree(20)
    m1 = Tree(16, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    return root

if __name__ == "__main__":
    sample_bst_root = make_sample_bst()
    print "bst_or_not: {0}".format(bst_or_not(sample_bst_root))
    sample_non_bst_root = make_sample_non_bst()
    print "bst_or_not: {0}".format(bst_or_not(sample_non_bst_root))
