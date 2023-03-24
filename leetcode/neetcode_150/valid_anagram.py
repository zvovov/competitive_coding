# https://leetcode.com/problems/valid-anagram/

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