from _tree import Tree

from _queue import Queue


def is_binary_tree_complete(node):
    if node == None:
        #probably tree is empty
        return True
    queue = Queue()
    queue.insert(node)
    while not queue.is_empty():
        temp = queue.remove()
        # if one of the children is None
        if ((temp.left== None and temp.right) or
              (temp.right== None and temp.left)):
            return False
        elif temp.left and temp.right:
            queue.insert(temp.left)
            queue.insert(temp.right)
    return True

def binary_tree_count(node):
    if node == None:
	return (0)
    return 1 + binary_tree_count(node.left) + binary_tree_count(node.right)

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
    #l4 = Tree(20)
    m1 = Tree(16, l1, l2)
    m2 = Tree(10, l3)
    root = Tree(8, m1, m2)
    return root

if __name__ =="__main__":
    bst_root = make_sample_bst()
    print "count nodes: {0}".format(binary_tree_count(bst_root))
    print "is_binary_tree_complete(bst_root) : {0}".format(is_binary_tree_complete(bst_root))
    non_bst_root = make_sample_non_bst()
    print "count nodes: {0}".format(binary_tree_count(non_bst_root))
    print "is_binary_tree_complete(non_bst_root) : {0}".format(is_binary_tree_complete(non_bst_root))