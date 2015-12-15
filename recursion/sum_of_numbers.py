def iterative_sum(array):
    sum = 0
    for element in array:
        sum += element
    return sum

def recursive_sum(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    else:
        return array[-1:][0] + recursive_sum(array[:-1])

if __name__ == "__main__":
    array = [45, 67, 89, 34, 89]
    iterative_sum = iterative_sum(array)
    print "iterative_sum : ", iterative_sum
    recursive_sum = recursive_sum(array)
    print "recursive_sum : ", recursive_sum
