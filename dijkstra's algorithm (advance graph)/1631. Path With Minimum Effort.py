class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows, cols = len(heights) , len(heights[0])

        directions = [(0,1),(0,-1),(-1,0),(1,0)]

        efforts = [[float('inf')]*cols for _ in range(rows)]
        efforts[0][0] = 0

        min_heap = [(0,0,0)]

        while min_heap:

            curr_efforts , r , c  = heapq.heappop(min_heap)

            if r == rows - 1 and c == cols -1:
                return curr_efforts


            for dx ,dy in directions:
                nx , ny = dx + r , dy + c

                if nx in range(rows) and ny in range(cols):

                    new_effort = max(curr_efforts , abs(heights[nx][ny] - heights[r][c]))

                    if new_effort < efforts[nx][ny]:
                        efforts[nx][ny] = new_effort
                        heapq.heappush(min_heap,(new_effort,nx,ny))


        return -1


        