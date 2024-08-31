# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        num1.reverse()
        num2.reverse()
        num1 = int("".join(map(str,num1)))
        num2 = int("".join(map(str,num2)))

        num = num1 + num2
        res = list(map(int,str(num)))[::-1]

        dummy = ListNode(0)
        cur = dummy
        for i in res:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next






















        