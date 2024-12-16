class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        left = 0
        for right in range(len(nums)):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[left] != 0:
                left += 1
        return nums


        

        # left = 0
        # for right in range(len(nums)):
        #     if nums[left] != 0:
        #         left += 1
        #         continue
        #     if nums[right] != 0:
        #         nums[right], nums[left] = nums[left], nums[right]
        #         left += 1
        # return nums




        