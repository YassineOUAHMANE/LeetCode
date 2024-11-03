class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for el in nums:
            if el in seen:
                return el 
            else:
                seen.add(el)
                
                            
        
        
        
            
        