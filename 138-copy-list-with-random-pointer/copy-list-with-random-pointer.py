"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        newNode = {}
        cur = head
        while cur:
            newNode[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                newNode[cur].next = newNode[cur.next]
            if cur.random:        
                newNode[cur].random = newNode[cur.random]
            cur = cur.next

        return newNode[head]