from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()  # Sort the input list to handle duplicates
        
        def dfs(i):
            if i == len(nums):
                # Append a copy of temp (as tuple) to avoid duplicate subsets
                if temp not in res:
                    res.append(temp[:])
                    print(temp[:])
                return 
            
            # Include the current number in the subset
            temp.append(nums[i])
            dfs(i + 1)
            
            # Backtrack and do not include the current number
            temp.pop()
            dfs(i + 1)
        print(res)
        dfs(0)
        return res

# Example usage:
# sol = Solution()
# print(sol.subsetsWithDup([1, 2, 2]))
