# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        n = 0
        while q:
            level = []
            n += 1
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
                    level.append(cur.val)
            if  level and n % 2 == 0:
                level.reverse()
                res.append(level)
            elif level:
                res.append(level)
        return res