'''
URL: https://leetcode.com/problems/palindrome-number/

Specification:
    Constraints:-2^31 <= x <= 2^31 - 1
    Follow up: Could you solve it without converting the integer to a string?

Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num: int = 121
        reverse: int = 121

        bin_num = bin(num)
        print()    

if __name__ == '__main__':
    s = Solution()
    # return s.isPalindrome()










            

