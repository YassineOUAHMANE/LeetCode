class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        new_code = [0 for _ in range(n)]
        l = 0
        if k==0:
            return new_code
        curr_sum = 0
        for r in range(n+abs(k)):
            curr_sum += code[r%n]
            if r - l + 1 > abs(k):
                curr_sum-=code[l%n]
                l = (l+1)%n
            if r - l + 1 == abs(k):
                if k > 0:
                    new_code[(l-1)%n] = curr_sum
                elif k < 0:
                    new_code[(r+1)%n] = curr_sum
        return new_code
                    
                    
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #new_code = [0 for _ in range(len(code))]
        #for i in range(len(code)):
        #    if k==0:
        #        return new_code
        #    elif k > 0:
        #        start = (i+1)%len(code)
        #        iteration = 0
        #        while iteration < k  :
        #            new_code[i] += code[start]
        #            start = (start + 1)%len(code)
        #            iteration+=1
        #    else:
        #        start = (i-1)%len(code)
        #        iteration = 0   
        #        while iteration < abs(k):
        #            new_code[i]+=code[start]
        #            start = (start-1)%len(code)
        #            iteration+=1
        #return new_code              
               
                
            
            
        
        