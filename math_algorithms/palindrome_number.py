"""
https://leetcode.com/problems/palindrome-number/
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_str = str(x)
        number_of_digits = len(num_str)
        index_counter = 0

        while(number_of_digits>index_counter):
            reminder = x%10
            if x>=0:
                first_digit = int(num_str[index_counter])
            else:
                first_digit = int(num_str[index_counter+1])

            if first_digit != reminder:
                return False
            x=x/10
            number_of_digits -= 1
            index_counter += 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print sol.isPalindrome(123456)
    print sol.isPalindrome(123321)
    print sol.isPalindrome(1)
    print sol.isPalindrome(00)
    print sol.isPalindrome(010)
    print sol.isPalindrome(-2147483648)
    print sol.isPalindrome(0)
