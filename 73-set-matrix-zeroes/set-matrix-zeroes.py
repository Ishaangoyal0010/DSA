class Solution(object):
    def markinf(self,matrix,row,col):
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(0,rows):
            if matrix[i][col]!=0:
                matrix[i][col]=float('inf')
        for j in range(0,cols):
            if matrix[row][j]!=0:
                matrix[row][j]=float('inf')

    def setZeroes(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(0,rows):
            for j in range(0,cols):
                if matrix[i][j]==0:
                    self.markinf(matrix,i,j)

        for i in range(0,rows):
            for j in range(0,cols):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=0
        

                    

        