from _tree import Tree
from copy import deepcopy


def insert_in_bst(root, element):
    if root == None:
        root = Tree(element)

    elif root.data > element:
        #move left
        if root.left == None:
            root.left = Tree(element)
        else:
            insert_in_bst(root.left, element)
    elif root.data < element:
        #move right
        if root.right == None:
            root.right = Tree(element)
        else:
            insert_in_bst(root.right, element)
    return root

def insert_in_bst_iterative(root, element):
    temp = root
    if root == None:
        root = Tree(element)
        return root
    else:
        while root != None:
            if root.data > element:
                if root.left:
                    root = root.left
                else:
                    root.left = Tree(element)
                    break
            elif root.data < element:
                if root.right:
                    root = root.right
                else:
                    root.right = Tree(element)
                    break
        return temp

if __name__ == "__main__":
    print "insert_in_bst :"
    root1 = insert_in_bst(None, 5)
    root1 = insert_in_bst(root1, 7)
    root1 = insert_in_bst(root1, 6)
    root1 = insert_in_bst(root1, 9)
    root1 = insert_in_bst(root1, 4)
    root1 = insert_in_bst(root1, 2)
    print root1

    print "insert_in_bst_iterative :"
    root2 = insert_in_bst_iterative(None, 5)
    root2 = insert_in_bst_iterative(root2, 7)
    root2 = insert_in_bst_iterative(root2, 6)
    root2 = insert_in_bst_iterative(root2, 9)
    root2 = insert_in_bst_iterative(root2, 4)
    root2 = insert_in_bst_iterative(root2, 2)
    import ipdb; ipdb.set_trace()
