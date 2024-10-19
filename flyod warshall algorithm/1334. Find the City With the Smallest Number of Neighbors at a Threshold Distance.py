class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        #initialize the distance matrix
        dist = [[float('inf')]*n for _ in range(n)]


        #the distance from the node to itself will be 0
        for i in range(n):
            dist[i][i] = 0

        #fill the initial distance from the provided weight
        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w


        #flyod warshell algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]  = min(dist[i][j], dist[i][k]+dist[k][j])


        smallest_city  = -1 
        smallest_count  = n

        for i in range(n):
            count = 0
            for j in range(n):
                if i!=j and dist[i][j]<= distanceThreshold:
                    count +=1


            if count <= smallest_count:
                smallest_count = count
                smallest_city = i


        return smallest_city

        