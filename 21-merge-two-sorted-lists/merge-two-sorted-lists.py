# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        
        cur.next = l1 if l1 else l2
        cur = cur.next

        return dummy.next


        '''
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val<=l2.val:
                cur.next= l1
                cur = cur.next
                l1 = l1.next
            elif l2.val<l1.val:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
            
        if l1:
            cur.next = l1
            cur = cur.next
        if l2:
            cur.next = l2
            cur = cur.next

        return dummy.next  
        '''     


        