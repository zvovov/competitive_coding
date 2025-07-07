# https://leetcode.com/problems/contains-duplicate/

from typing import List

# Brute Force

# Intuition:  
# Match every element in nums with every other elements. 

# Approach:  
# Two nested 'for' loops iterating over nums

# Complexity:  
# Time O(n^2)
# Space O(1)

class Solution:
    def containsDuplicate_bf(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i):
                # duplicate found
                if nums[i] == nums[j]:
                    return True
        # otherwise
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False




# Optimized 1

# Intuition:
# What if we only traversed each element only once
# This is not possible without sorting nums

# Approach:
# After sorting, we compare each element to the next until we traverse the entire nums array, or we find the duplicate

# Complexity:
# Time Sorting + Comparison time.  O(n + n logn) = O(n logn). n logn for quick sort or merge sort
# Space O(1), if in place sorting is used


# Optimized 2

# Intuition:
# Maintain a hashmap for the count of occurence for each character in nums

# Approach:
# While building the hashmap, if the next character is found out to already present in the hashmap, we know its a duplicate

# Complexity:
# Time O(n), because we traverse the array once to build the hashmap
# Space O(n), because we always have to build the hashmap


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        dict_count = {}
        for i in nums:
            if dict_count.get(i) == 1:
                return True
            else:
                dict_count[i] = 1
        return False

solved = Solution()
print(solved.contains_duplicate([1,2,3,4]))
print(solved.contains_duplicate([1,2,3,1]))
print(solved.contains_duplicate([1,1,1,3,3,4,3,2,4,2]))


