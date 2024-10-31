class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        final_prefix_commun = first_word
        if first_word == "":
            return ""
        
        for word in strs[1:]:
            i = 0
            prefix_commun = ""
            if word == "":
                return ""
            while word[i] == first_word[i]:
                    prefix_commun+=first_word[i]
                    i+=1
                    if i >= len(word) or i >= len(first_word):
                        break
            if len(prefix_commun) < len(final_prefix_commun):
                final_prefix_commun = prefix_commun
        return final_prefix_commun        
                
            
            
            
            
        
        