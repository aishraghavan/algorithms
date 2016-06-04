"""
https://www.careercup.com/question?id=5695003068203008

Find if the characters of the sample string is in the same order in the text string.. Give a simple algo..
Eg.. TextString: abcNjhgAhGjhfhAljhRkhgRbhjbevfhO
Sample string :NAGARRO
"""
def sample_str_in_input_same_order(text, string):
    if not text or not string:
        return None
    prev_index = 0
    curr_index = 0
    temp_text = text
    for element in string:
        if element in temp_text:
            curr_index = temp_text.find(element)
            temp_text = temp_text[curr_index+1:]
        else:
            return False
    return True

TextString = 'abcNjhgAhGjhfhAljhRkhgRbhjbevfhO'
string  = 'NAGARRO'
print "string: {0} in TextString: {1} =>Result: {2}".format(string, TextString, sample_str_in_input_same_order(TextString, string))
string  = 'NAGGARRO'
print "string: {0} in TextString: {1} =>Result: {2}".format(string, TextString, sample_str_in_input_same_order(TextString, string))
print "string: {0} in TextString: {1} =>Result: {2}".format(None, TextString, sample_str_in_input_same_order(TextString, None))
string  = 'NAGARROOP'
print "string: {0} in TextString: {1} =>Result: {2}".format(string, TextString, sample_str_in_input_same_order(TextString, string))
string  = 'NAGZ'
print "string: {0} in TextString: {1} =>Result: {2}".format(string, TextString, sample_str_in_input_same_order(TextString, string))
