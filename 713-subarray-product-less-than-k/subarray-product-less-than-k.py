class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k < 1:
            return 0

        product = 1
        left = 0
        res = 0
        for right in range(len(nums)):
            product = product * nums[right]

            while product >= k and left <= right:
                product = product // nums[left]
                left += 1
            res += right - left + 1
        return res
            































# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         if k <= 1:
#             return 0  

#         product = 1
#         left = 0
#         res = 0

#         for right in range(len(nums)):
#             product *= nums[right]

         
#             while product >= k and left <= right:
#                 product //= nums[left]
#                 left += 1

#             res += right - left + 1

#         return res
