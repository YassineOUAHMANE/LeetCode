class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If lengths are not the same, the strings can't be made equal
        if len(word1) != len(word2):
            return False
        
        # Count character occurrences in both words
        occurences_word1 = {}
        occurences_word2 = {}
        for el in word1:
            occurences_word1[el] = occurences_word1.get(el, 0) + 1
        for el in word2:
            occurences_word2[el] = occurences_word2.get(el, 0) + 1
        
        # Check if the sets of characters are the same
        if set(occurences_word1.keys()) != set(occurences_word2.keys()):
            return False
        
        # Check if the frequency distributions are the same
        if sorted(occurences_word1.values()) != sorted(occurences_word2.values()):
            return False
        
        return True
