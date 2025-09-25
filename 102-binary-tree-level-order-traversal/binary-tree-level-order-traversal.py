# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if level:
                res.append(level)
        
        return res























        # res = []
        # q = deque()
        # q.append(root)
        # while q:
        #     level = []
        #     for i in range(len(q)):
        #         node  = q.popleft()
        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if level:
        #         res.append(level)
        # return res




















        # if not root:
        #     return []
        # q = deque([root])
        # arr = []
        # while q:
        #     cur = []
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         cur.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     arr.append(cur)

        # return arr
            
