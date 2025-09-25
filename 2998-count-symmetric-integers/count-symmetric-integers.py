class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(
            sum(map(int, str(i)[:len(str(i))//2])) == sum(map(int, str(i)[len(str(i))//2:]))
            for i in range(low, high + 1)
            if len(str(i)) % 2 == 0
        )
