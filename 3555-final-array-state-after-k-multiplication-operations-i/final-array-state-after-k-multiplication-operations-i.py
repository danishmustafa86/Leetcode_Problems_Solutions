class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            num = float("inf")
            cur = 0
            for i in range(len(nums)):
                if nums[i] < num:
                    num = nums[i]
                    cur = i
            nums[cur] *= multiplier
        return nums
            