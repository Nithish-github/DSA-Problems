class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        '''
        This problem should be seen from the point of view of grpah 
        '''

        adj = defaultdict(list)

        for i,eq in enumerate(equations):
            a,b = eq
            adj[a].append([b,values[i]])
            adj[b].append([a,1/values[i]])


        #implementing Breath first search approch 

        def bfs(src , target):
            if src not in adj or target not in adj:
                return -1

            
            queue , visit = deque() , set()
            queue.append([src , 1])
            visit.add(src)

            while queue:
                n,w = queue.popleft()

                if n == target:
                    return w

                for nei , weight in adj[n]:
                    if nei not in visit:
                        queue.append([nei , w*weight])
                        visit.add(nei)

            return -1 

        return [bfs(q[0],q[1]) for q in queries]
        