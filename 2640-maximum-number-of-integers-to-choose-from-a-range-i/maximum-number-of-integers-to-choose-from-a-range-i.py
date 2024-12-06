class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        hsh = {i:i for i in banned}
        ans = 0
        sumIs = 0
        for i in range(1,n+1):
            
            if i not in hsh and sumIs + i <= maxSum:
                sumIs += i
                ans += 1
        return ans