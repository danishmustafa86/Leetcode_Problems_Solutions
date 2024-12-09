# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def traverse(root, Sum):
            if not root:
                return False
            Sum += root.val
            if not root.left and not root.right:
                return targetSum == Sum
            return traverse(root.left, Sum) or traverse( root.right, Sum)

        return traverse(root, 0)



# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#         def traverse (cur:Optional[TreeNode],sum)->bool:
#             if not cur:
#                 return False    
#             sum+=cur.val
#             if not cur.left and not cur.right:
#                 return sum==targetSum
#             return traverse(cur.left, sum) or traverse(cur.right, sum)
#         return traverse(root,0)
