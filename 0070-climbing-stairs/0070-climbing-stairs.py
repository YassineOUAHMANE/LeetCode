from numpy import dot
class Solution:
    def climbStairs(self, n: int) -> int:
        # Starting from the top stairs and ask ourselves how many ways exists to get to the top and descend .
        #back_stairs = [[1],[1]] # There is always one way to get to the top where we are in n and n-1#
        #matrix = [[1,1],[1,0]]
        #for i in range(n-1):
        #    back_stairs = dot(matrix,back_stairs)
        #return int(back_stairs[0][0]) 
        
        back_stairs = [1]*n
        for i in range(1,n):
            back_stairs[i] = back_stairs[i-1]+back_stairs[i-2]
        return back_stairs[n-1]
            
            
            