# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #conditions needed to same as preorder traversal

        def dfs(root):
            
            if not root:
                return None

            left_side = dfs(root.left)
            right_side = dfs(root.right)

            if root.left:
                left_side.right = root.right
                root.right = root.left
                root.left = None
            last = right_side or left_side or root
            return last

        dfs(root)



         
 



            