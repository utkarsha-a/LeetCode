# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        tail = head
        for i in range(k):
            if not tail:
                return head
            tail = tail.next

        def rev(cur, end):
            node  = None
            while cur!=end:
                nxt = cur.next
                cur.next = node
                node = cur
                cur = nxt
            return node

        new_head = rev(head, tail)
        head.next = self.reverseKGroup(tail, k)

        return new_head

        
        