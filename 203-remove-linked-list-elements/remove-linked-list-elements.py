# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        dum = ListNode(0)
        dum.next = head
        curr = dum

        while curr and curr.next:
            if curr.next.val != val:
                curr = curr.next
            else:
                curr.next = curr.next.next
        
        return dum.next

        