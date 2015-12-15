from _tree import Tree

def max_value_bst_recursively(node):
    if node.right == None:
        return node
    return max_value_bst_recursively(node.right)

def max_value_bst(node):
    if node == None:
        return
    while(node.right != None):
        node = node.right
    return node

if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    max_value_recursive = max_value_bst_recursively(root)
    print "max in BST recursively: {0}".format(max_value_recursive)
    max_value =  max_value_bst(root)
    print "max in BST : {0}".format(max_value)
