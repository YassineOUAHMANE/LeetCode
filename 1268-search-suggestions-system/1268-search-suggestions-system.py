class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Design a system that returns at most three products
        # Commom prefix
        # sorted lexicographically products
        products.sort()
        def binary_search(List,x,start=0,end=None):
            if end==None:
                end = len(List)
            while start < end:
                mid = (start+end)//2
                if List[mid] < x:
                    start = mid + 1
                else:
                    end = mid 
            return start
        propositions = []
        prefix = ''
        for el in searchWord:
            prefix += el
            
            start_position = binary_search(products,prefix)
            suggestions = []
            for i in range(start_position,min(start_position+3,len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            propositions.append(suggestions)     
        return propositions
            
                    
        
        
        
        
        
        
        
        
        
        #products.sort()
        #propositions = []
        #s = ''
        #for el in searchWord:
        #    s+=el
        #    list_words = []
        #    for word in products:
        #        if word.startswith(s):
        #            list_words.append(word)
        #    if len(list_words) >= 3:
        #         propositions.append(list_words[:3])
        #    else:
        #         propositions.append(list_words)        
        #return propositions            
            
            
                                  
                
                
            
            
            
            
            
        