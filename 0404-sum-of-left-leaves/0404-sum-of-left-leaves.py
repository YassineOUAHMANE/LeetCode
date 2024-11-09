# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
           #ITERATIVE APPROACH
            def is_leaf(root):
                if root.left == None and root.right==None: return True
                else: return False
            if not root:
                return 0
            sum_value = 0 
            queue = [root]
            while queue:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    if is_leaf(node.left):
                        sum_value += node.left.val
                if node.right:
                    queue.append(node.right)
            return sum_value        
                    
                
            
            
         #RECURSIVE APPROACH
            #def mysum(root,is_left):
            #    if not root:
            #        return 0
            #    if  not root.left and not root.right and is_left:
            #        return root.val
            #    left_sum = mysum(root.left,is_left=True) 
            #    right_sum= mysum(root.right,is_left=False)
            #    return left_sum + right_sum
            #return mysum(root,is_left=False)       
            
            
        
        
        