from _tree import Tree
from _stacks import Stack

def search_in_bst_iterative(root, element):
    if root == None:
        return False

    curr = root
    while curr != None:
        if curr.data == element:
            return True
        elif curr.data > element:
            curr = curr.left
        elif curr.data < element:
            curr = curr.right
    return False

def search_in_bst_recursive(root, element):
    if root == None:
        return False

    if root.data == element:
        return True

    elif root.data > element:
        return search_in_bst_recursive(root.left, element)
    elif root.data < element:
        return search_in_bst_recursive(root.right, element)
    #return False

def make_sample_bst():
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    return root

if __name__ == "__main__":
    sample_bst_root = make_sample_bst()
    print "Search 6 in bst iterative : "
    print search_in_bst_iterative(sample_bst_root, 6)
    print "Search 9 in bst iterative : "
    print search_in_bst_iterative(sample_bst_root, 9)
    print "Search 16 in bst iterative : "
    print search_in_bst_iterative(sample_bst_root, 16)

    print "Search 6 in bst: "
    print search_in_bst_recursive(sample_bst_root, 6)
    print "Search 9 in bst: "
    print search_in_bst_recursive(sample_bst_root, 9)
    print "Search 16 in bst: "
    print search_in_bst_recursive(sample_bst_root, 16)
