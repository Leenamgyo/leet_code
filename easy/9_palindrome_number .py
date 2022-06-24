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
        # int not iterable object
        
        is_minus = (x < 0)
        if is_minus: 
            return False    
        
        num, tmp_x = 0, x
        while tmp_x != 0:
            y = tmp_x % 10 
            num = (num * 10) + y
            tmp_x = tmp_x // 10
            
        return (num == x)
        
if __name__ == '__main__':
        """_summary_
        """    
        s = Solution()
        result = s.isPalindrome(121)










            

