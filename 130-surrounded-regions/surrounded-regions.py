class Solution(object):
    def dfs(self, r ,c , rows,cols, board,visited):
        if r<0 or c<0 or r>=rows or c>=cols:
            return 
        if board[r][c]=='X':
            return
        if visited[r][c]==1:
            return
        visited[r][c]=1
        self.dfs( r+1 ,c , rows,cols, board,visited)
        self.dfs( r-1 ,c , rows,cols, board,visited)
        self.dfs( r ,c+1 , rows,cols, board,visited)
        self.dfs( r ,c-1 , rows,cols, board,visited)

    def solve(self, board):
        rows=len(board)
        cols=len(board[0])
        visited = [[0 for _ in range(cols)]for _ in range (rows)]

        for r in  range (rows):
            for c in range (cols):
                if r==0 or c == 0 or r == rows-1 or c==cols-1:
                    if board[r][c]=='O':
                        if visited[r][c]==0:
                            self.dfs(r,c, rows,cols, board,visited)

        for r in  range (rows):
            for c in range (cols):
                if board[r][c]=='O' and visited[r][c]==0:
                   board[r][c]='X'  
        return board

        