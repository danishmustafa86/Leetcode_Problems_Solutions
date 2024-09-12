class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        Max = [nums[i] for i in range(len(nums)) if i%2 == 0]
        return sum(Max)