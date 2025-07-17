# https://neetcode.io/problems/products-of-array-discluding-self

# Intuition:
# We calculate the product of all i of nums
# in the second iteration over nums, divide it by each i 

# without divide operation: use hashmap
# create hashmap with key: value as  

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        out = []
        for i in nums:
            if i != 0:
                prod *= i 
            else:
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)

        for i in nums:
            if zero_count == 1: 
                if i == 0:
                    out.append(prod)
                else:
                    out.append(0)
            else:
                out.append(int(prod/i)) 
        return out
