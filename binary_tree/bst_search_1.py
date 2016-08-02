class Tree:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def print_node(self):
		print self.data, self.left.data, self.right.data

	def __str__(self):
		return str(self.data)

def example_bst():
	#n4 = Tree(4)
	n4 = helper_to_insert(None, 4)
	n8 = helper_to_insert(None, 8)

	#n6 = Tree(6, n4, n8)
	n6 = helper_to_insert(None,6)
	n6 = helper_to_insert(n6, n4, left=True)
	n6 = helper_to_insert(n6, n8, right=True)
	
	n12 = helper_to_insert(None, 12)#Tree(12)
	n20 = helper_to_insert(None, 20)#Tree(20)
	
	#n15 = Tree(15, n12, n20)
	n15 = helper_to_insert(None, 15)
	n15 = helper_to_insert(n15, n12, left=True)
	n15 = helper_to_insert(n15, n20, right=True)
	
	#root = Tree(10,n6, n15)
	root = helper_to_insert(None, 10)
	root = helper_to_insert(root, n6, left=True)
	root = helper_to_insert(root, n15, right=True)

	return root

def inorder(node):
	if node == None:
		return
	inorder(node.left)
	print node.data,
	inorder(node.right)

def bst_search(root, ele):
	
	if root == None:
		return None
	#print "calling bst", root, ele, root.data == ele
	if root.data == ele:
		return root
	elif root.data>ele:
		#print "moving left", root
		return bst_search(root.left, ele)
	else:
		#print "moving right", root
		return bst_search(root.right, ele)
	return -1	

def bst_insertion(root, ele):
	pass

def helper_to_insert(node, val, left=False, right=False):
	if not left and not right and not node:
		node = Tree(val)
	elif left:
		if isinstance(val, Tree):
			node.left = val
		else:
			node.left = Tree(val)
	elif right:
		if isinstance(val, Tree):
			node.right = val
		else:
			node.right = Tree(val)
	return node

"""
		10		
	6			15
4		8	12	20
"""

if __name__ == "__main__":
	root = example_bst()
	inorder(root)
	print "Searching for 8 : ", bst_search(root, 8)
	print "Searching for 20 : ", bst_search(root, 20)
	print "Searching for 4 : ", bst_search(root, 4)
	print "Searching for 25 : ", bst_search(root, 25)
