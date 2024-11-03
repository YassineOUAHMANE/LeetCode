class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #let's find a O(1) space complexity solution modifying the array
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                return abs(nums[i])
            else:
                nums[index] = -nums[index]
            
        
        
        
        
        
        
        
        
        
        
        
        
       
    
    
        #This solution is O(n)  time and  space complexity
        #seen = set()
        #for el in nums:
        #    if el in seen:
        #        return el 
        #    else:
        #        seen.add(el)
                           
        
        
        
            
        