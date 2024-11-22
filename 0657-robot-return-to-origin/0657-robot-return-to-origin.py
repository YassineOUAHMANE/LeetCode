class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0 
        for el in moves:
            if el == 'U':
                y+=1
            elif el == 'R':
                x+=1
            elif el == 'L':
                x-=1
            elif el == 'D':
                y-=1
        if x == 0 and y == 0:
            return True 
        return False
             