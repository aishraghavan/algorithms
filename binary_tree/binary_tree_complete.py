from _tree import Tree

def binary_tree_count(node):
    if node == None:
	return (0)
    return	1 + binary_tree_count(node.left) + binary_tree_count(node.right)

def binary_tree_complete(node, index, number_of_nodes):
    if node == None:
        return True
    if index>=number_of_nodes:
        return False
    return (
        binary_tree_complete(node.left, 2*index + 1, number_of_nodes) and
	binary_tree_complete(node.right, 2*index + 2, number_of_nodes) 
	)

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

if __name__ =="__main__":
    root1 = make_sample_bst()
    print binary_tree_count(root1)
    print binary_tree_complete(root1, 0 , binary_tree_count(root1))
