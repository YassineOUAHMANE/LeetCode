class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # This is O(n) time O(1) space complexity solution  
            res = []
            for i in range(len(nums)):
                existed = abs(nums[i]) - 1
                if nums[existed] > 0:
                    nums[existed] *= -1
           
            for i,num in enumerate(nums):
                if num > 0:
                    res.append(i+1)
            return res        
                    
                    
                    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # This is O(n) time O(n) space complexity solution
        
            #missing_numbers = []
            #set_nums = set(nums)
            #for num in range(1,len(nums)+1):
            #    if  num not in set_nums:
            #        missing_numbers.append(num)
            #return missing_numbers   