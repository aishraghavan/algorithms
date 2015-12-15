from _helper_generators import generate_linked_list
from linked_list_count_elements import count_no_of_elements

def check_if_both_linked_list_are_same(head1, head2):
    if not head1 or not head2:
        print "Empty linked list."
        return False

    if count_no_of_elements(head1) != count_no_of_elements(head2):
        print "Number of nodes do not match!!!"
        return False

    while head1 and head2:
        if head1.contents != head2.contents:
            print "They do not look the same. Sorry"
            return False
        head1 = head1.next
        head2 = head2.next
    print "Both are the same."
    return True

if __name__ == "__main__":
    head1 = generate_linked_list(4)
    head2 = generate_linked_list(4)
    check_if_both_linked_list_are_same(head1, head2)

    len_4 = generate_linked_list(4)
    len_5 = generate_linked_list(5)
    check_if_both_linked_list_are_same(len_4, len_5)

    check_if_both_linked_list_are_same(None, None)

    lista = generate_linked_list(4, start=2)
    listb = generate_linked_list(4, start=3)
    check_if_both_linked_list_are_same(lista, listb)
