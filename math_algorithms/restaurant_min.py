"""
https://www.hackerrank.com/challenges/restaurant

Martha is interviewing at Subway. One of the rounds of the interview requires her to cut
a bread of size lXb into smaller identical pieces such that each piece is a square having
maximum possible side length with no left over piece of bread.

TEST INPUT:
-----------
11
38 751
344 734
165 635
297 667
917 264
544 642
254 914
612 50
94 707
564 417
145 246

TEST OUTPUT:
------------
28538
63124
4191
198099
242088
87312
58039
7650
66458
26132
35670

"""
# Example 1:
# length =2, breadth =2 => return 1

# Example 2:
# length =6, breadth =9 => return 6
# case 1: 54 size 1 X 1
# case 2: 0 size 2 X 2 => there will be remaining
# case 3: 6 size 3 X 3
# case 4: 0 size 4 X 4
# case 5: 0 size 5 X 5
# case 6: 0 size 6 X 6

# SOLUTION:
# 1. Calculate gcd(l, b)
# 2. Calcuate l/gcd and b/gcd
# 3. multiply the values in step 2

# to store the length and breadth of Bread
from collections import namedtuple
Bread = namedtuple('Bread', ['length', 'breadth'])

def get_input():
    # get input value
    n = int(raw_input().strip())
    arr = []
    for i in range(n):
        temp = map(int,raw_input().strip().split(' '))
        if len(temp)==2:
            arr.append(Bread(temp[0], temp[1]))
    return arr


def calculate_gcd_rec(a, b):
    if(b == 0):
        return a
    return calculate_gcd_rec(b, a % b)

def number_of_squares_of_max_size(arr):
    min_arr = []
    for point in arr:
        # step1: calculate gcd
        gcd = calculate_gcd_rec(point.length, point.breadth)
        # step2: get quotient
        q_length = point.length/gcd
        q_breadth = point.breadth/gcd
        # step 3: return result by multiplying both
        print (q_length*q_breadth)


array = get_input()
number_of_squares_of_max_size(array)
