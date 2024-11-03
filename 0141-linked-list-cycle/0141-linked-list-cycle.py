# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head.next == None:
            return False
        visited_nodes = []
        while head not in visited_nodes:
            visited_nodes.append(head)
            if head.next:
                head = head.next
            else:
                return False
                
        return True
        
            
            
                
                
        
        