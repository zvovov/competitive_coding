# https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n^2): nested loops
        # for left, right in range(len(numbers)-1): # left ends at the penultimate element
        #     reqd = target - numbers[left]
        #     for right in range(len(numbers)-1, left, -1): # right starts from the last element, and ends at just before left
        #         if reqd == numbers[right]:
        #             return list((left+1, right+1)) # +1 because 1-indexed
        #         elif numbers[right] < reqd:
        #             break
        #         else:
        #             continue

        
        # O(n): single loop
        left, right = 0, len(numbers) - 1 # first to last index. 0-index
        while left < right:
            reqd = target - numbers[left]

            if reqd == numbers[right]:
                return list((left+1, right+1)) # return 1-indexed indices
            elif reqd > numbers[right]:
                left += 1
                right = len(numbers)-1
            else: 
                right -= 1