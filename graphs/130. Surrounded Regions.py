class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #this the typical graph problem

        ROWS , COLS = len(board) , len(board[0])

        #solving using depth first search method
        def dfs(r,c):

            if (r<0 or r== ROWS or c <0 or c==COLS or board[r][c]!='O'):

                return 
            
            #converting the the 'O' to 'T'

            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        #mark all the borders
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O' and (r in [0,ROWS-1] or c in [0 , COLS-1]):
                    dfs(r,c)

        
        #Convert all the O to X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c] = "X"

       
        #convert all the reamining T to O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        
        