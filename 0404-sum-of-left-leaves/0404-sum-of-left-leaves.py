# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
            def mysum(root,is_left):
                if not root:
                    return 0
                if  not root.left and not root.right and is_left:
                    return root.val
                left_sum = mysum(root.left,is_left=True) 
                right_sum= mysum(root.right,is_left=False)
                return left_sum + right_sum
            return mysum(root,is_left=False)       
            
            
        
        
        