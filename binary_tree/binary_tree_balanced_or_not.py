from binary_tree_height import height_of_tree
from tree_helpers import example_unbalanced_tree, example_balanced_tree
from _tree import Tree

def binary_tree_balanced_or_not(root):
	if not root:
		return True

	left_ht = height_of_tree(root.left)
	right_ht = height_of_tree(root.right)
	if (abs(left_ht-right_ht) <=1 and
		binary_tree_balanced_or_not(root.left) and
		binary_tree_balanced_or_not(root.right)):

		return True
	return False

"""
Better solution: calculate the height within the call. Not in a seperate function
http://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
"""


def print_format(root):
	print "--------------"
	print "root: {0}".format(root)
	print "binary_tree_balanced_or_not: {0}".format(binary_tree_balanced_or_not(root))
	print "--------------"

if __name__ == "__main__":
	unbalanced_root =  example_unbalanced_tree()
	print_format(unbalanced_root)
	balanced_root = example_balanced_tree()
	print_format(balanced_root)