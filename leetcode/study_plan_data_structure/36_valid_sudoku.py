# https://leetcode.com/problems/valid-sudoku/


from typing import List
import numpy as np

class Solution:
    def isValidSeries(self, inp_series: np.ndarray) -> bool:
        # inp_series = inp_series.astype(int)
        inp_series = inp_series.flatten()
        
        # remove dots
        inp_series = inp_series[inp_series != "."]
        # print(inp_series)
        # check if all are unique
        if len(set(inp_series)) != len(inp_series):
            return False

        # check if all elements are between 1-9
        return all(map(lambda x: True if 0 < int(x) < 10 else False, inp_series))

    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # convert to pandas df
        board_df = np.asarray(board)
        # print(type(board_df), board_df.shape, board_df)
        # check
        
        # check rows
        for row in range(board_df.shape[0]):
            # print(type(board_df.loc[row, :]))
            if self.isValidSeries(board_df[row, :]) == False:
                return False
            
            # check 3x3 squares
            if row % 3 == 0:
                # print("row: ", row)
                for col in range(3):
                    # print(" 3x3 square")
                    # print(board_df[row:row+3, col*3: col*3+3])
                    if self.isValidSeries(board_df[row:row+3, col*3: col*3+3]) == False:
                        return False

        # check columns
        for col in range(board_df.shape[1]):
            # print(board_df.loc[:,col])
            if self.isValidSeries(board_df[:,col]) == False:
                return False
        return True

solved = Solution()
print(solved.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # true

print(solved.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # false


print(solved.isValidSudoku(board =
[[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]))