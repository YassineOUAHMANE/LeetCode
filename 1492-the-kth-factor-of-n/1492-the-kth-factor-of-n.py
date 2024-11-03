class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        list_all_factors = []
        for i in range(1,n+1):
            if n%i==0:
                list_all_factors.append(i)
                if len(list_all_factors) == k:
                    return list_all_factors[-1]
        return -1        
            
        
        
        