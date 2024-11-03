class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def find_start_end_position_and_empty_cells(grid):
            empty_cells = 0
            start, end = None, None
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        start = (r, c)
                    elif grid[r][c] == 2:
                        end = (r, c)
                    elif grid[r][c] == 0:
                        empty_cells += 1
            return start, end, empty_cells
        
        start, end, empty_cells = find_start_end_position_and_empty_cells(grid)
        valid_path = [0]  # Use a list to track valid paths as a mutable count
        
        def dfs(current, end, remaining_cells, grid, visited_cells):
            if current == end and remaining_cells == 0:
                valid_path[0] += 1
                return
            
            r, c = current
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                new_position = (nr, nc)
                
                if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and
                        new_position not in visited_cells and grid[nr][nc] != -1):
                    
                    visited_cells.add(new_position)
                    dfs(new_position, end, remaining_cells - 1, grid, visited_cells)
                    visited_cells.remove(new_position)  # Backtrack after returning
        
        visited_cells = set([start])
        dfs(start, end, empty_cells + 1, grid, visited_cells)
        return valid_path[0]

                
                    
                
                
        