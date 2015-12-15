class Tree:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def print_node(self):
		print self.data, self.left.data, self.right.data

	def __str__(self):
		return str(self.data)


	# crap
	# def count_total(self, tree):
	# 	if tree == None: return 0
	# 	return self.count_total(tree.left) + self.count_total(tree.right) + tree.cargo

def total(tree):
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.data

if __name__ == "__main__":
	print "Welcome to Trees data structure"
	left_tree = Tree(2)
	right_tree = Tree(3)
	tree = Tree(1, left_tree, right_tree)
	print tree
	print tree.left
	print tree.right
	#print tree.count_total(tree)
	print total(tree)
