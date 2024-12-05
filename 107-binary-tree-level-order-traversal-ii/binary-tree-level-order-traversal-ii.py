# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
                    level.append(cur.val)
            if level:
                res.append(level)
        ans = []
        for i in range(len(res) - 1, -1, -1):
            ans.append(res[i])
        return ans