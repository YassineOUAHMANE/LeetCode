class Solution:
    def count(count_say):
        next_count_say = ""
        counter = 1 
        for i in range(1,len(count_say)):
            if count_say[i]!= count_say[i-1]:
                next_count_say += str(counter) + count_say[i-1]
                counter = 1 
            else:
                counter +=1
        next_count_say += str(counter)  + count_say[-1]
        return next_count_say
        
    
    
    
    def countAndSay(self, n: int) -> str:
        count_say = "1"
        if n == 1:
            return count_say
        for i in range(2,n+1):
            count_say = Solution.count(count_say)
        return count_say    
            
        
        
        
            
            
            
            
        