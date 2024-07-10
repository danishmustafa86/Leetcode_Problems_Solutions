class Solution:
    def getSum(self, a: int, b: int) -> int:
        if b > 0:
            while b > 0:
                a += 1
                b -= 1
        elif b < 0:
            while b < 0:
                a -= 1
                b += 1
        return a