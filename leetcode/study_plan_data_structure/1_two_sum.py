# https://leetcode.com/problems/two-sum/

from typing import List

class Solution_brute_force():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

class Solution_binary_search():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_original = [*nums]
        nums.sort() # sort input
        for i in range(len(nums)): # iterate over input
            # run binary search in the remaining elements to find the matching j,
            # such that i + j = target
            j = target - nums[i]
            # binary search to find j
            result = self.binarySearch(nums, j, 0, len(nums)-1)
            if result is not None:
                # find index in nums_original
                return [nums_original.index(nums[i]), nums_original.index(nums[result])]
                # return [i, result]
            return None

    def binarySearch(self, inp: List[int], to_find: int, left: int, right: int) -> int:
        """
        Uses binary search to find integer and return its index from sorted list.
        Returns None otherwise
        """
        # do not change the length of array; this will not work
        # mid = floor(len(list)/2)
        # if mid == to_find return
        # if mid < to_find:
        #     bs(start:mid-1, to_find)
        # else: bs(mid+1:end, to_find)

        # correct binary search implementation; does not take care of the case nums=[3,3] & target=6
        mid = (left + right)//2
        # print("tofind: ", to_find, "mid", mid, "nums: ", inp)

        if left > right: return None

        if inp[mid] == to_find:
            return mid
        if inp[mid] < to_find:
            return self.binarySearch(inp, to_find, mid+1, right)
        return self.binarySearch(inp, to_find, left, mid-1) 

class Solution_hashmap():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return [seen[remaining], i]
            seen[value] = i
        return None

solution = Solution_hashmap()
print(solution.twoSum(nums=[2,8,11,15,5,72,11,9,7,23,4,3], target=9)) # [0,8]
print(solution.twoSum(nums=[2,7,11,15], target=9)) # [0,1]
print(solution.twoSum(nums=[3,2,4], target=6)) # [1,2]
print(solution.twoSum(nums=[3,3], target=6)) # [0,1]
