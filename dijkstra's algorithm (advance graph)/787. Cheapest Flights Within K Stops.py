class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        '''
        The Approch is with BFS and priority queue(heap) 
        '''

        adj = defaultdict(list)
        for fr,to,price in flights:
            adj[fr].append([to,price])


        min_heap =[(0,src,0)] #cost, node, stops

        visited = defaultdict(lambda : float('inf'))
        visited[(src , 0)] = 0    #the source node with 0 stops requires 0 cost


        while min_heap:

            current_cost , current_node , stops = heapq.heappop(min_heap)

            if current_node == dst:
                return current_cost


            if stops<=k:

                for to , price in adj[current_node]:
                    new_cost = price + current_cost

                    if new_cost < visited[(to , stops+1)]:
                        visited[(to , stops+1)] = new_cost
                        heapq.heappush(min_heap,(new_cost , to , stops+1)) 


        return -1

