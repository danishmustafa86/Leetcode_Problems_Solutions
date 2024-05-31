class Solution:
    def jump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return 0

        farthest = end = jump = 0
        for i, j in enumerate(nums):
            farthest = max(farthest, i+j)
            
            if farthest >= len(nums)-1:
                jump += 1
                break

            if i == end:
                jump += 1
                end = farthest
        return jump