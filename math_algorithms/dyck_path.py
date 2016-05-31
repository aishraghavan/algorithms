"""
http://www.geeksforgeeks.org/dyck-path/

Input : n = 1
Output : 1

Input : n = 2
Output : 2

Input : n = 3
Output : 5

Input : n = 4
Output : 14
dyckpaths

Image Source : http://mathworld.wolfram.com/DyckPath.html

The number of Dyck paths from (n-1, 0) to (0, n-1) can be given by the Catalan numberC(n).

catalan4

"""
def calculate_catalan(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    numerator = denominator = 1
    for index in range(1, n+2):
        denominator *= index
    for index in range(n+1, 2*n+1):
        numerator *= index
    return numerator/denominator

for index in range(1,6):
    print "calculate_catalan for {0} is {1}".format(index, calculate_catalan(index))
