class Solution:
    def partitionString(self, s: str) -> int:
        #The characters in each substring are unique 
        #No letter appears in a substring more than once
        
#let's do another approach using a bit mask
        bitmask = 0
        counter = 0
        for ch in s:
            bit_position = ord(ch) - ord("a")
            
            if bitmask & (1 << bit_position)!=0:
                counter += 1
                bitmask = 0
            
            bitmask|=(1 << bit_position)
        return counter +  1    
    
        #We know that the set cannot contain more than 26 letters in alphabet so space complexity is O(1) and time complexity is O(1)
        #unique_substring = set()
        #counter = 0
        #for el in s:
        #    if el not in unique_substring:
        #        unique_substring.add(el)
        #    else:
        #        counter+=1
        #        unique_substring = set()
        #        unique_substring.add(el)
        #counter+=1        
        #return counter        
              
        
        