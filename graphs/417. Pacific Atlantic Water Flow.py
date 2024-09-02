class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        #finding the length of the row and the column
        rows , cols = len(heights) , len(heights[0])

        pac , atl = set() , set()

        def dfs(r,c,visit,prev_height):

            if (r not in range(rows)
            or c not in range(cols)
            or heights[r][c]<prev_height
            or (r,c) in visit):

               return 

            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        #going for top and bottom 
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])


        #going for right and left
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1]) 


        #going into the functions 
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])


        return result


        