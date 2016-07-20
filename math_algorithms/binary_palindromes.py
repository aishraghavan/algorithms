"""
https://www.careercup.com/question?id=5692699114995712

Restrict to odd numbers
Assumed to be positive numbers only
"""

def print_palindromes(n):
    list_of_palindromes = []
    #check only for odd values based off on pattern
    for i in range(1, n+1, 2):
        binary= bin(i)[2:]
        if check_palindrome(binary):
            list_of_palindromes.append({i:binary})
    return list_of_palindromes

def check_palindrome(string1):
    if string1 == string1[::-1]:
        return True
    return False

if __name__ == "__main__":
    print print_palindromes(5)
    print print_palindromes(15)
    print print_palindromes(55)
    print print_palindromes(550)
