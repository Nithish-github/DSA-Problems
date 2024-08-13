# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ''' 
        Can be solved using bfs algorithm 
        '''

        if not root:
            return None

        queue = deque([root])
        result = []
        while queue:

            prev = None

            for _ in range(len(queue)):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(node.val)


        return result


        