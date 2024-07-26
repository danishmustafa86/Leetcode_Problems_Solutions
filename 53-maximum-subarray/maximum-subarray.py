class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        cur = 0
        for i in nums:
            if cur < 0:
                cur = 0
            cur += i
            maxsub = max(cur, maxsub)
        return maxsub