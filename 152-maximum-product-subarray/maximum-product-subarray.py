from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize variables to track the maximum, minimum, and global maximum
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            num = nums[i]
            
            # If the current number is negative, swap max and min
            if num < 0:
                max_product, min_product = min_product, max_product

            # Update max_product and min_product
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            # Update the result with the global maximum
            result = max(result, max_product)

        return result
