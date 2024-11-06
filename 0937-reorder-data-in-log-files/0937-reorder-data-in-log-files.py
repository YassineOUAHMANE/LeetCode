class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
            logs_digits = []
            logs_letters = []
            for el in logs:
                if el[-1].isdigit():
                    logs_digits+=[el]
                else:
                    logs_letters.append(el)
            logs_letters.sort(key = lambda x: (x.split(" ",1)[1],x.split(" ",1)[0]))    
            
            return logs_letters + logs_digits
                    
            
        