"""
http://www.geeksforgeeks.org/connect-nodes-at-same-level/
"""
from tree_helpers import example_balanced_tree
from _queue import Queue

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


def binary_tree_connect_nodes_at_same_level_to_linked_list(node):
    if node == None:
        return
    queue1 = Queue()
    queue1.insert(node)
    linked_list = None
    node_count = 1
    temp_list = []
    while not queue1.is_empty():
        node_count = queue1.size()
        temp = queue1.remove()
        linked_list = insert_in_linked_list(linked_list, temp)
        node_count -= 1
        if temp.left:
            temp_list.append(temp.left)
        if temp.right:
            temp_list.append(temp.right)
        if node_count == 0:
            print_linked_list(linked_list)
            for e in temp_list:
                queue1.insert(e)
            temp_list = []
            linked_list = None


if __name__ == "__main__":
    root = example_balanced_tree()
    binary_tree_connect_nodes_at_same_level_to_linked_list(root)