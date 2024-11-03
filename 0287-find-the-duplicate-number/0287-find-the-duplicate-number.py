class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
         # O(1) space complexity without modifying the array
         #Convert a problem to a linkedlist problem 
        slow,fast = nums[0],nums[nums[0]]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow    
         
        
        
        
        
        
        
        
        
        #This solution is O(n)  time and  space complexity
        #seen = set()
        #for el in nums:
        #    if el in seen:
        #        return el 
        #    else:
        #        seen.add(el)
                           
        #let's find a O(1) space complexity solution modifying the array
        #for i in range(len(nums)):
        #    index = abs(nums[i]) - 1
        #    if nums[index] < 0:
        #        return abs(nums[i])
        #    else:
        #        nums[index] = -nums[index]
        
        
            
        