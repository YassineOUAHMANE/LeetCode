class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        longest_mountain = 0
        i = 1
        
        while i < n - 1:
            # check if "i" is a peak
            if arr[i-1] < arr[i] > arr[i+1]:
                #Expand left
                left = i - 1
                while left > 0 and arr[left-1] < arr[left]:
                    left-=1
                #Expand right
                right = i + 1
                while right < n-1 and arr[right+1] < arr[right]:
                    right+=1
                
                #Calculate mountain length
                longest_mountain = max(longest_mountain,right-left+1)
                # Move i to the end of current mountain
                i = right
            
            else:
                i+=1
        return longest_mountain       
                    
            
                
                
                
                
                
                
                
        
        