# https://leetcode.com/problems/maximum-subarray/

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

# Kadane's solution
class Solution_kadane:
    def maxSubArray(self, nums):
            if not nums:
                return 0

            curSum = maxSum = nums[0]
            for num in nums[1:]:
                print("\nnum: ", num)
                curSum = max(num, curSum + num)
                print("curSum: ", curSum)
                maxSum = max(maxSum, curSum)
                print("maxSum: ", maxSum)

            return maxSum

solution = Solution_kadane()
print(solution.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray(nums=[1]))
print(solution.maxSubArray(nums=[5,4,-1,7,8]))

