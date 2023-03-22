# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            curr_first_num = nums[i]
            curr_reqd_num = target - curr_first_num
            for j in range(i + 1, len(nums)): # loop on remaining elements 
                if nums[j] == curr_reqd_num:
                    return [i, j]
                
# solved = Solution()

# print(solved.twoSum(nums = [2,7,11,15], target = 9))
# print(solved.twoSum(nums = [3,2,4], target = 6))
# print(solved.twoSum(nums = [3,3], target = 6))
