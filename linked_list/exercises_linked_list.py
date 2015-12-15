from _helper_printers import print_linked_list_contents
from _helper_generators import generate_linked_list, generate_linked_list_with_values
from _stacks import Stack

def print_linked_list_in_reverse_recursively(head):
    if (head == None):
        return ;
    print_linked_list(head.next)
    print head,

# head = generate_linked_list(6)
# print_linked_list_in_reverse_recursively(head)

def print_linked_list_recursively(start):
    if start == None:
        return
    print start,

    if(start.next != None):
        print_linked_list_recursively(start.next)

# head = generate_linked_list(6)
# print_linked_list_recursively(head)

def print_linked_list_recursively_odd_only(start):
    if start == None:
        return
    print start,

    if start.next != None:
        print_linked_list_recursively_odd_only(start.next.next)

# head = generate_linked_list(6)
# print_linked_list_recursively_odd_only(head)

def print_linked_list_recursively_even_only(start):
    if start == None:
        return
    print start.next,

    if start.next != None:
        print_linked_list_recursively_even_only(start.next.next)

# head = generate_linked_list(6)
# print_linked_list_recursively_even_only(head)

def print_linked_list_recursively_odd_only_in_reverse(start):
    if start == None:
        return

    if start.next != None:
        print_linked_list_recursively_odd_only(start.next.next)
    print start,

# head = generate_linked_list(6)
# print_linked_list_recursively_odd_only_in_reverse(head)


def print_linked_list_recursively_even_only_in_reverse(start):
    if start == None:
        return

    if start.next != None:
        print_linked_list_recursively_even_only(start.next.next)
    print start.next,

# head = generate_linked_list(6)
# print_linked_list_recursively_even_only_in_reverse(head)


def print_linked_list_in_reverse(start):
    if(start == None):
        return

    stack =  Stack()
    temp = start
    while(temp != None):
        stack.push(temp)
        temp = temp.next

    while(not stack.is_empty()):
        print stack.pop(),

# head = generate_linked_list(6)
# print_linked_list_in_reverse(head)


def move_to_front(head):
    q = None
    p = head
    if head ==  None or head.next == None:
        return head

    while(p.next != None):
        q=p
        p=p.next

    q.next= None
    p.next=head
    head=p
    return head


# head = generate_linked_list(6)
# new_head = move_to_front(head)
# print_linked_list_contents(new_head)


def rearrange_in_pairs(start):
    if not start or not start.next:
        return
    p = start
    q = start.next

    while(q):
        temp = p.contents
        p.contents = q.contents
        q.contents =  temp
        p = q.next
        q = p.next if p else None
    return start

# case 1:
# head = generate_linked_list(6)
# reverse_in_pairs = rearrange_in_pairs(head)
# print_linked_list_contents(reverse_in_pairs)
# case 2:
# reverse_in_pairs = rearrange_in_pairs(None)
# print reverse_in_pairs
# print_linked_list_contents(reverse_in_pairs)
# print "# case 3:"
# head = generate_linked_list(5)
# reverse_in_pairs = rearrange_in_pairs(head)
# print_linked_list_contents(reverse_in_pairs)


def search_in_linked_list(start, element):
    if(not start):
        return
    temp = start
    while(temp):
        if temp.contents == element:
            return True
        temp = temp.next
    return False

# array=[55, 67,34, 56, 23, 100, 110, 2]
# header = generate_linked_list_with_values(array)
# print "Searching for: {0} and the result is:{1}".format(34, search_in_linked_list(header, 34))
# print "Searching for: {0} and the result is:{1}".format(43, search_in_linked_list(header, 43))
# print "Searching for: {0} and the result is:{1}".format(43, search_in_linked_list(None, 43))


def fun(p):
    return(
        (p == None) or
        (p.next == None) or
        (p.contents <= p.next.contents and fun(p.next))
    )

head = generate_linked_list(5)
print fun(head)
print fun(None)
