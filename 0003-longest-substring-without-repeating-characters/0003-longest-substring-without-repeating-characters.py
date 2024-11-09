class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        element_visited = {}
        start = 0
        max_length = 0
        for i,el in enumerate(s):
            if el in element_visited and element_visited[el] >= start:
                start = element_visited[el] + 1
            element_visited[el] = i

            max_length = max(max_length,i-start+1)

        return max_length    
                
                
                
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        