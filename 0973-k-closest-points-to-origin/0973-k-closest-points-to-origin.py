from math import sqrt
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        distances = []
        for x,y in points:
            distance = sqrt(x**2+y**2)
            distances.append([distance,x,y])
        distances.sort(key=lambda x:-x[0])
        while k > 0:
            result.append(distances.pop()[1:])
            k-=1
        return result    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #result = []
        #closest_points = defaultdict(list)
        #for point in points:
        #    euclidien_d = sqrt(point[0]**2+point[1]**2)
        #    closest_points[euclidien_d].append(point)
        #list_closest_points = sorted(closest_points.items())  
        #for i in range(k):
        #    if i >= len(list_closest_points):
        #        break
        #    result.append(list_closest_points[i][1])
        #return sum(result,[])[:k]    
            
            
        
        