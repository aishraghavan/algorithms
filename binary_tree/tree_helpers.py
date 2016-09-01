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

def example_big_tree():
	"""
	                        50
	           20                         100
	     30        40               25            45
	 32                23        21    22      11

	"""
	n32 = Tree(32)
	n30 = Tree(30, n32)
	n23 = Tree(23)
	n40 = Tree(40, 23)
	n20 = Tree(20, n30, n40)
	n21 = Tree(21)
	n22 = Tree(22)
	n25 = Tree(25, n21, n22)
	n11 = Tree(11)
	n45 = Tree(45, n11)
	n100 = Tree(100,n25, n45)
	root = Tree(50, n20, n100)
	return root
