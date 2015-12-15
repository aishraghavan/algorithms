"""
Longest Palindromic Substring
Brute force method: O(n^3)
http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

"""
def check_palindrome_half_way(string):
    i = 0
    j = len(string)-1
    while(i<j):
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def longest_palindromic_substring_1(string):
    if string == None:
        return None
    length_string = len(string)
    for i in range(0, length_string):
        j = length_string-i
        if i<j:
            if check_palindrome_half_way(string[i:j]):
                return string[i:j]
    return None


if __name__ == "__main__":
    print longest_palindromic_substring_1("forgeeksskeegfor")
    print longest_palindromic_substring_1("forgeeksskeegrof")
    print longest_palindromic_substring_1("forgeeks")
