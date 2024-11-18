class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        new_code = [0 for _ in range(len(code))]
        for i in range(len(code)):
            if k==0:
                return new_code
            elif k > 0:
                start = (i+1)%len(code)
                iteration = 0
                while iteration < k  :
                    new_code[i] += code[start]
                    start = (start + 1)%len(code)
                    iteration+=1
            else:
                start = (i-1)%len(code)
                iteration = 0   
                while iteration < abs(k):
                    new_code[i]+=code[start]
                    start = (start-1)%len(code)
                    iteration+=1
        return new_code              
                
                
                
            
            
        
        