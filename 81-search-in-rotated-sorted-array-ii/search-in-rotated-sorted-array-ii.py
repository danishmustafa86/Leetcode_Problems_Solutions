class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # return target in nums
        arr = set(nums)
        nums = list(arr)
        print(nums)  # corrected from 'num' to 'nums'
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2  # added parentheses to ensure correct order of operations
            # for first half
            if nums[i] <= nums[mid]:
                if nums[mid] == target:
                    return True
                elif nums[i] <= target <= nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            # for 2nd half
            else:
                if nums[mid] == target:
                    return True
                elif nums[mid] <= target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        return False












# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         # return target in nums
#         arr = set(nums)
#         nums = list(arr)
#         i = 0
#         j = len(nums)-1
#         while i <= j:
#             mid = i + j // 2
#             # for first half
#             if nums[i] <= nums[mid]:
#                 if nums[mid] == target:
#                     return True
#                 elif nums[i] <= target and target <= nums[mid]:
#                     j = mid - 1
#                 else:
#                     i = mid + 1
#             # for 2nd half
#             else:
#                 if nums[mid] == target:
#                     return True
#                 elif nums[mid] <= target and target <= nums[j]:
#                     i = mid + 1
#                 else:
#                     j = mid - 1
        
#         return False
