from _linked_list import Node
from _helper_generators import generate_linked_list_with_values
from linked_list_insert import linked_list_insert
from linked_list_count_elements import count_no_of_elements
from _helper_printers import print_linked_list_contents

# Note the numbers are in the reverse direction. so add additional zeros at the end.
# if other way, add zeros in the front.

def add_two_numbers(number1, number2):
    if number1 == None or number2 == None:
        return
    added_sum = None
    carry = 0
    #make it same size
    number1, number2 = check_length_and_alter(number1, number2)


    # same size
    while number1 != None and number2 != None:

        sum = number1.contents + number2.contents + carry
        carry = 0

        if sum >= 10:
            carry += 1
            sum = sum%10
        added_sum = linked_list_insert(added_sum, sum)
        #print "number1: {0}, number2: {1}, add: {2}, node: {3}".format(number1, number2, sum, added_sum)
        # if carry>0:
        #     print "carry : ", carry
        number1 = number1.next
        number2 = number2.next
    return added_sum

def check_length_and_alter(number1, number2):
    #check for size
    length1 = count_no_of_elements(number1)
    length2 = count_no_of_elements(number2)
    if length1 != length2:
        diff = abs(length1-length2)
        if length1> length2:
            #number2 = insert_in_front(number2, diff)
            for i in range(diff):
                number2 = linked_list_insert(number2, 0)
        else:
            #number1 = insert_in_front(number1, diff)
            for i in range(diff):
                number1 = linked_list_insert(number1, 0)
    return number1, number2

def insert_in_front(head, diff):
    # insert extra nodes of zero in the front
    if head == None:
        return
    for i in range(diff):
        temp = Node(0)
        temp.next = head
        head = temp
    return head


if __name__ == "__main__":
    # same size
    number1 = generate_linked_list_with_values([2, 4, 3])
    number2 = generate_linked_list_with_values([5, 6, 4])
    added_sum = add_two_numbers(number1, number2)
    print_linked_list_contents(added_sum)

    #different size
    diff_size_number1 = generate_linked_list_with_values([1, 2, 4, 3])
    diff_size_number2 = generate_linked_list_with_values([6, 1, 4])
    diff_size_added_sum = add_two_numbers(diff_size_number1, diff_size_number2)
    print_linked_list_contents(diff_size_added_sum)


    # test insert_in_front
    # number1 = generate_linked_list_with_values([2, 4, 3])
    # head = insert_in_front(number1, 1)
