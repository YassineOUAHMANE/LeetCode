class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) == 1:
            return s
        longest_palindrom = ""
        palindrom_even = ""
        palindrom_odd = ""
        for i in range(len(s)):
            #check for odd palindrom
            low  = i 
            high = i
            while low>=0 and high<len(s) and s[high]==s[low]:
                low-=1
                high+=1
            palindrom_even = s[low+1:high]   
            #check for even palindrom
            low   = i - 1
            high = i
            while low>=0 and high<len(s) and s[high]==s[low] :
                low-=1
                high+=1
            palindrom_odd = s[low+1:high]
            #Update the longest palindrom
            longest_palindrom = max(longest_palindrom,palindrom_odd,palindrom_even,key=len)
        return longest_palindrom
                    

                    
            
                
        
        
