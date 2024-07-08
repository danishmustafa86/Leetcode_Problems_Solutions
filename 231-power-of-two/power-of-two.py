class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n/2 > n//2:
            print("hellossofaghso")
            return False
        num = n
        twos = 1
        while num//2 >= 2:
            # if num/2 > num//2:
            #     return False
            num = num//2
            twos += 1 
        if 2**twos == n:
            return True
        return False