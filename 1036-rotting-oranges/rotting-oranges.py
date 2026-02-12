class Solution(object):
     def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        copy = deepcopy(grid)
        
        fresh_cnt = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if copy[r][c] == 2:
                    queue.append((r,c))
                elif copy[r][c] == 1:
                    fresh_cnt += 1
        
        minutes = 0
        while len(queue) != 0 and fresh_cnt > 0:
            minutes += 1
            rotten = len(queue)
            for _ in range(rotten):
                i, j = queue.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + dx, j + dy
                    if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                        continue
                    if copy[ni][nj] == 0 or copy[ni][nj] == 2:
                        continue
                    else:
                        fresh_cnt -= 1
                        copy[ni][nj] = 2
                        queue.append((ni, nj))
        
        if fresh_cnt > 0:
            return -1
        return minutes