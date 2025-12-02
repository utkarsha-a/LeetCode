# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode()
        res = dum
        tot = car = 0

        while l1 or l2 or car:
            tot = car
            if l1:
                tot+=l1.val
                l1 = l1.next
            if l2:
                tot+=l2.val
                l2 = l2.next

            num = tot%10
            car = tot//10

            dum.next = ListNode(num)
            dum = dum.next
        
        return res.next

        