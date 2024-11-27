class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for x in range(1,2**n):
            res+=[x^(x>>1)]
        return res
       
                
            
        
        
        
        