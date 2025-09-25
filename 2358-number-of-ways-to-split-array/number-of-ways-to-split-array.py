class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        tsum = sum(nums)
        n = 0
        cursum = 0
        for i in range(len(nums) - 1):
            tsum = tsum - nums[i]
            cursum += nums[i]
            if cursum >= tsum :
                n += 1
        return n