from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: Compute the sum of all subarrays of size k
        subarray_sums = [sum(nums[:k])]
        for i in range(1, n - k + 1):
            subarray_sums.append(subarray_sums[-1] - nums[i - 1] + nums[i + k - 1])
        
        # Step 2: Find the left max indices
        left = [0] * len(subarray_sums)
        max_index = 0
        for i in range(len(subarray_sums)):
            if subarray_sums[i] > subarray_sums[max_index]:
                max_index = i
            left[i] = max_index
        
        # Step 3: Find the right max indices
        right = [0] * len(subarray_sums)
        max_index = len(subarray_sums) - 1
        for i in range(len(subarray_sums) - 1, -1, -1):
            if subarray_sums[i] >= subarray_sums[max_index]:
                max_index = i
            right[i] = max_index
        
        # Step 4: Find the best middle subarray
        max_sum = 0
        result = []
        for j in range(k, len(subarray_sums) - k):
            i, l = left[j - k], right[j + k]
            total_sum = subarray_sums[i] + subarray_sums[j] + subarray_sums[l]
            if total_sum > max_sum:
                max_sum = total_sum
                result = [i, j, l]
        
        return result
