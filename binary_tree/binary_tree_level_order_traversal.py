from _tree import Tree
from _queue import Queue

def level_order_traversal(node):
    if node == None:
        return
    queue1 = Queue()
    queue1.insert(node)
    while not queue1.is_empty():
        temp = queue1.remove()
        print temp,
        if temp.left:
            queue1.insert(temp.left)
        if temp.right:
            queue1.insert(temp.right)

if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    print "level order traversal :"
    level_order_traversal(root)
