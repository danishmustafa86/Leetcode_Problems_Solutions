class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(1,len(nums)):
            if nums[left] != 0:
                left += 1
                continue
            else:
                if nums[right] != 0:
                    nums[right], nums[left] = nums[left] , nums[right];
                    left += 1
        return nums
