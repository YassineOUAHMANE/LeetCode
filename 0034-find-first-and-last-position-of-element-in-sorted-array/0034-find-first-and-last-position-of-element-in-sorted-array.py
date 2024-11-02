class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_start(nums,target):
            if nums[0] == target :
                 return 0
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid  = (left + right) // 2
                if nums[mid] == target and  nums[mid-1] < target:
                    return mid 
                elif nums[mid] >= target:
                    right = mid - 1
                else:    
                    left = mid + 1
            return -1
        def find_end(nums,target):
            if nums[-1] == target :
                 return len(nums)-1
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid  = (left + right) // 2
                if nums[mid] == target and  nums[mid+1] > target:
                    return mid 
                elif nums[mid] > target:
                    right = mid - 1
                else: 
                    left  = mid + 1
                    
                    
            return -1
        
        if len(nums) == 0 or  target < nums[0] or nums[-1] < target:
            return [-1,-1]
        start = find_start(nums,target)
        end   = find_end(nums,target)
        return [start,end]
        
                    
        