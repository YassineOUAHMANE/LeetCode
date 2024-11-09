class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        start = 0
        longest = 0
        visited_characters = {}
        for i,el in enumerate(s):
            if el in visited_characters:
                #Check if the visited_character is in the current substring
                if visited_characters[el] >= start: 
                    start = visited_characters[el] + 1             
            visited_characters[el] = i        
            longest = max(longest,i-start+1)
        return longest        
                
                
                
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #if not s:
        #    return 0
        #if len(s) == 1:
        #    return 1
        #
        #element_visited = {}
        #start = 0
        #max_length = 0
        #for i,el in enumerate(s):
        #    if el in element_visited and element_visited[el] >= start:
        #        start = element_visited[el] + 1
        #    element_visited[el] = i
#
        #    max_length = max(max_length,i-start+1)
#
        #return max_length    