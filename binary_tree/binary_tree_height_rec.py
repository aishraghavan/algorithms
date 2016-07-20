from tree_helpers import sample_tree

def binary_tree_height_rec(head):
    if head == None:
        return 0
    return 1 + max(binary_tree_height_rec(head.left),
     				binary_tree_height_rec(head.right))

if __name__ == "__main__":
	root = sample_tree()
	print binary_tree_height_rec(root)
