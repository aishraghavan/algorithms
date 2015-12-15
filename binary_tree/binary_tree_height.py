from _tree import Tree
from _queue import Queue

def height_of_tree(head):
    if head == None:
        return
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

n1= Tree(4)
n2= Tree(5)
n3= Tree(2, n1, n2)
n4= Tree(3)
root = Tree(1, n3, n4)
print height_of_tree(root)
