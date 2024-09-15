class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        '''
        Longest increasing using Graph this is kind of topological sort problem 
        '''

        rows ,  cols  = len(matrix) , len(matrix[0])
        dp = {}

        #constructing the depth first search 
        def dfs(r , c, prevValue):
            
            if ((r not in range(rows))
                or (c not in range(cols))
                or (matrix[r][c]<= prevValue)):

                return 0

            if (r,c) in dp:
                return dp[(r,c)]

            res = 1 
            res = max(res , 1+ dfs(r+1,c,matrix[r][c])) 
            res = max(res , 1+ dfs(r-1,c,matrix[r][c]))
            res = max(res , 1+ dfs(r,c+1,matrix[r][c])) 
            res = max(res , 1+ dfs(r,c-1,matrix[r][c]))

            dp[(r,c)] = res
            return res


        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1)

        return max(dp.values())