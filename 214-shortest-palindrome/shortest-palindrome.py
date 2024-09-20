class Solution:
    def shortestPalindrome(self, s: str) -> str:

        for i in range(len(s), 0, -1):
            back = s[:i]
            rev = back[::-1]
            front = s[i:]
            if  back == rev:
                return front[::-1] + s
        return ""