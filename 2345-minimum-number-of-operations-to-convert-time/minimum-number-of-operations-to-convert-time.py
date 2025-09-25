class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur = (int(current[:2]) * 60) + int(current[3:])
        cor = (int(correct[:2]) * 60) + int(correct[3:])
        diff = cor - cur
        ans = 0
        for val in [60, 15, 5, 1]:
            if diff >= val:
                ans += diff // val
                diff = diff % val

        return ans