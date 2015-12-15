from _tree import Tree
from _tree_traversal import TreeTraversal
from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents


class linked_list_to_bst:
	def __init__(self, array):
		self.array = array
		self.count = 0

	def convert_to_bst(self, start, end):
		self.count +=1
		#print "count: ", self.count
		rootNode = None
		if (start>end):
			return None
		else:
			mid =(start+end)/2
			# mid =(start+(end-start))/2

			#print "left :  " ,start, mid, self.array[mid]
			leftNode = Tree(self.convert_to_bst(start, mid-1))
			#leftNode.print_node()

			#print "mid: " ,self.array[mid]
			rootNode = Tree(self.array[mid])
			rootNode.left = leftNode
			#rootNode.print_node()

			#print "right: ", mid+1, end,  self.array[mid]
			rightNode = Tree(self.convert_to_bst(mid+1, end))
			rootNode.right = rightNode
			#rightNode.print_node()z
		return rootNode

	def convert_to_BST_n(self, nu, head):
		#import ipdb; ipdb.set_trace()
		if (nu<=0):
			return None
		left = self.convert_to_BST_n(nu/2, head)
		node = Tree(head.contents)
		head = head.next
		node.left = left
		right = self.convert_to_BST_n(nu-nu/2-1, head)
		node.right = right
		return node


if __name__ == '__main__':
	array = [5,6,7,8,9,10,20]
	ll_bst = linked_list_to_bst(array)
	#ll_bst.to_bst()
	# root = Tree(None)
	# root = ll_bst.convert_to_bst(0, 6)
	# root.print_node()
	# print root.left.data

	# now calling
	head = generate_linked_list_with_values(array)
	print_linked_list_contents(head)
	root = ll_bst.convert_to_BST_n(len(array)-1, head)
	tree_traveral = TreeTraversal()
	print "inorder : "
	tree_traveral.inorder(root)
	print "preorder : "
	tree_traveral.preorder(root)
	print "postorder : "
	tree_traveral.postorder(root)
