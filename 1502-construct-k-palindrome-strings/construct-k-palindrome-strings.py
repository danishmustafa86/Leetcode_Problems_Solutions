class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        count = Counter(s)
        odd = 0
        for key in count.values():
            odd += key % 2
        return odd <= k