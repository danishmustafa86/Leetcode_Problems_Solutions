# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def pre(mn, node, high):
            if not node:
                return True
            if not (mn < node.val < high):
                return False
            # Check the left and right subtrees with updated bounds
            return pre(mn, node.left, node.val) and pre(node.val, node.right, high)

        return pre(float("-inf"), root, float("inf"))



















        # if not root:
        #     return True

        # # Queue will store tuples of (node, lower_bound, upper_bound)
        # q = deque([(root, float('-inf'), float('inf'))])

        # while q:
        #     node, low, high = q.popleft()
            
        #     # If the current node's value does not satisfy the BST properties, return False
        #     if not (low < node.val < high):
        #         return False

        #     # For the left child, update the upper bound to the current node's value
        #     if node.left:
        #         q.append((node.left, low, node.val))

        #     # For the right child, update the lower bound to the current node's value
        #     if node.right:
        #         q.append((node.right, node.val, high))
        
        # # If all nodes satisfy the BST properties, return True
        # return True






































# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         q = deque([root])
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft()
#                 if node.left and node.left.val is not None and node.val < node.left.val:
#                     return False
#                 if node.right and node.right.val is not None and node.val < node.right.val:
#                     return False
#                 q.append(node.left)
#                 q.append(node.right)
#         return True
        
            


