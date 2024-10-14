class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        '''
        Implimentation with Bellman ford algorithm
        '''

        # Step 1: Initialize maximum probabilities for each node
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0  # The probability to reach the start node is 1.0
        
        # Step 2: Repeat the relaxation process for n-1 times
        for _ in range(n - 1):
            updated = False
            # Step 3: Relax all edges
            for i, (u, v) in enumerate(edges):
                prob = succProb[i]
                
                # Relax the edge u -> v
                if max_prob[u] * prob > max_prob[v]:
                    max_prob[v] = max_prob[u] * prob
                    updated = True
                
                # Relax the edge v -> u (since the graph is undirected)
                if max_prob[v] * prob > max_prob[u]:
                    max_prob[u] = max_prob[v] * prob
                    updated = True
            
            # If no update is made in an iteration, break early
            if not updated:
                break
        
        # Step 4: Return the maximum probability to reach the target node
        return max_prob[end_node] if max_prob[end_node] > 0 else 0.0