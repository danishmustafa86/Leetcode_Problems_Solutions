class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = [ -i for i in nums]
        heapq.heapify(num)
        for i in range(k-1):
            cur = heapq.heappop(num)
        return -heapq.heappop(num)
