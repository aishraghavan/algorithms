from _tree import Tree

def example_unbalanced_tree():
	n8= Tree(8)
	n4= Tree(4,n8)
	n5= Tree(5)
	n2= Tree(2, n4,n5)
	n3= Tree(3)
	root= Tree(1, n2, n3)
	return root

def example_balanced_tree():
	n8= Tree(8)
	n9= Tree(9)
	n4= Tree(4, n8)
	n5= Tree(5)
	n2= Tree(2, n4, n5)
	n6= Tree(6, n9)
	n7= Tree(7)
	n3= Tree(3, n6, n7)
	root= Tree(1, n2, n3)
	return root

def sample_tree():
	n1= Tree(4)
	n2= Tree(5)
	n3= Tree(2, n1, n2)
	n4= Tree(3)
	root = Tree(1, n3, n4)
	return root