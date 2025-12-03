# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None

        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f==s:
                break
        else:
            return None

        f = head
        while f!=s:
            f = f.next
            s = s.next
        return s
        
        '''
        s = set()
        curr = head
        while curr:
            if curr in s:
                return curr
            s.add(curr)
            curr = curr.next
        return None
        '''



