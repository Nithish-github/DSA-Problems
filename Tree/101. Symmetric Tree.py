# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        #implementation of Depth first search 
        # def dfs(left , right):
        #     if not left and not right:
        #         return True
        #     if not left or not right:
        #         return False
        #     if left.val != right.val:
        #         return False

        #     return (dfs(left.left , right.right)) and (dfs(left.right , right.left))

        # return dfs(root.left,root.right)

        #Implementation in Breath First Search 

        if not root:
                return True
            
        queue = deque([(root.left, root.right)])
        
        while queue:
            left, right = queue.popleft()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
            
        return True
