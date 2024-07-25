class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        x = 0
        for i in range(len(nums)):
            if i not in nums:
                x= i
        if x == 0:
            return max(nums) + 1
        else:
            return x
