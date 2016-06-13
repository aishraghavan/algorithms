"""
https://www.careercup.com/question?id=5729332770111488

Write all jumbled number which is >0 && <N, where N is provided by the user.
A jumbled number is a number whose neighbour digit (either left or right) max differ by 1 value.

e.g.:
8987 is a jumbled number.
13 is not a jumbled number.
123456 is a jumbled number.
287 is not jumbled number.
"""
def generate_jumbled_numbers(number):
    jumbled_numbers = []
    if number <0:
        return jumbled_numbers
    for element in range(number):
        if is_jumbled_number(element): jumbled_numbers.append(element)
    return jumbled_numbers

def is_jumbled_number(number):
    if number <0:
        return False

    str_num = str(number)
    # For loop wont work for two digit number. Hence, this is made separate.
    if len(str_num) == 2:
        if abs(int(str_num[1])-int(str_num[0])) != 1:
            return False
    for index in range(1, len(str_num)-1):
        before_index = index - 1
        after_index =  index + 1
        if (abs(int(str_num[before_index])-int(str_num[index])) != 1 or
            abs(int(str_num[before_index])-int(str_num[index])) != 1):
            return False
    return True

def pretty_header_printer(string1):
    print "-"*50
    print string1
    print "-"*50

def pretty_output_printer(function_name, *custom_args):
    func_call = function_name(custom_args[0])
    print "{0} called with {1} => Result: {2} =>Assertion: {3}".format(
                function_name.func_name, custom_args[0],
                func_call, assert_statement(func_call, custom_args[1]) if len(custom_args) ==2 else None)

def assert_statement(output, expected_output):
    return "Pass" if output == expected_output else "Fail"

if __name__ == "__main__":
    pretty_header_printer(" Testing Jumbled Number")
    function_name = is_jumbled_number
    pretty_output_printer(function_name, 0, True)
    pretty_output_printer(function_name, 123, True)
    pretty_output_printer(function_name, 13, False)
    pretty_output_printer(function_name, 123456, True)
    pretty_output_printer(function_name, 287, False)
    pretty_output_printer(generate_jumbled_numbers, 30)
