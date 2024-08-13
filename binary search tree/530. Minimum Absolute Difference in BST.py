# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
            
        prev = None
        min_diff = float('inf')

        def dfs(node):
            nonlocal prev, min_diff
            if node is None:
                return
            
            # Traverse the left subtree
            dfs(node.left)
            
            # Process the current node
            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev))
            prev = node.val
            
            # Traverse the right subtree
            dfs(node.right)
    

        dfs(root)
        return min_diff