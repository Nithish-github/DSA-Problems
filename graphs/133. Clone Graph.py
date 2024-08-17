"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #creating the deep copy for the graph
        #using the concept of dfs

        old_to_new = {}

        def dfs(node):

            if node in old_to_new:
                return old_to_new[node]


            deep_copy = Node(node.val)
            old_to_new[node] = deep_copy


            for nei in node.neighbors:
                deep_copy.neighbors.append(dfs(nei))


            return deep_copy

        return dfs(node) if node else  None
        