class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0
        for i in range(len(nums) - 1):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp
        max1 = rob2
        rob1, rob2 = 0, 0
        for i in range(len(nums) - 1, 0, -1):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp

        return max(nums[0],max1, rob2)