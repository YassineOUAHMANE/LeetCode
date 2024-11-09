class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s = s.lower()
        p = p.lower()
        s = s.replace(" ","")
        p = p.replace(" ","")
        find_anagrams = []
        if p=="" or s=="":
            return []
        if len(p) > len(s):
            return []
        p_hash_map = {}
        s_hash_map = {}
        for el in p:
            p_hash_map[el] = 1 + p_hash_map.get(el,0)
        l = 0
        for r  in range(len(s)):
            s_hash_map[s[r]] = 1 + s_hash_map.get(s[r],0)
            if r - l + 1 == len(p): 
                if s_hash_map == p_hash_map:
                    find_anagrams.append(l)
            
                s_hash_map[s[l]]-=1
                if s_hash_map[s[l]] == 0:
                    s_hash_map.pop(s[l])
                l+=1
        return find_anagrams
                           
                    
                
                
            
        