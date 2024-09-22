class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        i = 1

        def count(cur):
            res = 0
            nei = cur + 1
            while cur <= n:
                nei = min(nei, n+1)
                res += nei - cur
                nei *= 10
                cur *= 10
            return res

        while i< k:
            step = count(cur)
            if i + step <= k:
                cur = cur+1
                i += step
            else:
                cur *= 10
                i += 1
            
        return cur