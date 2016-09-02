# coding: utf-8
"""
http://codeforces.com/problemset/problem/327/A

Answer: http://codeforces.com/blog/entry/19070

Iahub got bored, so he invented a game to be played on paper.

He writes n integers a1, a2, ..., an. Each of those integers can be either 0 or 1.
He's allowed to do exactly one move: he chooses two indices i and j (1 <= i <= j <= n)
and flips all values ak for which their positions are in range [i, j] (that is i <= k <= j).
Flip the value of x means to apply operation x = 1 - x.

The goal of the game is that after exactly one move to obtain the maximum number
 of ones. Write a program to solve the little game of Iahub.

Input
The first line of the input contains an integer n (1 <= n <= 100). In the second line
of the input there are n integers: a1, a2, ..., an.
It is guaranteed that each of those n values is either 0 or 1.

Output
Print an integer — the maximal number of 1s that can be obtained after exactly one move.

Examples
input
5
1 0 0 1 0
output
4
input
4
1 0 0 1
output
4
Note
In the first case, flip the segment from 2 to 5 (i = 2, j = 5).
That flip changes the sequence, it becomes: [1 1 1 0 1]. So, it contains four ones.
There is no way to make the whole sequence equal to [1 1 1 1 1].

In the second case, flipping only the second and the third element (i = 2, j = 3)
will turn all numbers into 1.

"""

def flip_coins_half(array):
    #fails when [1,1,1]
    len_array = len(array)
    dp_array = [0]* len_array

    #intialize
    dp_array[0]=1
    for i in range(1, len_array):
        if array[i] == 0:
            dp_array[i] = dp_array[i-1] + 1
        else:
            dp_array[i] = dp_array[i-1]

    #return dp_array
    return dp_array[len_array-1]

def flip_coins(array):
    #Logic: max (total_1s + max (number_of_0s_in_subarray))
    len_array = len(array)
    dp_array = [0]* len_array

    count_ones = 0
    #zero_to_one_count = 0
    #intialize
    dp_array[0]=1 if array[0]==1 else 0
    for i in range(0, len_array):
        if array[i] == 0:
            dp_array[i] = dp_array[i-1] + 1
            #zero_to_one_count += 1
        else:
            dp_array[i] = dp_array[i-1]
            count_ones += 1

    #return dp_array
    #print "count_ones : ", count_ones, "dp_array[len_array-1] : ",dp_array[len_array-1]
    return max(count_ones,dp_array[len_array-1])

def format_and_print(array):
    print "Calling flip_coins_half(array) with : {0}, Result : {1}".format(array, flip_coins_half(array))
    print "Calling flip_coins(array) with : {0}, Result : {1}".format(array, flip_coins(array))

if __name__ == "__main__":
    format_and_print([1,0,0,1,0])
    format_and_print([0,1,0,1,0])
    format_and_print([1,1,1])
    format_and_print([0,0,0,0])
