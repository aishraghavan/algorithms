from _helper_printers import print_linked_list_contents

class Node:
    def __init__(self, contents=None, next=None):
        self.contents = contents
        self.next  = next

    def getContents(self):
        return self.contents

    def __str__(self):
        return str(self.contents)

class LinkedList:
    def __init__(self, head=None):
        self.head = head

def get_linked_list(length):
    head = Node()
    temp_node = head
    for i in xrange(1, length+1):
        node = Node(i)
        temp_node.next = node
        temp_node = temp_node.next
    head =  head.next
    print_linked_list_contents(head)
    return head


def testList():
    node1 = Node("car")
    node2 = Node("bus")
    node3 = Node("lorry")
    node1.next = node2
    node2.next = node3
    print_linked_list_contents(node1)

def testEmptyList():
    node1 = Node()
    print_linked_list_contents(node1)


if __name__ == '__main__':
    testList()
    testEmptyList()
