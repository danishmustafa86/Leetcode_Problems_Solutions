# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        cur = head
        while cur:
            while stack and stack[-1] < cur.val:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next
        
        dummy = ListNode()
        cur = dummy
        for val in stack:
            cur.next = ListNode(val)
            cur = cur.next
        
        return dummy.next











# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         def reverse(head):
#             prev, cur = None, head
#             while cur:
#                 tmp = cur.next
#                 cur.next = prev
#                 prev, cur = cur, tmp
#             return prev

#         head = reverse(head)

#         cur = head
#         max_val = cur.val
#         while cur.next:
#             if cur.next.val < max_val:
#                 cur.next = cur.next.next
#             else:
#                 max_val = cur.next.val
#                 cur = cur.next


#         return reverse(head)














# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         cur = head
#         stack = []
#         while cur:
#             while stack and stack[-1] < cur.val:
#                 stack.pop()
#             stack.append(cur.val)
#             cur = cur.next
        
#         dummy = ListNode()
#         cur = dummy
#         for val in stack:
#             cur.next = ListNode(val)
#             cur = cur.next
        
#         return dummy.next
        