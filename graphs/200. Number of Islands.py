class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        '''
        This is the typicall graph problem 
        if there is a graph poblem visited is important
        '''
        
        ROWS , COLS = len(grid) , len(grid[0])


        def bfs(r,c):


            queue = deque([(r,c)])

            visited.add((r,c))


            while queue:
                r,c = queue.popleft()
                
                directions =[(1,0),(0,1),(-1,0),(0,-1)]

                for dr , dc in directions:
                    nr , nc  = dr+r , dc+c

                    if (nr,nc) not in visited and nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] =="1":
                        queue.append((nr,nc))
                        visited.add((nr,nc))



        #base condition to travel with the matrix
        visited = set()
        island=0
        for r in range(ROWS):
            for c in range(COLS):
                if(r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    island+=1


        return island

