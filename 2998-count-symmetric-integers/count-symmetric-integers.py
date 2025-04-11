class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for i in range(low, high+1):
            st = str(i)
            if len(st) % 2 == 0:
                half = len(st) // 2
                fh, lh = st[:half], st[half:]
                fh, lh = sum(int(ch) for ch in fh), sum(int(ch) for ch in lh)
                if fh  == lh:
                    count += 1
        return count