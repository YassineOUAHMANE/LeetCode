from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagm_dict = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagm_dict[sorted_word].append(word)
        return list(anagm_dict.values())    
                
        