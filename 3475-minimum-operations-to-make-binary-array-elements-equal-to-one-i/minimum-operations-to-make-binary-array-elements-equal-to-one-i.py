class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                flips += 1
                nums[i] = 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
        return flips if nums[-1] == 1 and nums[-2] == 1 else -1







# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         flips = 0
#         for i in range(len(nums)-2):
#             if nums[i] == 0:
#                 flips += 1
#                 for j in range(i,i+3):
#                     if nums[j] == 0:
#                         nums[j] = 1
#                     else:
#                         nums[j] = 0
#         return flips if nums.count(1) == len(nums) else -1





























# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         flip = 0
#         for i in range(len(nums)-2):
#             if nums[i] == 0:
#                 flip += 1
#                 for j in range(i,i+3):
#                     if nums[j] == 0:
#                         nums[j] = 1
#                     else:
#                         nums[j] = 0
#         return flip if nums.count(1) == len(nums) else -1








# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         flip = 0
#         for i in range(len(nums) - 2):
#             if nums[i] == 0:
#                 flip += 1
#                 nums[i] == 1
#                 nums[i+1] ^= 1
#                 nums[i+2] ^= 1
        
#         return flip if nums[-1] == 1 and nums[-2] == 1 else -1