from collections import defaultdict
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Dictionary to store the two largest numbers for each digit sum
        digit_sum_map = defaultdict(list)
        
        # Calculate the sum of digits for each number and group them
        for num in nums:
            val = sum(map(int, str(num)))
            digit_sum_map[val].append(num)
        
        max_sum = -1
        
        # Iterate through the groups and find the maximum sum of pairs
        for key in digit_sum_map:
            if len(digit_sum_map[key]) >= 2:
                # Sort the list in descending order and take the top two
                sorted_nums = sorted(digit_sum_map[key], reverse=True)
                current_sum = sorted_nums[0] + sorted_nums[1]
                max_sum = max(max_sum, current_sum)
        
        return max_sum