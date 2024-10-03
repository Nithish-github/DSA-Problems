class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        '''
        Solution using Dijkstra algorithm 
        '''

        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v,w))

        #min_heap
        min_heap  = [(0,k)]

        dist = {}  #to save the min distance

        while min_heap:
            d , node  = heapq.heappop(min_heap)

            if node in dist:
                continue

            dist[node] = d

            for nei , weight in adj[node]:
                if nei not in dist:
                    heapq.heappush(min_heap,(d+weight , nei))


        if len(dist)!=n:
            return -1

        return max(dist.values())
        