from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        def backtrack(i, temp):
            if i == len(nums):
                res.append(temp[::])
                return
            temp.append(nums[i])
            backtrack(i + 1, temp)
            temp.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1 , temp)


        backtrack(0,[])
        return res

# Example usage:
# sol = Solution()
# print(sol.subsetsWithDup([1, 2, 2]))
