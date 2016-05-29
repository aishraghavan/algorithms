"""
http://www.geeksforgeeks.org/print-concatenation-of-zig-zag-string-form-in-n-rows/

Input: str = "ABCDEFGH"
       n = 2
Output: "ACEGBDFH"
Explanation: Let us write input string in Zig-Zag fashion
             in 2 rows.
A   C   E   G
  B   D   F   H
Now concatenate the two rows and ignore spaces
in every row. We get "ACEGBDFH"

Input: str = "GEEKSFORGEEKS"
       n = 3
Output: GSGSEKFREKEOE
Explanation: Let us write input string in Zig-Zag fashion
             in 3 rows.
G       S       G       S
  E   K   F   R   E   K
    E       O       E
Now concatenate the two rows and ignore spaces
in every row. We get "GSGSEKFREKEOE"

"""
class InputError(Exception):
    def __init__(self, message):
        self.message = message

def _error_checking(string, n):
    if not string:
        raise InputError("Empty string")
    if n> len(string):
        raise InputError("N is greater than string")
    return


def print_zig_zag_simple(string, n):
    _error_checking(string, n)

    row_list = [[] for _ in range(n)]

    direction = "down"
    row = 0
    for index in range(len(string)):
        row_list[row].append(string[index])
        # check direction
        if direction == "down":
            row += 1
        elif direction == "up":
            row -= 1

        # reverse the direcion
        if row == 0:
            direction = "down"
        if  row == n-1:
            direction = "up"

    # just for testing
    #print row_list
    str = ""
    for row in row_list:
        temp = "".join(row)
        str += temp
    print str


def print_zig_zag_efficient(string, n):
    _error_checking(string, n)

    row_list = ["" for _ in range(n)]
    direction = "down"
    row = 0
    for index in range(len(string)):
        row_list[row] += string[index]
        # check direction
        if direction == "down":
            row += 1
        elif direction == "up":
            row -= 1

        # reverse the direcion
        if row == 0:
            direction = "down"
        if  row == n-1:
            direction = "up"

    zig_zag_sting = "".join(row_list)
    print zig_zag_sting


print_zig_zag_simple("GEEKSFORGEEKS", 3)
# Error checking
#print_zig_zag_simple("", 3)

print_zig_zag_efficient("GEEKSFORGEEKS", 3)
