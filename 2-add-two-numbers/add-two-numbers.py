# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        tot = carry = 0

        while l1 or l2 or carry:
            tot = carry
            if l1:
                tot += l1.val
                l1 = l1.next
            if l2:
                tot += l2.val
                l2 = l2.next
            num = tot%10
            carry = tot//10


            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next


