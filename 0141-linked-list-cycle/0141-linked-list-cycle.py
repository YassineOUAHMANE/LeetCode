# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #This is O(n) time and O(1) space complexity
        #We will use fast and slow pointer to solve this problem
        slow,fast =head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        return False    
        
        
        #this is O(n) time and space complexity
        #if not head:
        #    return False
        #if head.next == None:
        #    return False
        #visited_nodes = []
        #while head not in visited_nodes:
        #    visited_nodes.append(head)
        #    if head.next:
        #        head = head.next
        #    else:
        #        return False      
        #return True
        
            
            
                
                
        
        