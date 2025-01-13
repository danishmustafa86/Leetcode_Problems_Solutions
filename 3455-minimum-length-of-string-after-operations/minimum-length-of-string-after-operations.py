class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        n = 0
        for val in count.values():
            print(val)
            if val > 2:
                if val % 2 == 0:
                    n += 2
                else:
                    n += 1
            else:
                n += val
        return n