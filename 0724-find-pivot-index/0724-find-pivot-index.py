class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            
            rightsum = total_sum - leftsum  - nums[i]
            if leftsum == rightsum :
                return i
            leftsum+=nums[i]
        return -1    
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #if len(nums)<=1:
        #    return -1
        #pivotindex = -1
        #
        #for pivot in range(len(nums)):
        #    leftsum = 0
        #    rightsum = 0
        #    #Calculate the leftsum
        #    for left in range(0,pivot):                       # This is a O(n^2) time complexity solution 
        #        leftsum+=nums[left]
        #    #Calculate the rightsum
        #    for right in range(pivot+1,len(nums)):
        #        rightsum+=nums[right]
        #        
        #    if leftsum == rightsum :
        #        pivotindex = pivot
        #        return pivotindex   
        #return  pivotindex 
            
                        
            
               
                
            
            
            
        
            
        