"""
http://www.geeksforgeeks.org/minimum-number-of-palindromic-subsequences-to-be-removed-to-empty-a-binary-string/

Input: str[] = "10001"
Output: 1
Since the whole string is palindrome,
we need only one removal.

Input: str[] = "10001001"
Output: 2
We can remove the middle 1 as first
removal, after first removal string
becomes 1000001 which is a palindrome.


unary stings with complete 0's or complete 1's: It is a palindrome.
"""

def is_palindrome(string):
    start_index = 0
    end_index = len(string)-1
    while start_index<end_index:
        if string[start_index] != string[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True

def min_removals(string):
    if not string:
        return 0

    if is_palindrome(string):
        return 1
    return 2

print "Number of mininal removals needed to make {0} as empty sting : {1}".format("010010", min_removals("010010"))
print "Number of mininal removals needed to make {0} as empty sting : {1}".format("0100101", min_removals("0100101"))
print "Number of mininal removals needed to make {0} as empty sting : {1}".format("1111", min_removals("1111"))
print "Number of mininal removals needed to make {0} as empty sting : {1}".format("00000", min_removals("00000"))
