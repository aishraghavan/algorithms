"""
https://www.hackerrank.com/challenges/halloween-party

base case:
n=1 => 0 chocolates
n=2 => 1 chocolate


"""
def max_chocolates(n):
    if n<=0:
        return -2
    if n == 1:
        return 0
    hash ={}
    result = 0
    for i in range(1,(n/2)+1):
        if (i not in hash.keys()) or ((n-i) not in hash.keys()):
            hash[i] = i*(n-i)
            result = hash[i]
    return result

def test_max_chocolates():
    array_int = []
    n = int(raw_input().strip())
    if n<=0:
        return
    for index in range(n):
        temp = int(raw_input().strip())
        if temp>0:
            array_int.append(temp)

    for element in array_int:
        print max_chocolates(element)

for index in range(1, 11):
    print "Max number of chocolates with {0} cuts is :{1}".format(index,max_chocolates(index))
test_max_chocolates()
