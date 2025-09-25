class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        for i in range(n):
            if i % (2*k) == 0:
                l,r = i, i+k-1
                if i+k-1 >= n-1:
                    r = n-1
                while l<r:
                    s[l],s[r] = s[r],s[l]
                    l += 1
                    r -= 1
        return "".join(s)