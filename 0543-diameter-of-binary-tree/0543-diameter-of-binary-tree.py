# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_length = 0  # Initialize max_length as an instance variable

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calculate_longest_path(node):
            if not node:
                return 0  # Return 0 for null nodes
            
            # Recursive depth-first search
            left_length = calculate_longest_path(node.left)
            right_length = calculate_longest_path(node.right)
            
            # Update max_length to the largest diameter found so far
            self.max_length = max(self.max_length, left_length + right_length)
            
            # Return the longest path from this node to its children
            return max(left_length, right_length) + 1

        calculate_longest_path(root)
        return self.max_length