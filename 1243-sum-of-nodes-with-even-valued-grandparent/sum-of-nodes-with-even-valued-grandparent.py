# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = deque([root])
        msum = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.val%2 == 0 :
                    if node.left:
                        if node.left.left:
                            msum += node.left.left.val
                        if node.left.right:
                            msum += node.left.right.val
                    if node.right:
                        if node.right.left:
                            msum += node.right.left.val
                        if node.right.right:
                            msum += node.right.right.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return msum