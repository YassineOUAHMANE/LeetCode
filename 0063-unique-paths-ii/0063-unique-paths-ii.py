class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(m):
             for j in range(n):
                    if obstacleGrid[i][j] == 1:
                            obstacleGrid[i][j] = 'o'
                    elif j==0 and i - 1 > 0 and obstacleGrid[i-1][j]=='o':
                        obstacleGrid[i][j] = 'o'
                    elif i==0 and j - 1 > 0 and obstacleGrid[i][j-1] == 'o':
                        obstacleGrid[i][j] = 'o'
                    elif i==0 or j==0:
                            obstacleGrid[i][j] = 1
                            
                    elif obstacleGrid[i-1][j]!='o'and obstacleGrid[i][j-1]!='o':
                            obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                    elif obstacleGrid[i-1][j] == 'o':
                           obstacleGrid[i][j] = obstacleGrid[i][j-1]
                    else:
                            obstacleGrid[i][j] = obstacleGrid[i-1][j]
        if obstacleGrid[m-1][n-1]=='o':
            return 0
        return obstacleGrid[m-1][n-1]                
                
                    
                    
                    
            
        