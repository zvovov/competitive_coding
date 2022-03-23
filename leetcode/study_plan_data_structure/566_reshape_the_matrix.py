# https://leetcode.com/problems/reshape-the-matrix/

from typing import List
from itertools import chain

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # check if wanted matrix is possible and legal        
        if len(mat) * len(mat[0]) != r*c:
            return mat
        
        # convert mat into r*c
        # flatten
        flat_mat = list(chain(*mat))
        
        new_mat = []

        start = 0
        end = c
        for _ in range(r):
            new_mat.append(flat_mat[start:end])
            start = end
            end += c
        return new_mat

solved = Solution()
print(solved.matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4)) # [[1,2,3,4]]
print(solved.matrixReshape(mat = [[1,2,3,],[3,4,5,],[5,6,7,],[7,8,9,]], r = 3, c = 4)) # [[1,2,3,4]]