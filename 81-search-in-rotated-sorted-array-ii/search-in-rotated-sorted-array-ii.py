class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums



        # i = 0
        # j = len(nums)-1
        # while i < j:
        #     mid = i + j // 2
        #     if nums[mid] < target:
        #         j = mid