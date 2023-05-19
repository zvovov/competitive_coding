# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def depth(n): 
            if not n: return 0
            left, right = depth(n.left), depth(n.right)
            self.ans = max(left + right, self.ans)
            return max(left, right) + 1
        
        depth(root)

        return self.ans