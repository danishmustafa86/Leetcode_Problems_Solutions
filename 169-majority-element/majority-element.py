class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums)//2]
        return mid


















        # nums.sort()
        # return nums[len(nums)//2]