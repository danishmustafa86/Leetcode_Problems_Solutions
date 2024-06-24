# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        maxHeight=0
        def dfs (cur: Optional[TreeNode], index : int):
            nonlocal maxHeight
            if not cur:
                maxHeight= max( maxHeight, index)
                return
            dfs (cur.left, index+1) 
            dfs (cur.right, index+1) 
        dfs(root,0)
        # step_2
        ansList = [[] for _ in range(maxHeight)]
        # step_3
        def dfsFunc (cur: Optional[TreeNode], index : int):
            nonlocal maxHeight
            if not cur:
                # maxHeight= max( maxHeight, index)
                return
            ansList[index].append(cur.val)
            dfsFunc (cur.left, index+1) 
            dfsFunc (cur.right, index+1) 
        dfsFunc(root,0)    
        # step_4
        for i in range(maxHeight):
            if i%2 == 1:
                ansList[i] = ansList[i][::-1]
        return ansList