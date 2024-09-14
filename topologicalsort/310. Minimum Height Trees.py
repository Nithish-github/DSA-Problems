class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:


        '''
        To solve the "Minimum Height Trees" problem using topological sort, we can treat the 
        problem similarly to how we would handle a graph trimming problem. 
        Specifically, we use a BFS (breadth-first search) approach that removes the leaf nodes 
        (nodes with only one edge) layer by layer until we're left with the minimum number of 
        nodes (which will be the roots of the Minimum Height Trees). 
        This is a reverse topological sorting strategy that is ideal for this problem.
        '''

        #create a adj list for all the nodes

        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)


        #Will be using a reverse topological approch like 
        #graph trimming

        edge_cnt = {}
        leaves  = deque()
        for src , nei in adj.items() :
            if len(nei) == 1:
                leaves.append(src)
            edge_cnt[src] = len(nei)

        #running the breath first search approch for it 
        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n-=1
                for nei in adj[node]:
                    edge_cnt[nei]-=1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)
        