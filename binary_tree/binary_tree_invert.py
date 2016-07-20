from _queue import Queue
from tree_helpers import sample_tree
from binary_tree_in_order_traversal import in_order_iterative

def binary_tree_invert(root):
    if not root:
        return 
    queue = Queue()
    queue.insert(root)

    while not queue.is_empty():
        temp = queue.remove()
        if temp.left:
            queue.insert(temp.left)
        if temp.right:
            queue.insert(temp.right)

        transfer = temp.left
        temp.left = temp.right
        temp.right = transfer

    return root

if __name__ == "__main__":
    root = sample_tree()
    print "Before the inversion" 
    in_order_iterative(root)
    binary_tree_invert(root)
    print "After the inversion" 
    in_order_iterative(root)
