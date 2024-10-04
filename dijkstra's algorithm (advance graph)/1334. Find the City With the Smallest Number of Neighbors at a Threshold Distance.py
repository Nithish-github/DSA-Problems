class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:


        #step 1 construction of adj list
        adj = defaultdict(list)

        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))



        def dijkstra(src):

            distance = [float("inf")] * n
            distance[src] = 0
            min_heap = [(0,src)]


            while min_heap:
                curr_weight , curr_node = heapq.heappop(min_heap)

                if curr_weight < distance[curr_node]:
                    continue


                for nei , weight in adj[curr_node]:

                    new_weight = weight + curr_weight

                    if new_weight < distance[nei]:
                        distance[nei]  = new_weight
                        heapq.heappush(min_heap , (new_weight , nei))


            return distance


        result_city = -1
        min_count = n

        for city in range(n):
            distance = dijkstra(city)
            count= sum(1 for dist in distance if dist <=distanceThreshold )

            if count < min_count or (count == min_count and city>result_city):
                result_city = city
                min_count  = count


        return result_city



                
            






        