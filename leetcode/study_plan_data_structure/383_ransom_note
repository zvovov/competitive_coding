# https://leetcode.com/problems/ransom-note/

from itertools import count


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for char in magazine:
            if mag_dict.get(char) is not None:
                mag_dict[char] += 1
            else:
                mag_dict[char] = 1
        print(mag_dict)
        for ele in ransomNote:
            if mag_dict.get(ele) is not None:
                if mag_dict.get(ele) > 0:
                    mag_dict[ele] -= 1
                else: return False
            else: return False
        return True
    
    def canConstruct_optimized(self, ransomNote: str, magazine: str) -> bool:
        for ele in ransomNote:
            # print(ele)
            if ele in magazine:
                magazine = magazine.replace(ele, "", 1)
            else: return False
            # print("mag", magazine)
            
        return True


solved = Solution()
print(solved.canConstruct_optimized(ransomNote="aa", magazine="aab")) # True
print(solved.canConstruct_optimized(ransomNote="aa", magazine="ab")) # False