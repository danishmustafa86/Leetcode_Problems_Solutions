# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        q = deque([root])
        arr = []
        while q:
            for i in range(len(q)-1):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            last = q.popleft()
            arr.append(last.val)
            if last.left:
                   q.append(last.left)
            if last.right:
                q.append(last.right)
        return arr
