from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        while q:
            level += 1
            dq = deque()
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    dq.append(node.left)
                if node.right:
                    q.append(node.right)
                    dq.append(node.right)
            if level % 2 == 1:
                values = [node.val for node in dq]
                for node in dq:
                    node.val = values.pop()
        return root


