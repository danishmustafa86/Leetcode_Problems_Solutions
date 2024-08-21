# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # This list will store the inorder traversal
        def rec(node):
            if node:
                rec(node.left)    # Traverse left subtree
                res.append(node.val)  # Visit node
                rec(node.right)   # Traverse right subtree
        rec(root)  # Start the recursion with the root node
        return res  # Return the result









        # stack = []
        # inorder = []
        # while (stack or inorder):
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         root = stack.pop()
        #         inorder.append(root.val)
        #         root = root.right
        # return inorder










        # st=[]
        # res=[]
        # while root or st:
        #     while root:
        #         st.append(root)
        #         root=root.left
        #     root=st.pop()
        #     res.append(root.val)
        #     root=root.right
        # return res