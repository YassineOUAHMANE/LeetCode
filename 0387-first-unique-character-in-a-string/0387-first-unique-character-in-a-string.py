from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = Counter(s)
        for key,value in hash_map.items():
            if value == 1:
                return s.index(key)
        return -1    
            
            
        
        