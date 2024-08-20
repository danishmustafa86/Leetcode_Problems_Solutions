# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root,False)])
        leftSum = 0
        while q:
            node,isleft =  q.popleft()
            if isleft and not node.left and not node.right:
                leftSum += node.val
            if node.left:
                q.append((node.left,True))
            if node.right:
                q.append((node.right,False))
        return leftSum
