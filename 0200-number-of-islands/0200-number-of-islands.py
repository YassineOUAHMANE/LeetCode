class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count_lands = 0

        def bfs(r, c):
            grid[r][c] = '0'
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1':
                    bfs(nr, nc)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count_lands += 1  
        
        return count_lands
                    
                    
                
            
            