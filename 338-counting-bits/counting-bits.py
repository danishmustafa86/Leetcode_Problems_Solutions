class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        b = 0
        for i in range(n+1):
            b = bin(i)
            arr.append(b.count("1"))
        return arr 