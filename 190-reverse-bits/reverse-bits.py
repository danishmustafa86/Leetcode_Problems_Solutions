class Solution:
    def reverseBits(self, nu: int) -> int:
        n = bin(nu)[2:].zfill(32)
        n = list(str(n))
        n.reverse()
        n = "".join(n)
        print(n)
        n = int(n,2)
        return n


