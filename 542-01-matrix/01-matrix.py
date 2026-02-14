class Solution(object):
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        distance = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append([r, c, 0])
                    visited[r][c] = 1
                    distance[r][c] = 0
        
        while queue:
            i, j, d = queue.popleft()
            
            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                ni, nj = i + dx, j + dy
                
                if ni >= rows or ni < 0 or nj >= cols or nj < 0:
                    continue
                if visited[ni][nj] == 1:
                    continue
                
                queue.append([ni, nj, d + 1])
                visited[ni][nj] = 1
                distance[ni][nj] = d + 1
        
        return distance



