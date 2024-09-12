class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for v in words[i]:
                if v not in allowed:
                    count -= 1
                    break
            count += 1
        return count
