def gcd(a, b):
    #assume a>b
    # if (b == 0):
    #     return a
    while(b != 0):
        r = a%b
        a = b
        b = r
    return a

    # if m == 0 or n == 0:
    #     return 0
    # if m == 1 or n ==1:
    #     return 1

def calculate_gcd_rec(a, b):
    if(b == 0):
        return a
    return calculate_gcd_rec(b, a % b)

if __name__ == "__main__":
    print "recursive: "
    print "calculate_gcd_rec(20, 4) : ", calculate_gcd_rec(20, 4)
    print "calculate_gcd_rec(20, 17) : ", calculate_gcd_rec(20, 17)
    print "iterative: "
    print "gcd(20, 4) : ", gcd(20, 4)
    print "gcd(20, 17) : ", gcd(20, 17)
