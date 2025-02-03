class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max1, max2 = 0,0
        cur1, cur2 = 1,1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                cur1 += 1
            else:
                max1 = max( max1, cur1)
                cur1 = 1
            if nums[i] > nums[i + 1]:
                cur2 += 1
            else:
                max2 = max( max2, cur2)
                cur2 = 1
        return max( max1, max2, cur1, cur2)
