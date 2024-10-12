class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, temp, curSum):
            if curSum == target:
                res.append(temp[::])
                return 
            if i == len(candidates) or curSum > target:
                return
            curSum += candidates[i]
            temp.append(candidates[i])
            backtrack(i+1, temp, curSum)
            curSum -= candidates[i]
            temp.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, temp, curSum)
        
        backtrack(0,[],0)
        return res