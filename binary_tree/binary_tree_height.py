from _queue import Queue
from tree_helpers import sample_tree

def height_of_tree(head):
    if head == None:
        return 0
    queue = Queue()
    queue.insert(head)
    height = 0

    while(1):
        children_count = queue.size()
        if children_count == 0:
            return height
        else:
            height += 1

        while(children_count>0):
            node = queue.remove()
            if node.left:
                queue.insert(node.left)
            if node.right:
                queue.insert(node.right)
            children_count -= 1

if __name__ == "__main__":
    root = sample_tree()
    print height_of_tree(root)
