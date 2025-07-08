# https://leetcode.com/problems/two-sum/


# Intuition:
# (Target - current) = the desired number to find in nums

# Approach:
# Hashmap one pass
# While building a hashmap, compute the desired number and find it in nums

# Complexity:
# Time O(n), for building the hashmap and constant lookups to find the desired number
# Space O(n), for the hashmap

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# desired_hm = {
#     7: 0,   
#     2: 1,     <--- .get(nums[i]) == 7
#     ...
# }


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        desired_hm = {}
        for i in range(len(nums)):
            desired = target - nums[i]
            # print("Checking desired_hm[nums[{}]]: {}".format(i, desired_hm.get(nums[i])))
            if desired_hm.get(nums[i]) is not None:
            # if nums[i] in desired_hm:
                return [desired_hm.get(nums[i]), i]
            else:
                desired_hm[desired] = i
            # print(desired_hm) 

from typing import List

class Solution_Brute_Force:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            curr_first_num = nums[i]
            curr_reqd_num = target - curr_first_num
            for j in range(i + 1, len(nums)): # loop on remaining elements 
                if nums[j] == curr_reqd_num:
                    return [i, j]
                
class Solution: # hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for idx, num in enumerate(nums):
            if (target - num) in store:
                return [idx, store[target - num]]
            store[num] = idx           
                
solved = Solution()

print(solved.twoSum(nums = [2,7,11,15], target = 9))
print(solved.twoSum(nums = [3,2,4], target = 6))
print(solved.twoSum(nums = [3,3], target = 6))
