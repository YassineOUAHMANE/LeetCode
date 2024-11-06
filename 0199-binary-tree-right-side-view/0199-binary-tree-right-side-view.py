from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_level = 0
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def my_right_view(self,root: Optional[TreeNode],level:int,result:List[int]) -> List[int]:
            if not root:
                return []
            
            if self.max_level < level:
                result.append(root.val)
                self.max_level = level
                
            my_right_view(self,root.right,level+1,result)
            my_right_view(self,root.left,level+1,result)
            return result
        return my_right_view(self,root,1,[])
            
            
        
    """                                                        1       LEVEL = 0
                                                            2     3    Level = 1
                                                          5   6  2  1  lEVEL = 2
    1    maxlevel = 3                                   5   3          Level = 3
  2   3  level = 3
7   5             <-- p            <  >
    
    output : 1 3 5
    
    
    
    
    
    
    
    
     """


    