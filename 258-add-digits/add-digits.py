class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.sumDigits(num)
        return num

    def sumDigits(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum