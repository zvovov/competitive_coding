# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution_inplace_nope:
    def mergeSortedArray(self, nums1: List[int], nums2: List[int], m: int, n: int) -> List[int]:
        i, j, inserted = 0, 0, 0
        while i < (m + inserted) and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                inserted += 1
                nums1.pop()
                j += 1
                i += 1
        return nums1


class Solution_additional_space_nope:
    def mergeSortedArray(self, nums1: List[int], nums2: List[int], m: int, n: int) -> List[int]:
        nums3 = [0 for i in range(m + n)] 
        i, j = 0, 0
        for k in range(len(nums3)):
            if j < n > 0:
                if nums1[i] <= nums2[j] and i < m:
                    nums3[k] = nums1[i]
                    i += 1
                else:
                    nums3[k] = nums2[j]
                    j += 1
            else:
                nums3[k] = nums1[i]
        nums1[:] = nums3
        print(nums1)


class Solution_reverse:
    def mergeSortedArray(self, nums1: List[int], nums2: List[int], m: int, n: int) -> List[int]:
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        nums1[:n] = nums2[:n]
        # print(nums1)

        


solution = Solution_reverse()
solution.mergeSortedArray(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
solution.mergeSortedArray(nums1 = [0], m = 0, nums2 = [1], n = 1)
solution.mergeSortedArray(nums1 = [1], m = 1, nums2 = [], n = 0)
solution.mergeSortedArray(nums1 = [2,0], m = 1, nums2 = [1], n = 1)