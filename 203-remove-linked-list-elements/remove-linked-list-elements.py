class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases more easily
        dummy = ListNode(0)
        dummy.next = head
        
        cur = dummy  # Start with the dummy node
        
        # Traverse the list
        while cur.next:
            if cur.next.val == val:
                # Skip the node with the value `val`
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        # Return the next node of dummy, which is the new head
        return dummy.next
