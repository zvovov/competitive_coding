# https://leetcode.com/problems/binary-search/

from typing import List

class Solution:
    def search_(self, nums: List[int], target: int) -> int:
        result_idx = -1

        left = 0
        right = len(nums) - 1

        if target == nums[left]: return left
        if target == nums[right]: return right

        while left < right:
            mid_idx = (left + right) // 2

            if target == nums[left]: return left
            if target == nums[right]: return right

            if target == nums[mid_idx]:
                return mid_idx

            if left + 1 == right: break

            elif target > nums[mid_idx]: left = mid_idx
            elif target < nums[mid_idx]: right = mid_idx
            

        return result_idx
    
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_idx = (left + right) // 2

            if target == nums[mid_idx]:
                return mid_idx

            elif target > nums[mid_idx]: left = mid_idx + 1
            elif target < nums[mid_idx]: right = mid_idx - 1 

        return -1


solved = Solution()
print(solved.search(nums = [-1,0,3,5,9,12], target = 9))
print(solved.search(nums = [-1,0,3,5,9,10,12], target = 12))
print(solved.search(nums = [-1,0,3,5,9,12], target = 2))
print(solved.search(nums = [-1], target = -1))
print(solved.search(nums = [-1, 0], target = 0))
print(solved.search(nums = [3], target = 4))
