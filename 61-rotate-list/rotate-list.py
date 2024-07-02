# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        lenght = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            lenght += 1

        old_tail.next = head

        k = k%lenght
        new_tail = head
        for _ in range(lenght - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head