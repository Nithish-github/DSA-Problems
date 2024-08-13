# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #The solution can be given both in BFS and DFS
        '''
        Breath First Tree
        '''

        # if not root:
        #     return None

        # queue = deque([root])


        # while queue:

        #     node  = queue.popleft()

        #     node.left , node.right = node.right , node.left

        #     if node.left is not None:
        #         queue.append(node.left)

        #     if node.right is not None:
        #         queue.append(node.right)



        # return root


        '''
        Depth First Search Approch
        '''

        def dfs(node):

            if not node:
                return None

            node.left , node.right = node.right , node.left


            #it is preorder traversal
            dfs(node.left)
            
            dfs(node.right)

        dfs(root)
        return root








        