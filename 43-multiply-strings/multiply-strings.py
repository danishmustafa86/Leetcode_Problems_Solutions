class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        r1 = 0
        r2 = 0
        for i in num1:
            dig = ord(i) - ord("0")
            r1 = r1 * 10 + dig
        for i in num2:
            dig = ord(i) - ord("0")
            r2 = r2 * 10 + dig
        ans = r1*r2
        result = []
        if ans == 0:
            return "0"
        while ans>0:
            remainder = ans%10
            result.append(chr(remainder + ord("0")))
            ans = ans//10
        result.reverse()
        return "".join(result)