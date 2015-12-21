"""
http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

ANALYSIS OF ALGORITHM:
----------------------
Algorithm Paradigm: Backtracking
Time Complexity: O(n*n!)

"""
def swap(array,i , j):
    array[i], array[j] = array[j], array[i]
    return array

# str1 = list("hello")
# print "Before swapping :", str1
# str1 =swap(list(str1), 1, 4)
# print "After swapping :", str1

def permutations_of_string_recursion(string, left, right):
    if left == right:
        print ''.join(string)
    else:
        for i in range(left, right+1):
            string = swap(string, left, i)
            permutations_of_string_recursion(string, left+1, right)
            string = swap(string, left, i)



if __name__ == "__main__":
    string = "abc"
    permutations_of_string_recursion(list(string), 0, len(string)-1)
