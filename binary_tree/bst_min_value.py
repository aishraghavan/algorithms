from _tree import Tree

def min_value_bst_recursively(node):
    if node.left == None:
        return node
    return min_value_bst_recursively(node.left)

def min_value_bst(node):
    if node == None:
        return
    while(node.left != None):
        node = node.left
    return node

if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    min_value_recursive = min_value_bst_recursively(root)
    print "min in BST recursively: {0}".format(min_value_recursive)
    min_value =  min_value_bst(root)
    print "min in BST : {0}".format(min_value)
