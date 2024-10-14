class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        dist = [float('inf')] * (n+1)
        dist[src] = 0

        temp_dist = dist.copy()

        for _ in range(k+1):


            for u,v,w in flights:

                if dist[u] != float('inf') and dist[u] + w < temp_dist[v]:
                    temp_dist[v] = dist[u] + w

            # Update the main distance array for the next iteration
            dist = temp_dist.copy()

        # If the destination city's distance is still infinity, return -1 (no valid route within k stops)
        return dist[dst] if dist[dst] != float('inf') else -1