class Solution:
    def spiralOrder(self,matrix: list[list[int]]) -> list[int]:
        spiral_matrix = []
        while matrix:
            spiral_matrix += matrix[0]
            matrix = matrix[1:]
            if not matrix:
                break
            nb_raws = len(matrix)
            for i in range(nb_raws):
                if matrix[i]:
                    spiral_matrix += [matrix[i].pop()]
            while matrix[-1]:
                spiral_matrix += [matrix[-1].pop()]
            matrix = matrix[:-1]    
            nb_raws = len(matrix)    
            for i in range(nb_raws-1,0,-1):
                if matrix[i]:
                    spiral_matrix += [matrix[i].pop(0)]
        
        return spiral_matrix          
                
                
                
            
        
        
        
        
        