class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #This is the typical graph problem
        #need to track which orange is fresh

        fresh = 0
        time = 0
        queue = deque()
        visited = set()

        rows , cols = len(grid) , len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    queue.append((r,c))

        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        while queue and fresh >0:

            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr , dc in directions:
                    nr , nc = r + dr , c + dc

                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc]==1:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        fresh-=1


            time+=1

        return time if not fresh else -1


                


                

        