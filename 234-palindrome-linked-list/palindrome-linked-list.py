# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp

        f, s = head, node

        while s:
            if f.val != s.val:
                return False
            f = f.next
            s = s.next

        return True
        