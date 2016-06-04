"""
https://www.careercup.com/question?id=5709246416027648

amazon-interview-questions1
of 1 vote
39
Answers
print all the characters present in the given string only once in a reverse order. Time & Space complexity should not be more than O(N).
e.g.
1)Given a string aabdceaaabbbcd
the output should be - dcbae

2)Sample String - aaaabbcddddccbbdaaeee
Output - eadbc

3)I/P - aaafffcccddaabbeeddhhhaaabbccddaaaa
O/P - adcbhef

"""
def print_reverse(str):
  lista=map(lambda x:x, str)
  output_list=[]
  for ele in lista:
    if ele in output_list:
      output_list.remove(ele)
    output_list.append(ele)
  return ''.join(output_list)[::-1]


input1='aabdceaaabbbcd'
output1 = print_reverse(input1)
print "input:{0} checking output:{1} is same:{2}".format(input1, output1, (output1 =='dcbae'))
input2 = 'aaaabbcddddccbbdaaeee'
output2 = print_reverse(input2)
print "input:{0} checking output:{1} is same:{2}".format(input2, output2, (output2 =='eadbc'))
input3 = 'aaafffcccddaabbeeddhhhaaabbccddaaaa'
output3 = print_reverse(input3)
print "input:{0} checking output:{1} is same:{2}".format(input3, output3, (output3 =='adcbhef'))
