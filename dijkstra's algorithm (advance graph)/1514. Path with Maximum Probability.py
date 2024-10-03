class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        '''
        Dijkstra's algorithm implementation with max heap
        '''

        #step 1 adj List creation
        
        adj = defaultdict(list)

        for (src , target), prob in zip(edges,succProb):

            adj[src].append((target , prob))
            adj[target].append((src , prob))


        #step 2 max heap

        max_heap = [(-1,start_node)]

        visit = set()

        #step 3 Dijkstra's algorithm 

        while max_heap:

            prob ,current_node , = heapq.heappop(max_heap)

            visit.add(current_node)

            if current_node == end_node:
                return prob * -1


            for nei , new_prob in adj[current_node]:

                if nei not in visit:

                    heapq.heappush(max_heap ,(new_prob * prob,nei))


        return 0