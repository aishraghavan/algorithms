def list_sum(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

def list_sum_recursion(list):
    if(len(list)==1):
        return list[0]
    else:
        return list[0] + list_sum_recursion(list[1:])

if __name__ == "__main__":
    print list_sum([2, 3, 4])
    print list_sum_recursion([2, 3, 4])
    print list_sum([])
    #print list_sum_recursion([])
