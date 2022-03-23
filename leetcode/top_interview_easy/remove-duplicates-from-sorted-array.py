# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

# # for loop does not allow jumps in iterating variable
# for i in range(10):
#     print(i)
#     if i % 3 == 0: 
#         i += 1

# # jumps in iterating variable are possible in a while loop 
# i=0
# while i < 10:
#     print(i)
#     if i % 3 == 0: 
#         i += 2
#         continue
#     i+=1

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        curr_largest_unique = -101
        i_search_index = 0
        i_value_index = 0
        while i_search_index < len(nums):
            if i_search_index == 0: # for first element in nums
                curr_largest_unique = nums[i_value_index]
                k += 1 
            else: # for second element onwards
                j = i_search_index
                while j < len(nums):
                    if nums[j] > curr_largest_unique:
                        nums[i_value_index] = nums[j]
                        k += 1
                        curr_largest_unique = nums[j]
                        i_search_index = j # jump the iterating variable to the right
                        break
                    j += 1 
            i_value_index += 1
            i_search_index += 1
        return k

class Solution_optimized:
    def removeDuplicates(self, nums=List[int]) -> int:
        dup_counter = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: dup_counter += 1
            else: nums[i-dup_counter] = nums[i]
        return len(nums)-dup_counter


solution = Solution_optimized()
print(solution.removeDuplicates(nums=[0,0,1,2,2,3,4,5,6,6]))

