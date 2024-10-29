class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count_secondes = 0 
        for i in range(len(points)-1):
            x = points[i][0]
            y = points[i][1]
            while x!=points[i+1][0] and y!=points[i+1][1]:
                if x > points[i+1][0] and y > points[i+1][1]:
                    x-=1
                    y-=1
                    count_secondes+=1
                if x < points[i+1][0] and y > points[i+1][1]: 
                    x+=1
                    y-=1
                    count_secondes+=1
                    
                if x > points[i+1][0] and y < points[i+1][1]:
                    y+=1
                    x-=1
                    count_secondes+=1
                if x < points[i+1][0] and y < points[i+1][1]:
                    x+=1
                    y+=1
                    count_secondes+=1
            while y!=points[i+1][1]:        
                if x==points[i+1][0] and y > points[i+1][1]:
                    y-=1
                    count_secondes+=1
                if x==points[i+1][0] and y < points[i+1][1]:
                    y+=1
                    count_secondes+=1
            while x!=points[i+1][0]:        
                if x > points[i+1][0] and y==points[i+1][1]:
                    x-=1 
                    count_secondes+=1
                if x < points[i+1][0] and y==points[i+1][1]:  
                    x+=1
                    count_secondes+=1
        return count_secondes              
            
        
        