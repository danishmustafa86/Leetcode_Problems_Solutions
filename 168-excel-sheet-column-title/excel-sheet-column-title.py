class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            letter = chr(remainder + ord('A'))
            result.append(letter)
            columnNumber = columnNumber // 26
        result.reverse()
        return "".join(result)