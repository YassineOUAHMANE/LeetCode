class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Design a system that returns at most three products
        # Commom prefix
        # sorted lexicographically products
        products = sorted(products)
        propositions = []
        s = ''
        for el in searchWord:
            s+=el
            list_words = []
            for word in products:
                if word.startswith(s):
                    list_words.append(word)
            if len(list_words) >= 3:
                 propositions.append(list_words[:3])
            else:
                 propositions.append(list_words)        
        return propositions            
            
            
                                  
                
                
            
            
            
            
            
        