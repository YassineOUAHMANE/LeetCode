class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {chr(i):0 for i in range(ord('a'),ord('z')+1)}
        s = s.lower()
        t = t.lower()
        s = s.replace(" ","")
        t = t.replace(" ","")
        for el in s:
            hash_map[el]+=1
        for el in t:
            hash_map[el]-=1
        for value in hash_map.values():
            if value!=0:
                return False
        return True
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #return sorted(s) == sorted(t)    #O(nlog(n)) time complexity