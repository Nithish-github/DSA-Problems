# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #have a variable to count the occurance

        result = []

        def dfs(node):
            nonlocal result

            if node is None:
                return None

            # Traverse the left subtree
            dfs(node.left)

            # Process the current node
            result.append(node.val)

            # Traverse the right subtree
            dfs(node.right)
    

        dfs(root)
        return result[k-1]
        
        