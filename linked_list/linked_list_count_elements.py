from _linked_list import Node, get_linked_list

def count_no_of_elements(head):
    count = 0
    while(head):
        count += 1
        head = head.next

    return count

if __name__ == "__main__":
    head = get_linked_list(6)
    print "Count # of nodes: {0}".format(count_no_of_elements(head))
