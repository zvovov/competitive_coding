# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx = 0
        while t_idx < len(t):
            if s_idx < len(s):
                if s[s_idx] == t[t_idx]:
                    s_idx += 1
            else:
                return True
            t_idx += 1
        print(s_idx, t_idx)
        if s_idx == len(s) and t_idx == len(t):
            return True
        else:
            return False
        
solved = Solution()
print(solved.isSubsequence(s = "abc", t = "ahbgdc"))
print(solved.isSubsequence(s = "axc", t = "ahbgdc"))
print(solved.isSubsequence(s = "a", t = "c"))


