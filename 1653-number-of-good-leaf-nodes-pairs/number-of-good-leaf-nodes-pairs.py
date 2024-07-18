
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            
            # If it's a leaf node
            if not node.left and not node.right:
                return [1]
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count valid pairs
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.count += 1
            
            # Collect distances from this node to leaves
            new_distances = []
            for d in left_distances:
                new_distances.append(d + 1)
            for d in right_distances:
                new_distances.append(d + 1)
            
            return new_distances
        
        self.count = 0
        dfs(root)
        return self.count

# Example usage
root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
distance = 3
sol = Solution()
print(sol.countPairs(root, distance))  # Output: 1
