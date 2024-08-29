class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        #find the cols and rows length
        rows , cols = len(grid) , len(grid[0])


        #running the depth first search 
        def dfs(r,c):

            if r not in range(rows) or c not in range(cols) or grid[r][c]!=1 or (r,c) in visited:
                return 0


            visited.add((r,c))

            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c-1)+dfs(r,c+1)


        visited = set()
        max_area = 0


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    area = dfs(r,c)
                    max_area = max(max_area , area)


        return max_area
        