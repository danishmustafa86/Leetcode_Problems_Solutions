class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        # XOR all elements of nums1 `len(nums2)` times
        if len(nums2) % 2 == 1:  # Contributes only if nums2's length is odd
            for num in nums1:
                result ^= num

        # XOR all elements of nums2 `len(nums1)` times
        if len(nums1) % 2 == 1:  # Contributes only if nums1's length is odd
            for num in nums2:
                result ^= num

        return result





# class Solution:
#     def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
#         result = 0
#         for i in range(len(nums1)):  # Outer loop
#             for j in range(len(nums2)):  # Inner loop
#                 result ^=( nums1[i] ^ nums2[j])
       
#         return result
