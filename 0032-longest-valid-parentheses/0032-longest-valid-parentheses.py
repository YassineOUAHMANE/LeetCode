class Solution:
    def longestValidParentheses(self, s: str) -> int: 
        #if not s:
        #    return 0
        #longest_one = 0 
        #stack = [-1]
        #for i,el in enumerate(s):
        #    if el == '(':
        #        stack.append(i)
        #    else:
        #        stack.pop()
        #        if not stack:
        #            stack.append(i)
        #        else:
        #            longest_one = max(longest_one,i-stack[-1])
        #        
        #return longest_one
        
            if not s:
                return 0

            def find_longest(s, direction):
                left_counter, right_counter, longest = 0, 0, 0
                iterable = range(len(s)) if direction == "left" else range(len(s) - 1, -1, -1)

                for i in iterable:
                    if s[i] == '(':
                        left_counter += 1
                    else:
                        right_counter += 1

                    if left_counter == right_counter:
                        longest = max(longest, left_counter + right_counter)
                    elif (right_counter > left_counter and direction == "left") or (left_counter > right_counter and direction == "right"):
                        left_counter, right_counter = 0, 0
                    

                return longest

            # Two passes: left-to-right and right-to-left
            longest_from_left = find_longest(s, "left")
            longest_from_right = find_longest(s, "right")

            return max(longest_from_left, longest_from_right)

        
                
        
     
    
    
        
        
        
        
        
        