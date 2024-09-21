from collections import defaultdict

from functools import lru_cache


class Solution:

    def leadsToDestination(self, n: int, edges: list, source: int, destination: int) -> bool:


        #adj list 
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)

        visited  = set()

        #Constructing the depth first search function
        def dfs(node):

            if node ==  destination:
                return len(adj_list[node]) == 0   #to make sure it is dead end

            if node in visited or not adj_list[node]:  #if the there is a dead end / there is a cycle 
                return False

            visited.add(node)

            for nei in adj_list[node]:
                if not dfs(nei):
                    return False

            return True


        return dfs(source)


#sample input
# n = 4
# edges = [[0, 1], [1, 2], [2, 0], [2, 3]]
# source = 0
# destination = 3
n = 4
edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
source = 0
destination = 3
sol  = Solution()
print("The final result ",sol.leadsToDestination(n,edges,source,destination))