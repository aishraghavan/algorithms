def string_reversal_recursively(string):
    if len(string) == 0:
        return
    elif len(string) == 1:
        return string
    else:
        return string[-1:] + string_reversal_recursively(string[:-1])

if __name__ == "__main__":
    test_string = "hello"
    print "String before recursion :{0}".format(test_string)
    print "String after recursion :{0}".format(string_reversal_recursively(test_string))
