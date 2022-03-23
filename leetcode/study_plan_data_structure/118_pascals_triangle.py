# https://leetcode.com/problems/pascals-triangle/

from typing import List

[[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1],
[1,5,10,10,5,1],
[1,6,15,20,15,6,1],
[1,7,21,35,35,21,7,1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        if numRows == 1:
            return pascal
        
        row = [1, 1]
        pascal.append(row)
        if numRows == 2:
            return pascal

        for i in range(numRows-2):
            new_row = [1]
            for j in range(len(row)-1):
                new_row.append(row[j]+row[j+1])
            new_row.append(1)
            row = new_row
            # print(row)
            pascal.append(row)
        return pascal

solved = Solution()
print(solved.generate(numRows = 5))