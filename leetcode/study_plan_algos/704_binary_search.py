# https://leetcode.com/problems/binary-search/



from re import search
from typing import List
from unittest.mock import seal


class Solution:
    def search_wrong(self, nums: List[int], target: int) -> int:
        if len(nums) > 0:
            if target <= nums[-1] and target >= nums[0]:
                start_idx = 0
                end_idx = len(nums)-1
                mid_idx = (start_idx + end_idx)//2
                if target == nums[mid_idx]:
                    return mid_idx
                elif target < nums[mid_idx]:
                    self.search(nums[start_idx:mid_idx], target)
                else:
                    self.search(nums[mid_idx:end_idx+1], target)
            else:
                return -1

    def search(self, nums: List[int], target: int) -> int:
        start_idx = 0
        end_idx = len(nums) - 1

        while(start_idx <= end_idx):
            mid_idx = (start_idx + end_idx) // 2
            if target == nums[mid_idx]:
                return mid_idx
            else:
                if target < nums[mid_idx]:
                    end_idx = mid_idx - 1
                else:
                    start_idx = mid_idx + 1
        return -1


solved = Solution()
print(solved.search([11,14,51,301,512,658,754,830,1010,5124], 1010))

