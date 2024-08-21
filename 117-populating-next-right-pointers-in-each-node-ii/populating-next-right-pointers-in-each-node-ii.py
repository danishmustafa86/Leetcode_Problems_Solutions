"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([root])
        while q:
            dq = deque()
            for i in range(len(q)):
                node = q.popleft()
                dq.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            while len(dq)>1:
                cur  = dq.popleft()
                cur.next = dq[0]
            cur = dq.popleft()
            cur.next = None
        return root

