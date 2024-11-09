class MinStack:

    def __init__(self):
        self.s = []
        self.t = []
        
    def peek(self,stack):
        return stack[-1] if stack else None
    
    
    def push(self, val: int) -> None:
        self.s.append(val)
        if  self.t == [] or  val < self.peek(self.t):
            self.t.append(val)
        else:
            self.t.append(self.peek(self.t))
            
            

    def pop(self) -> None:
        if self.s:
            self.s.pop()
            self.t.pop()
        

    def top(self) -> int:
        return self.peek(self.s)

    def getMin(self) -> int:
        return self.peek(self.t)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()