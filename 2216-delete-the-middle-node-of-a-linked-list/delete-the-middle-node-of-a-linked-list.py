# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            prev = prev.next
            fast = fast.next.next
        
        prev.next = slow.next
        return dummy.next
        