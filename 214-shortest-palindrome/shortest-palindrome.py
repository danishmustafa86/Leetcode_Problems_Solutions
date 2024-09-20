class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        for i in range(len(s), 0, -1):
            cur = s[:i]
            rev = cur[::-1]
            right = s[i:]
            if  cur == rev:
                return right[::-1] + s
            