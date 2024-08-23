class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flip = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                flip += 1
                for j in range(i,i+3):
                    if nums[j] == 0:
                        nums[j] = 1
                    else:
                        nums[j] = 0
        return flip if nums.count(1) == len(nums) else -1