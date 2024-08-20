# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        arr = []
        # msum = 0
        while q:
            newarr = []
            for i in range(len(q)):
                node = q.popleft()
                newarr.append(node.val)
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            arr.append(newarr)
            print(newarr)
            # msum = max(msum,sum(newarr))
        return sum(arr[-1])