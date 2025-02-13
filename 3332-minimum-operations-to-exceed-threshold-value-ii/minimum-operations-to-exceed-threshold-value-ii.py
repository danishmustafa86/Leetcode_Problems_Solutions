class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        op = 0
        while nums[0] < k:
            op +=  1
            n1, n2 = heapq.heappop(nums), heapq.heappop(nums)
            cur = min(n1, n2) * 2 + max(n1, n2)
            heapq.heappush(nums, cur)

        return op