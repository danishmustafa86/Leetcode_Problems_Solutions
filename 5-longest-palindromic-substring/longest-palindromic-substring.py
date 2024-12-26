class Solution:
    def longestPalindrome(self, s: str) -> str:
        st,e , ml = 0, 0, 0
        for i in range(len(s)):
            cur = ""
            for j in range(i, len(s)):
                cur = s[i:j+1]
                if cur[::-1] == cur and (j - i) > ml:
                    ml = j - i
                    st , e = i, j
        return s[st:e + 1]
