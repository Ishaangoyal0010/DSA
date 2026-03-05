class Solution(object):
    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])
        old_color = image[sr][sc]

        if old_color == color:
            return image
        
        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = color
        
        while queue:
            i, j = queue.popleft()
            
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ni, nj = i + dx, j + dy
                
                # Check boundaries
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                    continue
                
                # Only fill if it matches the original color
                if image[ni][nj] != old_color:
                    continue
                
                # Fill with new color and add to queue
                image[ni][nj] = color
                queue.append((ni, nj))
        
        return image
            