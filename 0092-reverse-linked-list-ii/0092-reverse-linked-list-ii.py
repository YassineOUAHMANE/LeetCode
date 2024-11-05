# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        leftpointer = dummy
        current = head
        for _ in range(left-1):
            leftpointer = leftpointer.next
            current     = current.next
        begin_head = current 
        prev = None
        for _ in range(right-left+1):
            nxt = current.next
            current.next =prev 
            prev = current 
            current = nxt
        begin_head.next = current 
        leftpointer.next = prev 
        
        return dummy.next
        
        
            
        
        
        
        
       
        
        
            
                
                
                
                
                
                
                
            
            
        