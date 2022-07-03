# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = 0
        output_lst = [0]*len(nums)

        for i in range(len(nums)):
            curr_sum += nums[i]
            output_lst[i] = curr_sum
        
        return output_lst 
    
    def runningSum_inplace(self, nums: List[int]) -> List[int]:
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            nums[i] = curr_sum
        
        return nums 
    
    def runningSum_inplace_optimized(self, nums: List[int]) -> List[int]:
        curr_sum = 0
        return [curr_sum := curr_sum + i for i in nums]

solved = Solution()
print(solved.runningSum([1,2,4,2,1,2,0]))
print(solved.runningSum_inplace([1,2,4,2,1,2,0]))
print(solved.runningSum_inplace_optimized([1,2,4,2,1,2,0]))

