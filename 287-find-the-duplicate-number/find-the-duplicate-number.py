class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                return nums[i]
            else:
                h[nums[i]] =  nums[i]
        return 0