# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = end = head
        for i in range(k-1):
            first = first.next
        res = first
        while first.next:
            end = end.next
            first = first.next
        res.val, end.val = end.val, res.val
        return head
        