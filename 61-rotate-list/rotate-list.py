# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        len = 1
        while curr.next:
            curr = curr.next
            len += 1
        curr.next = head

        k = len - (k % len)
        while k>0:
            curr = curr.next
            k -= 1
        
        newhead = curr.next
        curr.next = None
        return newhead
        