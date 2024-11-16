class Solution:
    def longestValidParentheses(self, s: str) -> int: 
        if not s:
            return 0
        longest_one = 0 
        stack = [-1]
        for i,el in enumerate(s):
            if el == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                        longest_one = max(longest_one,i-stack[-1])
                
        return longest_one
            
            
        
     
    
    
        
        
        
        
        
        