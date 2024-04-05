# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s,f=head,head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        prev=None
        curr=s.next
        while curr:
            new= curr.next
            curr.next=prev
            prev=curr
            curr=new
        s.next=None
        l1=head
        l2=prev
        while l2 != None:
            t1=l1.next
            t2=l2.next
            l1.next=l2
            l2.next=t1
            l1,l2=t1,t2