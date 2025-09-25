class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xgate = start ^ goal
        return bin(xgate).count("1")