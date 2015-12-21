"""
https://www.youtube.com/watch?v=YDf982Lb84o
http://www.geeksforgeeks.org/program-nth-catalan-number/

ANALYSIS OF ALGORITHM:
----------------------
Time Complexity: Time complexity of above implementation is O(n2)

Better solution:
------------------
Using Binomial Coefficient which could take O(n)
"""
def count_binary_trees_dp(n):
    if n == 0:
        return 1
    elif n == 1:
        return [1]
    binary_tree_array = [0]*n
    # Intialize array[0] = 1
    # Intialize array[1] = 1
    binary_tree_array[0] = 1
    binary_tree_array[1] = 1

    # needs to run from 2 to n
    for i in range(2, n):
        # runs from 0 to i
        for j in range(0, i):
            # most important part i-j+1
            binary_tree_array[i] += binary_tree_array[j] * binary_tree_array[i-j-1]

    return binary_tree_array

if __name__ == "__main__":
    print count_binary_trees_dp(0)
    print count_binary_trees_dp(1)
    print count_binary_trees_dp(2)
    print count_binary_trees_dp(3)
    print count_binary_trees_dp(4)
    print count_binary_trees_dp(5)
