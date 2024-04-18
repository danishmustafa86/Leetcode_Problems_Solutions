class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        count = 0
        index = len(s) - 1

        # Skip trailing spaces
        while index >= 0 and s[index] == " ":
            index -= 1

        # Count the characters of the last word
        while index >= 0 and s[index] != " ":
            count += 1
            index -= 1

        return count
