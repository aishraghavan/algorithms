"""
http://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/

Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.
Only subsequence "abc" is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"
"""
from collections import namedtuple
Testcase = namedtuple('Testcase', ['input', 'expected_output'])


def spl_reverse_string(string):
    if not string or len(string) == 0:
        return -1

    start = 0
    end = len(string)-1
    list_string = list(string)
    while(start<end):
        while not list_string[start].isalpha():
            start +=1
        while not list_string[end].isalpha():
            end -=1
        if start< len(string) and end>=0:
            list_string[start], list_string[end] = list_string[end], list_string[start]
        start +=1
        end -= 1
    output = "".join(list_string)
    print "string: {0} and reversed string: {1}".format(string, output)
    return output


def test_spl_reverse_string(input, expected_output):
    output = spl_reverse_string(input)
    print "pass" if output == expected_output else "fail"


spl_reverse_string("a,b$c")
spl_reverse_string("Ab,c,de!$")
spl_reverse_string("a!!!b.c.d,e'f,ghi")

print "--------------------"
print "running test cases"
print "--------------------"
Testcases = []
Testcases.append(Testcase("a,b$c", "c,b$a"))
Testcases.append(Testcase("Ab,c,de!$", "ed,c,bA!$"))
Testcases.append(Testcase("a!!!b.c.d,e'f,ghi", "i!!!h.g.f,e'd,cba"))
for test in Testcases:
    test_spl_reverse_string(test.input, test.expected_output)
