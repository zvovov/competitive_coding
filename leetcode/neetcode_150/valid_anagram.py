# https://leetcode.com/problems/valid-anagram/

# Intuition:
# To be able to make one string from another, i need to have the exact same number of characters in both.

# Approach:
# First, check if they are the same length. They need to be if they are an anagram.
# Maintain a count of occurence of each character in a hashmap
# After traversing the length of the string, if they hashmaps are identical, its an anagram

# Complexity:
# Time O(n)
# Space O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check same length
        if len(s) != len(t):
            return False
        else:
            # define hashmap
            hm_s = {}
            hm_t = {}
            # iterate over both strings, build hashmap
            for i in range(len(s)):
                hm_s[s[i]] = hm_s.get(s[i])+1 if hm_s.get(s[i]) != None else 1
                hm_t[t[i]] = hm_t.get(t[i])+1 if hm_t.get(t[i]) != None else 1
            if hm_s == hm_t:
                return True
            else:
                return False



class Solution:
    def isAnagram(self, s: str, t: str)  -> bool:
        # create hashmap for s
        s_count = {}
        for i in s:
            if s_count.get(i) is None:
                s_count[i] = 1
            else:
                s_count[i] += 1

        # while creating hashmap for t, check if values of each ele in t is <= s
        t_count = {}
        for i in t:
            if t_count.get(i) is None:
                if s_count.get(i) is None:
                    return False
                else:
                    t_count[i] = 1
            else:
                t_count[i] += 1
        
        # check if all original characters are used exactly once
        for i in s:
            if s_count.get(i) != t_count.get(i):
                return False
        return True

solved = Solution()
print(solved.isAnagram(s = "anagram", t = "nagaram"))
print(solved.isAnagram(s = "rat", t = "car"))
print(solved.isAnagram(s = "ab", t = "a"))