#http://www.programcreek.com/2013/01/leetcode-remove-duplicates-from-sorted-list/
from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents

def remove_duplicates(node):
    if node == None:
        return
    curr = node
    next = node.next
    print "\ncontents :"
    while next != None:
        if next.contents == curr.contents:
            curr.next = next.next
            next = next.next
        else:
            curr = next
            next = next.next
        print curr, next

def remove_duplicates_with_one_node(node):
    if node == None:
        return
    curr = node
    while curr != None and curr.next != None:
        if curr.contents == curr.next.contents:
            curr.next =  curr.next.next
        else:
            curr = curr.next


if __name__ == "__main__":
    array = [1, 1, 1, 2, 3, 4, 4]
    head = generate_linked_list_with_values(array)
    print_linked_list_contents(head)
    # remove_duplicates(head)
    # print "linked list contents: "
    # print_linked_list_contents(head)

    remove_duplicates_with_one_node(head)
    print "linked list contents: "
    print_linked_list_contents(head)
