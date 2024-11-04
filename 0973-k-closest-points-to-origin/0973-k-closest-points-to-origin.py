from math import sqrt
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        closest_points = defaultdict(list)
        for point in points:
            euclidien_d = sqrt(point[0]**2+point[1]**2)
            closest_points[euclidien_d].append(point)
        list_closest_points = sorted(closest_points.items())  
        for i in range(k):
            if i >= len(list_closest_points):
                break
            result.append(list_closest_points[i][1])
        return sum(result,[])[:k]    
            
            
        
        