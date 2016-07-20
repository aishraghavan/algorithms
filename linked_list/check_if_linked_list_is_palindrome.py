from _helper_conversions import convert_array_to_linked_list, convert_linked_list_to_stack
from _helper_printers import print_linked_list_contents, print_stack_contents
from reverse_linked_list import reverse_linked_list
from compare_two_linked_list import check_if_both_linked_list_are_same
from middle_element_in_linked_list import middle_element_with_head_and_one_fast_pointer

# method 1: compare lists after reversing
def naive_palindrome_check_by_comparing_list_and_reversed_list(org_list, prev_list):
    if check_if_both_linked_list_are_same(org_list, prev_list):
        print "Palindrome"
    else:
        print "Not Palindrome"

# flop!!!!
# # method 2: find the mid point and check
# def palindrom_based_on_middle_element(head):
#     import ipdb; ipdb.set_trace()
#     mid_pt = middle_element_with_head_and_one_fast_pointer(head)
#     #check empty:
#     if not head:
#         print "List is empty"
#
#     while head and mid_pt:
#         if mid_pt.contents != head.contents:
#             print "Not palindrome"
#             return
#         head = head.next
#         mid_pt = mid_pt.next
#     print "Palindrome"
# even palindrome
###palindrom_based_on_middle_element(convert_array_to_linked_list(['f', 'g', 'e', 'e', 'g', 'f']))

# def palindrom_based_on_middle_element(head):



def method_2_using_stack(head):
    if not head:
        print "empty linked list"
        return

    print "\n# convert linked list to stack"
    stack = convert_linked_list_to_stack(head)
    print_stack_contents(stack)

    while head:
        if stack.pop() != head.contents:
            print "Not a palindrome"
            return
        head = head.next
    print "Yes palindrome"

def method_3_by_recursion():
    # to be implemented
    pass

def test_palindrome_method_1():
    list1 = convert_array_to_linked_list(['f', 'g', 'e', 'g', 'f'])
    list2 = reverse_linked_list(convert_array_to_linked_list(['f', 'g', 'e', 'g', 'f']))
    naive_palindrome_check_by_comparing_list_and_reversed_list(list1, list2)

    list3 = convert_array_to_linked_list(['a', 'g', 'e', 'd', 'f'])
    list4 = reverse_linked_list(convert_array_to_linked_list(['a', 'g', 'e', 'd', 'f']))
    naive_palindrome_check_by_comparing_list_and_reversed_list(list3, list4)

def test_palindrome_method_2():
    palindrome_head = convert_array_to_linked_list(['f', 'g', 'e', 'g', 'f'])
    method_2_using_stack(palindrome_head)

    non_palindrome_head = convert_array_to_linked_list(['a', 'g', 'e', 'd', 'f'])
    method_2_using_stack(non_palindrome_head)


if __name__ == "__main__":
    # test_palindrome_method_1()
    test_palindrome_method_2()
