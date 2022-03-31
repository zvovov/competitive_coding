# https://leetcode.com/problems/valid-anagram/

from socket import TCP_SYNCNT

from numpy import s_


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

    def isAnagram(self, s: str, t: str) -> bool:
        
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

        # print(s_dict, t_dict)

        # check if all elements are used once
        for key, val in s_dict.items():
            if (t_dict.get(key) is None) or (val != t_dict.get(key)):
                return False
        return True

    def isAnagram_readable(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        return s_dict == t_dict

solved = Solution()
# print(solved.isSubstring(s="pahts", t="stahp")) # True
# print(solved.isSubstring(s="pahtss", t="stahp")) # True
# print(solved.isSubstring(s="pahts", t="sstahp")) # False
# print(solved.isSubstring(s="pahtss", t="sttahp")) # False

print(solved.isAnagram_readable(s="pahts", t="stahp")) # True
print(solved.isAnagram_readable(s="pahtss", t="stahp")) # False
print(solved.isAnagram_readable(s="pahts", t="sstahp")) # False
print(solved.isAnagram_readable(s="pahtss", t="sttahp")) # False
print(solved.isAnagram_readable(s="ab", t="a")) # False