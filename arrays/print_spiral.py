"""
print elements in spiral"

Something like: http://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
But reverse format assumed.
"""

def print_spriral(input):
    if not input or len(input)==0:
        print "Nothing to print"
        return -1
    row_len = len(input)
    col_len = len(input[0])
    start_row = 0
    end_row = row_len
    start_col = 0
    end_col = col_len
    while(start_col<end_col and start_row<end_row):
        for i in range(start_row, end_row):
            print "row:{0} col: {1} and printing: {2}".format(i, start_col,input[i][start_col])
        start_col += 1
        for i in range(start_col, end_col):
            print "row:{0} col: {1} and printing: {2}".format(end_col-1, i, input[end_row-1][i])
        end_row -= 1
        for i in range(end_row-1, start_row-1, -1):
            print "row:{0} col: {1} and printing: {2}".format(i, end_col-1,input[i][end_col-1])
        end_col -= 1
        for i in range(end_col-1, start_col-1, -1):
            print "row:{0} col: {1} and printing: {2}".format(start_col-1, i, input[start_col-1][i])
        start_row += 1


if __name__ == "__main__":
    array = [
        [1,12,11,10],
        [2,13,16,9],
        [3,14,15,8],
        [4,5,6,7]
        ]
    print_spriral(array)
