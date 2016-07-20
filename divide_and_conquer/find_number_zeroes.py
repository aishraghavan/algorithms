"""
http://www.geeksforgeeks.org/find-number-zeroes/
"""
def find_number_zeroes_linear_search(array):
    if not array or len(array) == 0:
        return -1
    length = len(array)
    for i in range(length):
        if array[i] ==0:
            break
    return length-i

def find_number_zeroes_binary_search(array):
    zero_index = binary_search(array)
    return len(array)-zero_index

def binary_search(array):
    start = 0
    end = len(array)-1
    while (start<=end):
        mid = (start+end)/2
        if (( mid == 0 or array[mid-1] == 1) and array[mid] == 0):
            return mid
 
        if (array[mid] == 1):  # If mid element is not 0
            #return firstZero(arr, (mid + 1), high);
            start = mid + 1
        else:  # If mid element is 0, but not first 0
            #return firstZero(arr, low, (mid -1));
            end = mid -1
    return -1


def format_and_print_output(array):
    print "Input array: {0}".format(array)
    print "Calling find_number_zeroes_linear_search : {0}".format(find_number_zeroes_linear_search(array))
    print "Calling find_number_zeroes_binary_search : {0}".format(find_number_zeroes_binary_search(array))


if __name__ == "__main__":
    array1 = [1,1,1,1,0,0] 
    format_and_print_output(array1)
    array2 = [1,0,0,0]
    format_and_print_output(array2)
    array3 = [0,0,0]
    format_and_print_output(array3)
    array4 = [1,1,1,1]
    format_and_print_output(array4)

