class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_happy = 3 * (2**(n- 1))
        left, right = 1, total_happy
        choices = "abc"
        res = []
        for i in range(n):
            cur = left
            partition = ( right - left + 1) // len(choices)

            for c in choices:
                if k in range(cur , cur + partition):
                    res.append(c)
                    left = cur
                    right= cur + partition - 1
                    choices = "abc".replace(c, "")
                    break
                cur += partition
        return "".join(res)