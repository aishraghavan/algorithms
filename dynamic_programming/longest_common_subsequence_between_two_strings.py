"""
https://www.youtube.com/watch?v=NnD96abizww
https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/LongestCommonSubsequence.java
http://www.geeksforgeeks.org/longest-common-substring/

ANALYSIS OF ALGORITHM:
----------------------
m  => length of first string
n  => length of second string
* Solved using DP
* Time complexity: O(m*n)
* Space complexity: O(m*n)

Can be solved sing suffix trees = O(m+n)
"""
def longest_common_subsequence_between_two_strings_dp(string1, string2):
    if string1 == None or string2 == None:
        return -1

    #note: mark this properly, else lead to index not found
    len_col = len(string1)
    len_row = len(string2)
    common_matrix =[[0] * (len_col+1)] * (len_row+1)

    # goal is to return the maximum value in the array
    maximum_value = 0
    for i in range(1, (len_row+1)):
        for j in range(1, (len_col+1)):
            # if row_header == col_header, increment diagonal value by 1
            if string2[i-1] == string1[j-1]:
                common_matrix[i][j] = 1 + common_matrix[i-1][j-1]
            # else set to the maximum value of the neighbours
            else:
                common_matrix[i][j] = max(common_matrix[i-1][j], common_matrix[i][j-1])

            # set maximum_value
            if common_matrix[i][j] > maximum_value:
                maximum_value = common_matrix[i][j]

    return maximum_value

if __name__ == "__main__":
    print longest_common_subsequence_between_two_strings_dp("abcdaf", "acbcf")
    print longest_common_subsequence_between_two_strings_dp("ABCDGHLQR", "AEDPHR")
    #Returns 14
    print longest_common_subsequence_between_two_strings_dp("OldSite:GeeksforGeeks.org", "NewSite:GeeksQuiz.com")
