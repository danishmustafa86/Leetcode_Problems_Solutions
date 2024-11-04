class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0  # Edge case where k is too small to have any valid subarray

        product = 1
        left = 0
        res = 0

        for right in range(len(nums)):
            product *= nums[right]

            # Shrink the window from the left while the product is greater or equal to k
            while product >= k and left <= right:
                product //= nums[left]
                left += 1

            # The number of subarrays ending at `right` is (right - left + 1)
            res += right - left + 1

        return res
