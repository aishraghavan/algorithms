"""
http://www.geeksforgeeks.org/kth-non-repeating-character/

----------------
Invalid cases:
----------------
two_loop_non_repeating_count called with ('geeksforgeeks', 0) => Result : Invalid input: Please check.
two_loop_non_repeating_count called with ('geeksforgeeks', 45) => Result : Invalid input: Please check.
two_loop_non_repeating_count called with (None, 45) => Result : Invalid input: Please check.
two_loop_non_repeating_count called with ('geeksforgeeks', 5) => Result : Invalid input: Please check.
----------------
Valid cases:
----------------
two_loop_non_repeating_count called with ('geeksforgeeks', 1) => Result : f
two_loop_non_repeating_count called with ('geeksforgeeks', 2) => Result : o
two_loop_non_repeating_count called with ('geeksforgeeks', 3) => Result : r
----------------
Invalid cases:
----------------
hash_map_non_repeating_count called with ('geeksforgeeks', 0) => Result : Invalid input: Please check.
hash_map_non_repeating_count called with ('geeksforgeeks', 45) => Result : Invalid input: Please check.
hash_map_non_repeating_count called with (None, 45) => Result : Invalid input: Please check.
hash_map_non_repeating_count called with ('geeksforgeeks', 5) => Result : Invalid input: Please check.
----------------
Valid cases:
----------------
hash_map_non_repeating_count called with ('geeksforgeeks', 1) => Result : f
hash_map_non_repeating_count called with ('geeksforgeeks', 2) => Result : o
hash_map_non_repeating_count called with ('geeksforgeeks', 3) => Result : r

"""
def two_loop_non_repeating_count(string, k):
    if not string or k<=0 or k>len(string):
        return "Invalid input: Please check."
    non_repeating_count = 0
    length = len(string)
    for index1 in range(length):
        if (string[index1] not in string[index1+1:]) and (string[index1] not in string[:index1]):
            non_repeating_count += 1
        if non_repeating_count == k:
            return string[index1]

    if non_repeating_count <k:
        return "Invalid input: Please check."

def hash_map_non_repeating_count(string, k):
    if not string or k<=0 or k>len(string):
        return "Invalid input: Please check."
    hash_map = {}
    length = len(string)
    non_repeated_chars = []
    for index1 in range(length):
        if string[index1] not in hash_map.keys():
            non_repeated_chars.append(string[index1])
            hash_map[string[index1]] = 1
        else:
            if string[index1] in non_repeated_chars:
                non_repeated_chars.remove(string[index1])
            hash_map[string[index1]] += 1
    if len(non_repeated_chars) <k:
        return "Invalid input: Please check."
    return non_repeated_chars[k-1]


def pretty_header_printer(string1):
    print "----------------"
    print string1
    print "----------------"

def pretty_output_printer(function_name, *custom_args):
    print "{0} called with {1} => Result : {2}".format(function_name.func_name, custom_args, function_name(*custom_args))

if __name__ == "__main__":
    string = "geeksforgeeks"
    function_names = [two_loop_non_repeating_count, hash_map_non_repeating_count]
    for function_name in function_names:
        pretty_header_printer("Invalid cases:")
        pretty_output_printer(function_name, string, 0)
        pretty_output_printer(function_name, string, 45)
        pretty_output_printer(function_name, None, 45)
        pretty_output_printer(function_name, string, 5)
        pretty_header_printer("Valid cases:")
        pretty_output_printer(function_name, string, 1)
        pretty_output_printer(function_name, string, 2)
        pretty_output_printer(function_name, string, 3)
