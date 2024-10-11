class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        '''
        Solution Using bellman ford algorithm 
        '''
        
        #distance init
        dist = [float("inf")] * (n+1)
        dist[k] = 0

        #Bellman ford implementation
        for _ in range(n-1):
            for u,v,w in times:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        max_dict = max(dist[1:])
        return max_dict if max_dict < float("inf") else -1