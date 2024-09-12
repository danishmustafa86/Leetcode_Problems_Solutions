class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        Max = 0
        for i in range(0,len(nums)-1,2):
            Max += nums[i]
        return Max