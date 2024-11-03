# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stock_memory_nodes = set()
        while headA:
            stock_memory_nodes.add(headA)
            headA = headA.next
        while headB:
            if headB in stock_memory_nodes:
                return headB
            else:
                headB = headB.next
        return        
            
                
        