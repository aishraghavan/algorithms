from tree_helpers import sample_tree, example_unbalanced_tree, example_balanced_tree
from _queue import Queue

class Solution(object):
    def binary_tree_count_leaves_old(self, root):
        if not root:
            return 0

        queue = Queue()
        queue.insert(root)
        leaf_count = 0
        
        while queue.size()>0:
            node = queue.remove()
            if self.is_leaf(node):
                leaf_count +=1
            if node.left:
                queue.insert(node.left)
            if node.right:
                queue.insert(node.right)
        return leaf_count

    def binary_tree_count_leaves(self, root):
        if not root:
            return 0

        list_nodes = []
        list_nodes.append(root)
        leaf_count = 0
        
        while len(list_nodes)>0:
            node = list_nodes.pop()
            if self.is_leaf(node):
                leaf_count +=1
            if node.left:
                list_nodes.append(node.left)
            if node.right:
                list_nodes.append(node.right)
        return leaf_count

    def is_leaf(self, node):
        if (node.left == None and node.right == None):
            return True
        return False

def print_format(root):
    sol = Solution()
    print "--------------"
    print "root: {0}".format(root)
    print "Number of leaf nodes: {0}".format(sol.binary_tree_count_leaves(root))
    print "--------------"

if __name__ == "__main__":
    unbalanced_root =  example_unbalanced_tree()
    print_format(unbalanced_root)
    balanced_root = example_balanced_tree()
    print_format(balanced_root)