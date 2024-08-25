# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        q = deque([root])
        maxarr = []
        while q:
            mx = float("-inf")
            for i in range(len(q)):
                node = q.popleft()
                mx = max(node.val,mx)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            maxarr.append(mx)
        return maxarr