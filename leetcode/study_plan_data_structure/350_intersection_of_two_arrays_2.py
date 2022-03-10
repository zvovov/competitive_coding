# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # convert nums1 to a dict {element: freq}
        # iterate over nums2, and check if element is present in nums1_dict
        #   if present, append element to output_arr and --1 freq 
        # return output_arr

        nums1_dict = {}
        intersection = []
        for i in nums1:
            nums1_dict[i] = nums1_dict[i] + 1 if i in nums1_dict else 1

        for j in nums2:
            if j in nums1_dict:
                if nums1_dict[j] > 0:
                    intersection.append(j)
                    nums1_dict[j] -= 1
        
        return intersection                    

solution = Solution()
print(solution.intersect([1,2,3], [4,5,6,1,3]))
print(solution.intersect([1,2,2,1], [2,2]))
print(solution.intersect([4,9,5], [9,4,9,8,4]))
