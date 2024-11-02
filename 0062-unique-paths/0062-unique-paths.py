class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Declare matrix (m,n)
        dp = [[0 for i in range(n)] for j in range(m)] # O(n*m) space complexity
        for i in range(m):
            for j in range(n):        #Time complexity O(n*m)
                if i==0 or j==0:   
                    dp[i][j] = 1
                else:
                               #Left side   #above side
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1] 

    


        
        
         
            
            
            
            
        
        