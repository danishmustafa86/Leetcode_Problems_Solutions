"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        arr = []
        while q:
            cur = []
            for i in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                if node:
                    q.extend(node.children)
            arr.append(cur)
        return arr
