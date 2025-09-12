# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fat = fast.next.next

            if slow == fast:
                break
        else:
            return None

        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow
        '''
        s = set()
        curr = head
        while curr:
            if curr in s:
                return curr
            s.add(curr)
            curr = curr.next
        return None



