class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        '''
        1. The scope is there should be no loop in the graph 
        2. and every one should be connected
        '''
        
        if not n:
            return True


        adj = defaultdict(list)
        for n1 , n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        
        #add the set for visit
        visit = set()

        def dfs(node,prev):
            if node in visit:
                return False

            visit.add(node)

            for j in adj[node]:
                if j == prev:
                    continue
                if not dfs(j,node):
                    return False

            return True


        return dfs(0,-1) and n == len(visit)


            

        