class Solution:
    def decodeString(self, s: str) -> str:
        stack_numbers = []
        stack_letters = []
        word = ""
        number = 0

        for el in s:
            if el.isdigit():
                # Accumulate digits for numbers greater than single digits
                number = number * 10 + int(el)
            elif el == '[':
                # Push the current number and word to their respective stacks
                stack_numbers.append(number)
                stack_letters.append(word)
                number = 0
                word = ""
            elif el == ']':
                # Pop the last number and word from the stack
                num = stack_numbers.pop()
                prev_word = stack_letters.pop()
                # Repeat 'word' num times and concatenate with prev_word
                word = prev_word + word * num
            else:
                # Accumulate characters in the current word
                word += el

        return word
 
        
        
                      
                
                
        