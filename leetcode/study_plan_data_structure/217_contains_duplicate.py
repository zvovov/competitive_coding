# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {} # count frequency of each element
        for i in nums:
            if i in nums_dict:
                return True
            else:
                nums_dict[i] = 1
        return False


solution = Solution()
solution.containsDuplicate(nums=[1,2,3,1])


