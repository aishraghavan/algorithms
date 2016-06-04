"""
https://www.careercup.com/question?id=5921450319937536

Given an array of both positive and negative integers , find all pairs whose sum is equal to zero.
output:
For input: [-2, 0, 2, 3, 5, 5], output:[Pair(negative=-2, positive=2)], better_sol:[Pair(negative=-2, positive=2)]
For input: [-2, 0, 3, 3, 5, 5], output:None, better_sol:None
For input: [-2, -3, 0, 3, 3, 5, 5, 2], output:[Pair(negative=-3, positive=3), Pair(negative=-2, positive=2)], better_sol:[Pair(negative=-3, positive=3), Pair(negative=-2, positive=2)]
"""
from sets import Set
from collections import namedtuple

Pair = namedtuple('Pair', ['negative', 'positive'])
def oppositePairs(input):
    if len(input) == 0:
        return None
    input = remove_duplicates_and_sorted(input)
    #print "input :{0}".format(input)
    i = 0
    end = len(input)-1
    output = []
    while i< len(input):
        for j in range( i+1, len(input)):
            if (input[i]+input[j] == 0):
                output.append(Pair(input[i], input[j]))
                break
        i = i+1
    if len(output) == 0:
        return None
    return output

def oppositePairs_better_sol(input):
    if len(input) == 0:
        return None
    input = remove_duplicates_and_sorted(input)
    #print "input :{0}".format(input)
    output = []
    for element in input:
        if element < 0 and -(element) in input:
            output.append(Pair(element, -element))
        elif element >0:
            break
    if len(output) == 0:
        return None
    return output

def remove_duplicates_and_sorted(input):
    return sorted(list(Set(input)))

input1 = [-2,0,2,3,5,5]
print "For input: {0}, output:{1}, better_sol:{2}".format(input1, oppositePairs(input1), oppositePairs_better_sol(input1))
input2 = [-2,0,3,3,5,5]
print "For input: {0}, output:{1}, better_sol:{2}".format(input2, oppositePairs(input2), oppositePairs_better_sol(input2))
input3 = [-2,-3,0,3,3,5,5,2]
print "For input: {0}, output:{1}, better_sol:{2}".format(input3, oppositePairs(input3), oppositePairs_better_sol(input3))
