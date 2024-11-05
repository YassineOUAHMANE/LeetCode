class Solution:
    def myPow(self, x: float, n: int) -> float:
        # recursive version
        
            def rec(x,n):
                if x == 0 : return 0
                if n == 0 : return 1
                res=rec(x,n//2)
                res*=res
                return res * x if n%2 else res
                   
                 
            
            res = rec(x,abs(n))
            return res if n > 0 else 1/res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #if n < 0:
        #    x = (1/x)
        #    n = -n
        #
        #result = 1
        #current = x
        #while n > 0:
        #    if n%2 == 1:
        #        result = current * result
        #    current *=current
        #    n//=2
        #return result    
                
            
        