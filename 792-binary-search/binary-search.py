class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target == nums[0]:
        #     return 0
        l,r = 0, len(nums)-1
        while l <= r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            else:
                l += 1
                r -= 1
        return -1
