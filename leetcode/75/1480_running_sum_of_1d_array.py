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
        

solved = Solution()
print(solved.runningSum([1,2,4,2,1,2,0]))

