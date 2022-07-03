# https://leetcode.com/problems/find-pivot-index/

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[i+1::]):
                return i
        return -1
        # TLE
    
    def pivotIndex_optimized(self, nums: List[int]) -> int:
        left_sum = 0
        nums_sum = sum(nums)
        for i in range(len(nums)):
            # use left_sum
            # compute right_sum
            right_sum = nums_sum - left_sum - nums[i]
            
            # check return condition
            if left_sum == right_sum:
                return i

            # update left_sum
            left_sum += nums[i]
         
        return -1

    def pivotIndex_optimized_further(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            # compute right_sum
            right_sum -= nums[i]
            
            # check return condition
            if left_sum == right_sum:
                return i

            # update left_sum
            left_sum += nums[i]
         
        return -1

solved = Solution()
# print(solved.pivotIndex([1,7,3,6,5,6]))
# print(solved.pivotIndex([1,2,3]))
# print(solved.pivotIndex([2,1,-1]))

print(solved.pivotIndex_optimized_further([1,7,3,6,5,6]))
print(solved.pivotIndex_optimized_further([1,2,3]))
print(solved.pivotIndex_optimized_further([2,1,-1]))
