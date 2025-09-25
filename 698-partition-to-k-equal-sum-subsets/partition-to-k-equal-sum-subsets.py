from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        nums.sort(reverse=True)
        n = len(nums)
        memo = {}

        def backtrack(used, current_sum, groups_formed):
            if groups_formed == k:
                return True  # Successfully formed k groups
            
            if (used, current_sum, groups_formed) in memo:
                return memo[(used, current_sum, groups_formed)]
            
            if current_sum == target:
                # Start a new subset
                result = backtrack(used, 0, groups_formed + 1)
                memo[(used, current_sum, groups_formed)] = result
                return result

            for i in range(n):
                if not (used & (1 << i)) and current_sum + nums[i] <= target:
                    if backtrack(used | (1 << i), current_sum + nums[i], groups_formed):
                        memo[(used, current_sum, groups_formed)] = True
                        return True
            
            memo[(used, current_sum, groups_formed)] = False
            return False

        return backtrack(0, 0, 0)
