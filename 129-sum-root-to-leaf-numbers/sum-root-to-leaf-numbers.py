# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        totalSum = 0
        stack = [(root,0)]
        while stack:
            node,curSum = stack.pop()
            if node:
                curSum = curSum*10 + node.val
                if not node.left and not node.right:
                    totalSum += curSum
                if node.left:
                    stack.append((node.left,curSum))
                if node.right:
                    stack.append((node.right,curSum))
        return totalSum


