class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        length = 0
        for i in range(len(s)):
            if words[i][0] == s[i]:
                length += 1
                if length == len(words):
                    return True
        return False
