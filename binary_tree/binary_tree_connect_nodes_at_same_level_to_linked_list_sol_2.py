"""
binary_tree_connect_nodes_at_same_level_to_linked_list_sol_2
http://www.geeksforgeeks.org/connect-nodes-at-same-level/
"""
from _queue import Queue

#------------- LINKED LIST ------------------
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def insert_in_linked_list(head, data):
    if head == None:
        return Node(data)
    temp = head
    while temp.next!= None:
        temp = temp.next
    temp.next = Node(data)
    return head

def print_linked_list(head):
    temp = head
    while temp!= None:
        print temp.data,
        print " --> ",
        temp = temp.next
    print "NULL"

#----------- MODIFIED TREE ---------------------
class ModifiedTree(object):
	def __init__(self, data, left=None, right=None, next_right=None):
		self.data = data
		self.left = left
		self.right = right
		self.next_right = next_right

	def print_node(self):
		print self.data, 
		print self.left.data if self.left else None,
		print self.right.data if self.right else None,
		print self.next_right.data if self.next_right else None

	def __str__(self):
		return str(self.data)

def convert_to_modified_tree(root):
	print "calling", root
	if not root:
		return

	if  root.left:
		print "before left", root.left.print_node()
		root.left.next_right = root.right
		#print root.left, root.left.next_right
		print "left", root.print_node()

	if  root.right:
		root.right.next_right = root.next_right.left if root.next_right else None
		print "right", root.print_node()

	convert_to_modified_tree(root.left)
	convert_to_modified_tree(root.right)

#------------- HELPER PRINTERS---------------------
def level_order_traversal(node):
    if node == None:
        return
    queue1 = Queue()
    queue1.insert(node)
    while not queue1.is_empty():
        temp = queue1.remove()
        #print temp,type(temp)
        temp.print_node()
        if temp.left:
            queue1.insert(temp.left)
        if temp.right:
            queue1.insert(temp.right)


def example_balanced_modified_tree():
	n8= ModifiedTree(8)
	n9= ModifiedTree(9)
	n4= ModifiedTree(4, n8,n9)
	n5= ModifiedTree(5)
	n2= ModifiedTree(2, n4, n5)
	n6= ModifiedTree(6)
	n7= ModifiedTree(7)
	n3= ModifiedTree(3, n6, n7)
	root= ModifiedTree(1, n2, n3)
	return root

if __name__ == "__main__":
    root = example_balanced_modified_tree()
    #print root
    level_order_traversal(root)
    #binary_tree_connect_nodes_at_same_level_to_linked_list(root)
    root = convert_to_modified_tree(root)
    level_order_traversal(root)