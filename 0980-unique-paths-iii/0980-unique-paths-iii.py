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
        start,end,empty_cells = find_start_end_position_and_empty_cells(grid)
        valid_path = [0]
        def dfs(current,end,remaining_cells,visited_cells,grid):
            if current == end and remaining_cells == 0 :
                valid_path[0]+=1
                return
            
            for tup in directions:
                r,c = tup
                nr,nc = current[0]+r,current[1]+c
                if 0<=nr<len(grid) and  0<=nc<len(grid[0]) and grid[nr][nc]!=-1 and (nr,nc) not in visited_cells:
                    new_position = (nr,nc)
                    visited_cells.add(new_position)
                    dfs(new_position,end,remaining_cells-1,visited_cells,grid)
                    visited_cells.remove(new_position)
                
        visited_cells = {start}        
        dfs(start,end,empty_cells+1,visited_cells,grid)
        return valid_path[0]
                