"""
URL: 
    https://leetcode.com/problems/valid-palindrome/

Question: 
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
    it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""

# 1. case_ignore
# 2. non-alphanumeric characters
# 3. palindrome 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s =  s.lower()
        s =  re.sub['[^a-z0-9]','', s] 
        
        # newS= [i.lower() for i in s if i.isalnum()] other 
        return s[:] == s[::-1]
    
    # two pointer solution
    def isPalindrome_best(self, s):
        l, r = 0, len(s)-1
        while l < r:
            # l이 alnum이 아니면 한칸 이동한다.
            while l < r and not s[l].isalnum():
                l += 1
            # r이 alnum이 아니면 한칸 이동한다.
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True
            
if __name__ == '__main__':
    s = Solution()
    s.isPalindrome_best(' tet')