class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = (1/x)
            n = -n
        
        result = 1
        current = x
        while n > 0:
            if n%2 == 1:
                result = current * result
            current *=current
            n//=2
        return result    
                
            
        