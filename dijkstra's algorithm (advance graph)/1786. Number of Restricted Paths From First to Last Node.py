class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        '''
        Solution using Dijkstra algorithm
        '''
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: Dijkstra's algorithm to find shortest path from node n to all other nodes
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        min_heap = [(0, n)]  # (distance, node)
        
        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(min_heap, (dist[v], v))

        #sorting the nodes based on their distance
        sorted_nodes = sorted(range(1, n + 1), key=lambda x: dist[x])

        path_count  = [0]*(n+1)
        path_count[n] = 1

        for u in sorted_nodes:
            for v,w in graph[u]:
                if dist[u] > dist[v]:
                    path_count[u]+=path_count[v]
                    path_count[u] %= MOD


        return path_count[1]


