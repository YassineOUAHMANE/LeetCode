class Solution:
    def partitionString(self, s: str) -> int:
        #The characters in each substring are unique 
        #No letter appears in a substring more than once
        unique_substring = set()
        counter = 0
        for el in s:
            if el not in unique_substring:
                unique_substring.add(el)
            else:
                counter+=1
                unique_substring = set()
                unique_substring.add(el)
        counter+=1        
        return counter        
                
        
        