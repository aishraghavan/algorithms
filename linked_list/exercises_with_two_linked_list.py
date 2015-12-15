#union, intersection, membership, cardinality
"""
Input:
   List1: 10->15->4->20
   lsit2:  8->4->2->10
Output:
   Intersection List: 4->10
   Union List: 2->8->20->4->15->10
"""
from _helper_generators import generate_linked_list_with_values
from _helper_printers import print_linked_list_contents

def union(start1, start2):
    # union of two linked_list
    pass

def intersection(start1, start2):
    # intersection of two linked_list
    pass

def membership():
    # Subsets and Powersets
    pass

def cardinality(start):
    # For example, the set A = {2, 4, 6} contains 3 elements,
    # and therefore A has a cardinality of 3
    pass

#[10, 15, 4, 20]
list1 = generate_linked_list_with_values([4, 10, 15, 20])
#[8, 4, 2, 10]
list2 = generate_linked_list_with_values([2, 4, 8, 10])
print "list1: "
print_linked_list_contents(list1)
print "\nlist2: "
print_linked_list_contents(list2)
