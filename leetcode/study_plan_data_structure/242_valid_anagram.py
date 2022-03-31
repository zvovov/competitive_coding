# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isSubstring(self, s: str, t: str) -> bool:
        # create a hash table with key:value character:frequency
        # way-1: O(n)
        s_dict = {}
        for char in s:
            if s_dict.get(char) is not None:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        # way-2:  O(n^2) as .count takes O(n) time        
        # t_dict = {char: t.count(char) for char in t}

        t_dict = {}
        for char in t:
            if t_dict.get(char) is not None:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
            # check with s
            if (s_dict.get(char) is None) or (t_dict.get(char) > s_dict.get(char)):
                return False
        return True
        

solved = Solution()
print(solved.isSubstring(s="pahts", t="stahp")) # True
print(solved.isSubstring(s="pahtss", t="stahp")) # True
print(solved.isSubstring(s="pahts", t="sstahp")) # False
print(solved.isSubstring(s="pahtss", t="sttahp")) # False
