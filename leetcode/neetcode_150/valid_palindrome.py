# https://leetcode.com/problems/valid-palindrome/

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # only keep alphanumeric characters
        s = re.sub('[\W_]+', '', s)
        # convert to lowercase
        s = s.lower()

        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

solved = Solution()
print(solved.isPalindrome(s = "A man, a plan_, a canal: Panama"))
print(solved.isPalindrome(s = "race a car"))
print(solved.isPalindrome(s = "race  car"))
print(solved.isPalindrome(s = " "))