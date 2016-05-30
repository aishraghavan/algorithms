"""

http://www.geeksforgeeks.org/length-of-the-longest-valid-substring/

Input : ((()
Output : 2
Explanation : ()

Input: )()())
Output : 4
Explanation: ()()

Input:  ()(()))))
Output: 6
Explanation:  ()(()))
"""

# same as the one in the data_structures folder
from _stack import Stack

def length_of_longest_valid_substring(string):
    #assume only contains ( and )
    if len(string) == 0:
        return
    stack = Stack()
    length = 0
    for element in string:
        if element == '(':
            stack.push('(')
        elif element == ')':
            if not stack.is_empty():
                stack.pop()
                length +=2
    return length

print "length_of_longest_valid_substring of {0} is {1}".format('((()', length_of_longest_valid_substring('((()'))
print "length_of_longest_valid_substring of {0} is {1}".format(')()())', length_of_longest_valid_substring(')()())'))
print "length_of_longest_valid_substring of {0} is {1}".format('()(()))))', length_of_longest_valid_substring('()(()))))'))
