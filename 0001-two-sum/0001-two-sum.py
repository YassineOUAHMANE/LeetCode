class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums) - 1
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        nums_with_indices.sort()  # Sort by the values
        while left < right:
            if nums_with_indices[left][0] + nums_with_indices[right][0] < target:
                left+=1
            elif nums_with_indices[left][0] + nums_with_indices[right][0] > target:
                right-=1
             
            else:
                return [nums_with_indices[left][1],nums_with_indices[right][1]]
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #hash_map = {}
        #result = []
        #for i,el in enumerate(nums):
        #    if target - el in hash_map:
        #            result.append(hash_map[target-el])
        #            result.append(i)   
        #    else:
        #        hash_map[el] = i
        #return result        
                
                
                