def fibonacci_series(n):
    n1=0
    n2=1
    sum = 0
    for i in range(n):
        n3 = n1+n2
        sum += n3
        print n3,
        n1=n2
        n2=n3
    print "sum : ",sum

def fibonacci_series_recursively(n):
    if n==0 or n==1:
        return n
    return fibonacci_series_recursively(n-1)+ fibonacci_series_recursively(n-2)

def print_fibonacci_series_recursively(n):
    for i in range(n):
        print fibonacci_series_recursively(i),

fibonacci_series(10)
#print fibonacci_series_recursively(10)
print_fibonacci_series_recursively(10)
