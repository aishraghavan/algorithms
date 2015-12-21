"""
https://www.hackerrank.com/challenges/minimum-draws
"""
n = int(raw_input().strip())
arr = []
for i in range(n):
    arr.append(int(raw_input().strip()))

for element in arr:
    print "{0}".format(element+1)
