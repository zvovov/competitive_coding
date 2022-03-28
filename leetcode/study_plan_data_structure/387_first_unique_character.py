# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}
        # create a dictionary with keys = elements of input and values = index
        for i in range(len(s)):
            if s_dict.get(s[i]) is not None:
                s_dict[s[i]] = -1
            else:
                s_dict[s[i]] = i
        
        for k in s_dict.values(): # assuming dict is sorted as per python 3.7+
            if k > -1:
                return k
        return -1


solved = Solution()
print(solved.firstUniqChar(s="ppiizza is my soulmate")) # 12