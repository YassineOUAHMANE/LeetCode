# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow,fast = head,head
        while  fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if not fast.next or not fast.next.next:
            return 
        slow = head
        while (slow!=fast):
            fast = fast.next
            slow = slow.next
        return slow    
        
            
            
            
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        #This solution is O(n) space complexity and O(n) time complexity
        #if not head: 
        #    return 
        #visited_nodes = {}
        #while head.next:
        #    if head in visited_nodes:
        #        return head
        #    visited_nodes.add(head)
        #    head = head.next
        #return 