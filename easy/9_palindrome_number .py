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
    # isPalindrome_Solution_1, isPalindrome_Solution_2 is best faster in leetCode 
    # Solution 1: 89.20% faster
    def isPalindrome_Solution_1(self, x: int) -> bool:
        if x<0: 
            return False

        inputNum = x
        newNum = 0
        while x>0:
            newNum = newNum * 10 + x%10
            x = x//10
        return newNum == inputNum
    
    
    # Solution 2: 99.14% faster.
    def isPalindrome_Solution_2(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
	        return False
        
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
            
        return True if (x == result or x == result // 10) else False
    
    
    # made by me 
    def isPalindrome(self, x: int) -> bool:
        # int not iterable object
        
        is_minus = (x < 0)
        if is_minus: 
            return False    
        
        num, tmp_x = 0, x
        while tmp_x != 0:
            num = (num * 10) + tmp_x % 10 
            tmp_x = tmp_x // 10
            
        return (num == x)
    
    
        
if __name__ == '__main__':
        """_summary_
        """    
        s = Solution()
        result = s.isPalindrome(121)










            

