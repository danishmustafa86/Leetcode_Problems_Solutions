# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = [], []
        cur = l1
        while cur:
            n1.append(str(cur.val))
            cur = cur.next
        cur = l2
        while cur:
            n2.append(str(cur.val))
            cur = cur.next
        
        n1.reverse()
        n1 = "".join(n1)
        n2.reverse()
        n2 = "".join(n2)
        sm = int(n1) + int(n2)
        sm = str(sm)
        sm = list(sm)
        # sm.reverse()
        sm = "".join(sm)
        ans = []
        for i in range(len(sm)-1, -1, -1):
            ans.append(int(sm[i]))
        
        dummy = ListNode()
        tail = dummy
        for i in range(len(ans)):
            tail.next = ListNode(int(ans[i]))
            tail = tail.next
        return dummy.next

