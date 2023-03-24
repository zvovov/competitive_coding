# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        dict_count = {}
        for i in nums:
            if dict_count.get(i) == 1:
                return True
            else:
                dict_count[i] = 1
        return False

solved = Solution()
print(solved.contains_duplicate([1,2,3,4]))
print(solved.contains_duplicate([1,2,3,1]))
print(solved.contains_duplicate([1,1,1,3,3,4,3,2,4,2]))