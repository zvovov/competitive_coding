# https://leetcode.com/problems/maximum-subarray/

from math import inf
from typing import List

# brute-force; TLE
class Solution_brute_force:
    def maxSubArray(self, nums: List[int]) -> int:
        highest_sum = max(nums)
        for i in range(len(nums)-1):
            curr_i_sum_array = []
            for j in range(i+1, len(nums)):
                curr_i_sum_array.append(sum(nums[i:j+1]))
            
            highest_sum = max(max(curr_i_sum_array), highest_sum)
        return highest_sum


# Kadane's algo
class Solution_kadane:
    def maxSubArray(self, nums):
        curr_sum, max_sum = 0, -inf
        for i in nums:
            curr_sum = max(i, curr_sum + i)
            max_sum = max(curr_sum, max_sum)
        return max_sum

  

solution = Solution_kadane()
print(solution.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray(nums=[1]))
print(solution.maxSubArray(nums=[5,4,-1,7,8]))

