"""
https://www.hackerrank.com/challenges/pangrams

Roy wanted to increase his typing speed for programming contests.
So, his friend advised him to type the sentence
"The quick brown fox jumps over the lazy dog" repeatedly, because
it is a pangram. (Pangrams are sentences constructed by using
every letter of the alphabet at least once.)

input:
The quick brown fox jumps over the lazy dog ->yes
We promptly judged antique ivory buckles for the next prize  ->yes
We promptly judged antique ivory buckles for the prize ->no

"""

def panagram_or_not(string):
    panagram = True
    all_alphabets = [chr(i) for i in range(97,123)]
    for alphabet in all_alphabets:
        if not alphabet in string:
            panagram = False
    if panagram:
        print "pangram"
    else:
        print "not pangram"


string = str(raw_input().strip())
if len(string) != 0:
    string = string.lower()
    panagram_or_not(string)
