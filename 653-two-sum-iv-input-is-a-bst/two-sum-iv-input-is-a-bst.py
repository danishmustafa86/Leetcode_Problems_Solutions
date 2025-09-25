# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        hash_map = dict()
        def dfs(root):
            if root is None:
                return False
            
            if k - root.val in hash_map:
                return True
                

            hash_map[root.val] = True   
            return dfs(root.right) or dfs(root.left)

        return dfs(root)