# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_and_balance(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # An empty tree has height 0 and is balanced
            
            left_height = height_and_balance(node.left)
            right_height = height_and_balance(node.right)
            
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1  # Tree is not balanced
            
            return max(left_height, right_height) + 1
        
        return height_and_balance(root) != -1
