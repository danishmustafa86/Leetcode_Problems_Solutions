class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        hsh = {}
        for i in candyType:
            hsh[i] = 1
        maxEat = len(candyType) // 2
        hshLen = len(hsh)
        if hshLen> maxEat:
            return maxEat
        else:
            return hshLen