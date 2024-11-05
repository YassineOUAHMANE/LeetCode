# Definition for singly-linked list.
  #class ListNode:
  #       def __init__(self, val=0, next=None):
  #          self.val = val
  #          self.next = next
            
            
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
        # Recursive apprroach 
        if not head or not head.next:
            return head
        
        reversed_list = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return reversed_list
        
        
        
        
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        #Iterative approach without creating a new linkedlist (no extra space)
        #if not head:
        #    return head
        #else:
        #    prev = None
        #    current = head
        #    while current:
        #        nxt = current.next
        #        current.next = prev
        #        prev = current
        #        current = nxt
        #    return prev
            
            
            
            
    
            #Using a stack data structure (extra space) it won't work here memory excedeed
            #if not head:
            #    return head
            #stack = []
            #while head:
            #    stack.append(head)
            #    head = head.next
            #dummy = ListNode(0)
            #current = dummy
            #while stack:
            #    current.next = stack.pop()
            #    current = current.next
            #return dummy.next
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
                
               
            
                
                
                
                
                
                
                
                
                
            
                
        