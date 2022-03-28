# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def binarySearch(self, inp: List[int], target: int) -> int:
        # TODO
        pass
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target>=i[0] and target<=i[-1]:
                for j in i:
                    if target == j:
                        return True 
                return False

solved = Solution()
print(solved.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)) # True
print(solved.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) # False


