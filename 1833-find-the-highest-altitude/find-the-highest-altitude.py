class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curAltitude = 0
        maxAltitude = 0
        for g in gain:
            curAltitude += g
            maxAltitude = max(curAltitude, maxAltitude)
        return maxAltitude