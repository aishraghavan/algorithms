from _tree import Tree

class TreeTraversal:
    def inorder(self, node):
    	if node == None:
    		return
    	self.inorder(node.left)
    	print node.data,
    	self.inorder(node.right)

    def preorder(self, node):
        if node == None:
            return
        print node.data,
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print node.data,


if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    tree_traveral = TreeTraversal()
    print "inorder : "
    tree_traveral.inorder(root)
    print "preorder : "
    tree_traveral.preorder(root)
    print "postorder : "
    tree_traveral.postorder(root)
