# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # if not head or not head.next or not head.next.next:
        #     return [-1, -1]
        
        arr1 = []
        var = 1
        p = head
        m = head.next
        n = head.next.next
        
        while n:
            if (m.val > p.val and m.val > n.val) or (m.val < p.val and m.val < n.val):
                arr1.append(var)
                
            p = p.next
            m = m.next
            n = n.next
            var += 1
        
        if len(arr1) < 2:
            return [-1, -1]
        
        mini = float("inf")
        for i in range(1, len(arr1)):
            mini = min(mini, arr1[i] - arr1[i - 1])
        
        max_distance = arr1[-1] - arr1[0]
        
        return [mini, max_distance]

# Example usage
# Assuming ListNode is defined and a linked list is created,
# you can create an instance of Solution and call nodesBetweenCriticalPoints like this:
# solution = Solution()
# result = solution.nodesBetweenCriticalPoints(head)
# print(result)
