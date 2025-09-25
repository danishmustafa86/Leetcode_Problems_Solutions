class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res








        # n = bin(nu)[2:].zfill(32)
        # n = list(str(n))
        # n.reverse()
        # n = "".join(n)
        # return int(n,2)