"""
https://leetcode.com/discuss/249/search-a-2d-matrix
"""
def search_in_matrix(matrix, element):
    if not matrix or len(matrix)==0:
        print "Nothing to print"
        return -1
    row_len = len(matrix)
    col_len = len(matrix[0])
    start = 0
    end = (row_len*col_len) - 1
    while(start<=end):
        mid = start+(end-start)/2
        if (matrix[mid/col_len][mid%row_len]== element):
            print "Found at i:{0}, j:{1}".format(mid/col_len, mid%row_len)
            return 1
        elif matrix[mid/col_len][mid%row_len]> element:
            end = mid-1
        else:
            start = mid+1
    print "not found"
    return 0

if __name__ == "__main__":
    array = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
    print search_in_matrix(array, element=5)
    print search_in_matrix(array, element=15)
    print search_in_matrix(array, element=50)
