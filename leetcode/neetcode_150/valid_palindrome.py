# https://leetcode.com/problems/valid-palindrome/

# Intuition:
# Clean the string and check if the string is the same forwards and backwards

# Approach:
# Remove non-alphanumeric characters and convert to lowercase
# Use isalnum to remove non-alphanumeric characters



class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join([char.lower() for char in s if char.isalnum()])
        for left in range(len(clean_s)):
            right = len(clean_s) - 1 - left # works because s >= 1
            if clean_s[left] != clean_s[right]:
                return False
        return True

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