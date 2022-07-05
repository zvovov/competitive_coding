# https://leetcode.com/problems/isomorphic-strings/


from operator import ge


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_dict = {}
        for _, char in enumerate(s): # read s and t, char-by-char
            if st_dict.get(char): # repeat char in s
                if st_dict[char] != t[_]:
                    return False
            else: # new char in s
                st_dict[char] = t[_]
        if len(set(st_dict.values())) != len(st_dict.keys()):
            return False

        return True
            

solved = Solution()
print(solved.isIsomorphic(s = "egg", t = "add"))
print(solved.isIsomorphic(s = "foo", t = "bar"))
print(solved.isIsomorphic(s = "paper", t = "title"))
print(solved.isIsomorphic(s = "badc", t = "baba"))