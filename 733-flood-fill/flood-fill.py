class Solution(object):
    def floodFill(self, image, sr, sc, color):
        rows=len(image)
        cols = len(image[0])
        grid = deepcopy(image)

        queue = deque()
        queue.append((sr,sc))
        old_colour=grid[sr][sc]
        grid[sr][sc]=color

        if old_colour==color:
            return grid


        while len(queue) != 0:
            new_colour = len(queue)
            for _ in range(new_colour):
                i, j = queue.popleft()
                for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    ni,nj = i+dx , j+dy
                    if ni<0 or ni==rows or nj<0 or nj == cols:
                        continue
                    if grid[ni][nj]!=old_colour or grid[ni][nj]==color:
                        continue
                    else:
                        grid[ni][nj]=color
                        queue.append((ni,nj))
        return grid