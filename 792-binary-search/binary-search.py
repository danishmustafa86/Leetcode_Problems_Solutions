class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        for i in range(len(nums)):
            if target == nums[i]:
                index = i
        return index