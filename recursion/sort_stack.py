"""
http://www.geeksforgeeks.org/sort-a-stack-using-recursion/
"""
from copy import deepcopy

class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def top(self):
        if self.is_empty():
            return
        return self.items[-1]

    def print_contents(self):
        temp = deepcopy(self.items)
        while (len(temp)!= 0):
            print temp.pop()

def sort_stack(stack):
    if (not stack.is_empty()):
        x = stack.pop()
        #print "x :{0}".format(x)
        sort_stack(stack)
        sort_insert_back(stack, x)
    return stack

def sort_insert_back(stack, x):
    if stack.is_empty() or x> stack.top():
        stack.push(x)
        #print "pushing back : {0} as stack.is_empty(): {1} or x> stack.top() {2} top: {3}".format(x, stack.is_empty(), x> stack.top(), stack.top())
        return
    temp = stack.pop()
    sort_insert_back(stack, x)
    stack.push(temp)

def pretty_header_printer(string1):
    print "-"*50
    print string1
    print "-"*50

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(40)
    stack.push(20)
    stack.push(50)
    pretty_header_printer("Stack contents : before sorting")
    stack.print_contents()
    s = sort_stack(stack)
    pretty_header_printer("Stack contents : after sorting")
    stack.print_contents()
