class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        curSum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[ i - 1]:
                curSum += nums[i]
            else:
                maxSum = max( maxSum, curSum)
                curSum = nums[i]
        return max(maxSum, curSum)

