def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1)

if __name__ == "__main__":
    for i in range(6):
        print "factorial of {0} = {1}".format(i, factorial(i))
