class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        Max = 0
        for i in range(0,len(nums)-1,2):
            cur = min(nums[i], nums[i+1])
            Max += cur
        return Max