
class Solution(object):
    def backtrack(self, row, n, cols, posDiag, negDiag, board, result):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        
        for col in range(n):
            if col in cols or (row - col) in posDiag or (row + col) in negDiag:
                continue
            
            cols.add(col)
            posDiag.add(row - col)
            negDiag.add(row + col)
            board[row][col] = 'Q'
            
            self.backtrack(row + 1, n, cols, posDiag, negDiag, board, result)
            
            cols.remove(col)
            posDiag.remove(row - col)
            negDiag.remove(row + col)
            board[row][col] = '.'
    
    def solveNQueens(self, n):
        cols = set()
        posDiag = set()
        negDiag = set()
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        
        self.backtrack(0, n, cols, posDiag, negDiag, board, result)
        return result
        