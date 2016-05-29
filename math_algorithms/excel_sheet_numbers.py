"""
http://www.geeksforgeeks.org/find-excel-column-name-given-number/

Input          Output
 26             Z
 51             AY
 52             AZ
 80             CB
 676            YZ
 702            ZZ
 705            AAC

"""
def print_excel_col_name(num):
    if num<0 or not isinstance(num, int):
        return

    string = ""
    while num>0:
      rem = num %26
      if rem == 0:
        #some cases like 52 where it should print 'AZ'
        string += 'Z'
        num = num/26 -1
      else:
        # here rem-1 is used as ord('A') already starts from 65.
        # example if the expected character is 'C' and if rem= 3 it will return 'D'.
        string += chr(rem-1 + ord('A'))
        num = num/26

    # Reverse the string and print result
    string = string[::-1]
    print string


print_excel_col_name(26)
print_excel_col_name(51)
print_excel_col_name(52)
print_excel_col_name(80)
print_excel_col_name(676)
print_excel_col_name(702)
print_excel_col_name(705)
