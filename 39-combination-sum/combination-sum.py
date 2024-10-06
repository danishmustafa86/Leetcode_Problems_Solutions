class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recursion(candidates, target, i, curSum, temp, ans):
            if curSum > target:
                return
            if curSum == target:
                ans.append(temp[:])  # Append a copy of temp
                return
            if i == len(candidates):
                return
            # Inclusion
            temp.append(candidates[i])
            recursion(candidates, target, i, curSum + candidates[i], temp, ans)
            temp.pop()  # Remove the last element to backtrack
            # Exclusion
            recursion(candidates, target, i + 1, curSum, temp, ans)

        ans = []
        recursion(candidates, target, 0, 0, [], ans)
        return ans
