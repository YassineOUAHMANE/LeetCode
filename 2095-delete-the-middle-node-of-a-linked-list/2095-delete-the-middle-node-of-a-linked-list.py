# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_middle_node(head):
            if not head:
                return head 
            slow,fast = head,head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        def remove_node(head,node):
            dummy = ListNode(0)
            dummy.next = head
            prev = dummy 
            current = head
            while current!=node:
                prev = current
                current = current.next
            
            prev.next = current.next
            current.next = None
            return dummy.next
        node = get_middle_node(head)
        return remove_node(head,node)
                
        