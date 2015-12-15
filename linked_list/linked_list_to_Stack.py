from _linked_list import Node
from _helper_printers import print_linked_list_contents

def insert_in_front(value, head):
  temp = Node(value)
  #if list is empty
  if head != None:
    temp.next = head
  return temp

def delete_in_front(head):
    if head == None:
      return None
    temp = head.next
    print "deleting :", head
    del head
    return temp # new head


node1 = insert_in_front(10, None)
node2 = insert_in_front(20, node1)
print_linked_list_contents(node2)
print "Stack contents:"
head = delete_in_front(node2)
print delete_in_front(head)
