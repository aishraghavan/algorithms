from copy import deepcopy
from _linked_list import Node


def linked_list_insert(head, data):
    if head == None:
        head = Node(data)
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)
    return head



if __name__ == "__main__":
    head = None
    head = linked_list_insert(head, 4)
    head = linked_list_insert(head, 5)
    head = linked_list_insert(head, 6)
