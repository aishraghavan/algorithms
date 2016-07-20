"""
https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list

Input Format 
You have to complete the Node* Insert(Node* head, int data) method. It takes two arguments: the head of the linked list and the integer to insert. You should not read any input from the stdin/console.

Output Format 
Insert the new node at the tail and just return the head of the updated linked list. Do not print anything to stdout/console.

Sample Input

NULL, data =  2
 2--> NULL, data = 3

Sample Output

2 -->NULL
2 --> 3 --> NULL
"""

class Node(object):
 
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node
 


def Insert(head, data):
	if head == None:
		return Node(data)
	temp = head
	while temp.next!= None:
		temp = temp.next
	temp.next = Node(data)
	return head


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
	head2 = Node(2)
	head2 = Insert(head2, 3)
	Print_Linked_List(head2)



