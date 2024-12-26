class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            left, right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1
                left -= 1
                right += 1
            left, right = i,i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left : right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1
        
        return res




























# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         start, end, max_length = 0, 0, 0  # Rename variables to avoid shadowing
#         for i in range(len(s)):
#             cur = ""
#             for j in range(i, len(s)):
#                 cur = s[i:j+1]
#                 # Use slicing to reverse the string
#                 if cur == cur[::-1] and (j - i + 1) > max_length:
#                     max_length = j - i + 1
#                     start, end = i, j
#         # Return the correct substring
#         return s[start:end + 1]
