# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        '''
        Needed to return the root to leaf path 
        '''

        def dfs(root , current_sum):

            if not root:
                return 0
            current_sum = current_sum * 10 + root.val
            if not root.left and not root.right:
                return current_sum   
            left_side = dfs(root.left,current_sum)
            right_side = dfs(root.right,current_sum)

            return left_side + right_side


        return dfs(root , 0)



        



        