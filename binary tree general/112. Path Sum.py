# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        '''
        Using Depth first search approch for traveral purpose
        needed to traverse from root to node  --- > preorder 
        '''

        def dfs(root , current_sum):
            if not root:
                return False

            #add the sum 
            current_sum += root.val

            #check the current node is leaf node 
            if not root.left and not root.right:
                if current_sum == targetSum:
                    return True

            left_side = dfs(root.left , current_sum)
            right_side = dfs(root.right , current_sum)

            return left_side or right_side


        return dfs(root ,0)






        