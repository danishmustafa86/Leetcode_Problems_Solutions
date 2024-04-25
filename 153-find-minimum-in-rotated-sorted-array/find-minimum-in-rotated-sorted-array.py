class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        for i in range(len(nums)):
            if minimum > nums[i]:
                minimum = nums[i]
        return minimum