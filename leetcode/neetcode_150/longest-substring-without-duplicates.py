# Intuition:
# use a sliding window to count the length of the longest
# substring using two pointers

# Approach:
# left pointer starts at 0, right moves with iteration loop
# Iterate on s and maintain a map with char:index
# when char is found existing in map, move left pointer
# one step to the right of the position
# maintain max of existing longest and current window len

# Complexity:
# Time: O(n) for iterating the string. 
# Hashmap storage and lookups are O(1)
# Space: O(n) for hashmap and O(1) for the counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest