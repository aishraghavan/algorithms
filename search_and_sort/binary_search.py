def binary_search(array, start, end, search):
    if not array or not search:
        return -1
    if start<end:
        mid = start + (end-start)/2
        if array[mid] == search:
            return mid
        elif array[mid] > search:
            return binary_search(array, start, mid,search)
        else:
            return binary_search(array, mid+1, end, search)
    return -1

def first_binary_search(array, start, end, search):
    if not array or not search:
        return -1
    if start == end and array[start] == search:
        return start
    if start<end:
        mid = start + (end-start)/2
        if mid == 0 or (array[mid] == search and array[mid-1] < search):
            return mid
        elif (array[mid] == search and array[mid-1] <= search):
            return first_binary_search(array, start, mid-1,search)
        elif array[mid] > search:
            return first_binary_search(array, start, mid-1,search)
        else:
            return first_binary_search(array, mid+1, end, search)
    return -1

def last_binary_search(array, start, end, search):
    if not array or not search:
        return -1
    if start == end and array[end] == search:
        return end
    if start<end:
        mid = start + (end-start)/2
        if mid == len(array)-1 or (array[mid] == search and array[mid+1] > search):
            return mid
        elif (array[mid] == search and array[mid+1] >= search):
            return last_binary_search(array, mid+1, end,search)
        elif array[mid] > search:
            return last_binary_search(array, start, mid-1,search)
        else:
            return last_binary_search(array, mid+1, end, search)
    return -1

def find_first_last(array, start, end, search):
    binary_result = binary_search(array, start, end, search)
    if binary_result == -1:
        return -1,-1
    first = -1
    for i in range(start, binary_result+1):
        if array[i] == search:
            first = i
            break

    last = -1
    for i in range(len(array)-1, binary_result-1, -1):
        if array[i] == search:
            last = i
            break
    return first, last


def format_and_print(array, search):
    print "Searching for {0} : {1}".format(search, binary_search(array, 0, len(array)-1, search))
    first, last = find_first_last(array, 0, len(array)-1, search)
    print "Calling to get first: {0} and last: {1}".format(first, last)

if __name__ == "__main__":
    repeated_array = [10, 10, 20, 20, 20, 20, 30, 40, 40, 40]
    print "input array : "
    for i in range(len(repeated_array)):
        print i, repeated_array[i]
    print "40 : {0}".format(first_binary_search(repeated_array, 0, len(repeated_array)-1, 40))
    print "10 : {0}".format(first_binary_search(repeated_array, 0, len(repeated_array)-1, 10))
    print "30 : {0}".format(first_binary_search(repeated_array, 0, len(repeated_array)-1, 30))
    print "20 : {0}".format(first_binary_search(repeated_array, 0, len(repeated_array)-1, 20))
    print "50 : {0}".format(first_binary_search(repeated_array, 0, len(repeated_array)-1, 50))
    print "5 : {0}".format(first_binary_search(repeated_array, 0, len(repeated_array)-1, 5))
    print "--------------"
    print "calling last_binary_search"
    print "40 : {0}".format(last_binary_search(repeated_array, 0, len(repeated_array)-1, 40))
    print "10 : {0}".format(last_binary_search(repeated_array, 0, len(repeated_array)-1, 10))
    print "30 : {0}".format(last_binary_search(repeated_array, 0, len(repeated_array)-1, 30))
    print "20 : {0}".format(last_binary_search(repeated_array, 0, len(repeated_array)-1, 20))
    print "50 : {0}".format(last_binary_search(repeated_array, 0, len(repeated_array)-1, 50))
    print "5 : {0}".format(last_binary_search(repeated_array, 0, len(repeated_array)-1, 5))
"""
if __name__ == "__main__":
    # array = [10,20,30,45,67]
    # format_and_print(array, 20)
    # format_and_print(array, 45)
    # format_and_print(array, 54)
    print "Repeated elements"
    repeated_array = [10,10,10,20,30,40,40]
    #format_and_print(repeated_array, 20)
    format_and_print(repeated_array, 10)

    # format_and_print(repeated_array, 40)
    # #print "Searching for {0} : {1}".format(20, binary_search_repeated(repeated_array, 0, len(repeated_array)-1, 20))
    # # print "Searching for {0} : {1}".format(10, binary_search_repeated(repeated_array, 0, len(repeated_array)-1, 10))
    # # print "Searching for {0} : {1}".format(10, binary_search(repeated_array, 0, len(repeated_array)-1, 10))
    
    # # first, last = find_first_last(repeated_array, 0, len(repeated_array)-1, 10)
    # # print first, last
    # first, last = find_first_last(repeated_array, 0, len(repeated_array)-1, 20)
    # print first, last
"""
