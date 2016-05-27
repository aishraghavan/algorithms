"""
https://www.hackerrank.com/challenges/funny-string/

2
acxz
bcxz

output:
Funny
Not Funny

"""
def funny_string(element):
    revered_str = element[::-1]
    funny_flag= False
    for i in range(0,len(element)-1):
        if abs(ord(element[i]) - ord(element[i+1])) != abs(ord(revered_str[i]) - ord(revered_str[i+1])):
            print "Not Funny"
            funny_flag = False
            break
        else:
            funny_flag = True
    if funny_flag:
        print "Funny"


def test_funny_string():
    n = int(raw_input().strip())

    array_str = []
    for i in range(n):
        string = str(raw_input().strip())
        if len(string) != 0:
            array_str.append(string)

    for element in array_str:
        funny_string(element)

test_funny_string()
