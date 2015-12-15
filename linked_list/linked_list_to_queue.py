from _linked_list import Node
from _helper_printers import print_linked_list_contents

def insert_in_end(value, head):
  temp = head
  #if list is empty
  if head == None:
      return Node(value)
  while temp.next != None:
      temp = temp.next
  temp.next = Node(value)
  return head

def delete_from_front(head):
    if head == None:
        return
    temp = head.next
    print "deleting :",head
    del head
    return temp

node1 = insert_in_end(10, None)
node2 = insert_in_end(20, node1)
node3 = insert_in_end(30, node2)
print_linked_list_contents(node3)
node2 = delete_from_front(node3)
node1 = delete_from_front(node2)
node = delete_from_front(node1)
