class Solution:



    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []
        def recursion(candidate, target, i , curSum, temp):
            if curSum > target:
                return
            if i == len(candidate):
                if curSum == target:
                    ans.append(temp[:])
                return
            # Inclusion
            curSum += candidate[i]
            temp.append(candidate[i])
            recursion(candidate, target, i, curSum, temp)
            curSum -= candidate[i]
            temp.pop()
            # Exclusion
            recursion(candidate, target, i+1, curSum, temp)
        recursion(candidates, target, 0 , 0 , temp)
        return ans