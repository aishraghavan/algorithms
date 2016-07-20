"""
https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list

Input Format 
You have to complete the Node* Insert(Node* head, int data) method which takes two arguments - the head of the linked list and the integer to insert. You should NOT read any input from stdin/console.

Output Format 
Insert the new node at the head and return the head of the updated linked list. Do NOT print anything to stdout/console.

Sample Input

NULL , data = 1 
1 --> NULL , data = 2

Sample Output

1 --> NULL
2 --> 1 --> NULL
"""

class Node(object):
 
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

def Insert(head, data):
	temp = Node(data)
	if head != None:
		temp.next = head
	return temp


def Print_Linked_List(head):
	temp = head
	while temp!= None:
		print temp.data,
		print " --> ",
		temp = temp.next
	print "NULL"


if __name__ == "__main__":
	head1 = None
	head1 = Insert(head1, 2)
	Print_Linked_List(head1)
	head2 = Node(1)
	head2 = Insert(head2, 2)
	Print_Linked_List(head2)



