class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        slow, fast = head, head
        prev = None

        # Find the middle node (slow)
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect left half from the mid
        if prev:
            prev.next = None

        root = TreeNode(slow.val)
        if head != slow:  # To avoid infinite loop
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
        