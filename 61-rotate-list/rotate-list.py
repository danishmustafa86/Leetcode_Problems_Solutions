# class ListNode:
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Determine the length of the list
        length = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        
        # Step 2: Make the list circular
        old_tail.next = head
        
        # Step 3: Find the new tail and new head
        k = k % length
        new_tail = head
        for _ in range(length - k - 1):  # Here is the loop with `_`
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # Step 4: Break the circular list
        new_tail.next = None
        
        return new_head
