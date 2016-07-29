"""
Longest Palindromic Substring
Brute force method: O(n^3)
http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

"""
def is_palindrome(string):
    i = 0
    j = len(string)-1
    while(i<j):
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def longest_palindromic_substring_possible(string):
    if string == None:
        return None
    length_string = len(string)
    for i in range(0, length_string):
        j = length_string-i
        if i<j:
            if is_palindrome(string[i:j]):
                return string[i:j]
    return None

def longest_palindromic_substring_possible_better(string):
    if string == None:
        return None
    length_string = len(string)
    # 6,5,4,3
    for index1 in range(length_string, 0, -1): # length of substring
        for index2 in range(0, len(string)-index1+1):
            temp_str = string[index2:index2+index1]
            if is_plaindrome(temp_str):
                return temp_str
    return None


def format_and_print(string):
    print "-----------------"
    print "Input string: {0} \nlongest_palindrome possible is: {1} \nlongest_palindromic_substring_possible_better: {2}".format(
                string, 
                longest_palindromic_substring_possible(string),
                longest_palindromic_substring_possible_better(string))
    print "-----------------"

if __name__ == "__main__":
    strings = ["forgeeksskeegfor",
                "forgeeksskeegrof",
                "forgeeks"]
    for string in strings:
        format_and_print(string)
 
"""
example = "abcdcba"
length 7
abcdcba start: 0 end: 6

length 6
abcdcb start: 0 end: 5
bcdcba start: 1 end: 6
length 5
abcdc start: 0 end: 4
bcdcb start: 1 end: 5
cdcba start: 2 end: 6
...
...
...
"""




