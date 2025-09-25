class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        stone_count = {}
        jewel_count = 0
        for stone in stones:
            if stone in stone_count:
                stone_count[stone] += 1
            else:
                stone_count[stone] = 1
            if stone in jewel_set:
                jewel_count += 1
        return jewel_count