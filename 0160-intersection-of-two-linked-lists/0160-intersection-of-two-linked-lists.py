# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # This is O(n) time and space complexity
        #stock_memory_nodes = set()
        #while headA:
        #    stock_memory_nodes.add(headA)
        #    headA = headA.next
        #while headB:
        #    if headB in stock_memory_nodes:
        #        return headB
        #    else:
        #        headB = headB.next
        #return   
        
        #what about O(1) space complexity ?
        def get_length(head):
            counter = 0
            while head:
                counter+=1
                head = head.next
            return counter
        
        lenA = get_length(headA)
        lenB = get_length(headB)
        
        while (lenA>lenB):
            lenA-=1
            headA = headA.next
        while (lenB>lenA):
            lenB-=1
            headB = headB.next
        
        while headA!=headB:
            headA = headA.next
            headB = headB.next
            if not headA or not headB:
                return
        return headA
    
            
                
        